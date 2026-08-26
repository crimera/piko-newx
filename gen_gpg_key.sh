#!/usr/bin/env bash
#
# Generates a GPG key for signing x-lite-apk patch bundle releases and writes
# the corresponding GitHub Actions secrets/variables to a text file in
# VARIABLE=VALUE format.
#
# The output file (gpg-secrets.txt) contains the PRIVATE KEY. It is chmod 600
# and git-ignored — never commit it.
#
# Usage:
#   ./gen_gpg_key.sh
#
# Override defaults via environment variables:
#   KEY_NAME      display name   (default: x-lite-apk)
#   KEY_EMAIL     key email      (default: noreply@users.noreply.github.com)
#   KEY_LENGTH    RSA bits       (default: 4096)
#   OUT_FILE      output path    (default: gpg-secrets.txt)
#   GPG_PASSPHRASE passphrase    (prompted if unset)

set -euo pipefail

KEY_NAME="${KEY_NAME:-x-lite-apk}"
KEY_EMAIL="${KEY_EMAIL:-noreply@users.noreply.github.com}"
KEY_LENGTH="${KEY_LENGTH:-4096}"
OUT_FILE="${OUT_FILE:-gpg-secrets.txt}"

# Passphrase: from env or interactive prompt.
if [[ -z "${GPG_PASSPHRASE:-}" ]]; then
  read -r -s -p "Enter GPG passphrase: " GPG_PASSPHRASE
  echo
fi

if ! command -v gpg >/dev/null 2>&1; then
  echo "gpg not found. Install it first:" >&2
  echo "  brew install gnupg" >&2
  exit 1
fi

# Reuse an existing key for this email instead of generating a duplicate.
# gpg exits non-zero when no key matches yet; that is expected here, so the
# `|| true` keeps `set -e`/pipefail from aborting the script.
FINGERPRINT=$(gpg --list-secret-keys --with-colons "${KEY_EMAIL}" 2>/dev/null \
  | awk -F: '/^fpr:/ { print $10; exit }') || true

if [[ -n "${FINGERPRINT}" ]]; then
  echo "Secret key for ${KEY_EMAIL} already exists (${FINGERPRINT}); reusing."
else
  echo "Generating GPG key for ${KEY_NAME} <${KEY_EMAIL}>..."
  batch_file=$(mktemp)
  cat > "${batch_file}" <<EOF
Key-Type: RSA
Key-Length: ${KEY_LENGTH}
Name-Real: ${KEY_NAME}
Name-Email: ${KEY_EMAIL}
Expire-Date: 0
Passphrase: ${GPG_PASSPHRASE}
%commit
EOF
  gpg --batch --pinentry-mode loopback --gen-key "${batch_file}"
  rm -f "${batch_file}"

  FINGERPRINT=$(gpg --list-secret-keys --with-colons "${KEY_EMAIL}" 2>/dev/null \
    | awk -F: '/^fpr:/ { print $10; exit }') || true
fi

if [[ -z "${FINGERPRINT}" ]]; then
  echo "Failed to determine fingerprint." >&2
  exit 1
fi

PRIVATE_KEY=$(gpg --pinentry-mode loopback --passphrase "${GPG_PASSPHRASE}" \
  --armor --export-secret-keys "${FINGERPRINT}")

{
  echo "# GitHub Actions secrets/variables for x-lite-apk releases"
  echo "# Paste GPG_PRIVATE_KEY and GPG_PASSPHRASE as Secrets,"
  echo "# GPG_FINGERPRINT as a Variable (Settings -> Secrets and variables -> Actions)."
  echo "# GPG_PRIVATE_KEY is multi-line; copy everything between the ##### markers"
  echo "# (the BEGIN/END PGP lines are part of the value, the ##### lines are not)."
  echo
  echo "##### GPG_PRIVATE_KEY START"
  echo "GPG_PRIVATE_KEY=${PRIVATE_KEY}"
  echo "##### GPG_PRIVATE_KEY END"
  echo "GPG_PASSPHRASE=${GPG_PASSPHRASE}"
  echo "GPG_FINGERPRINT=${FINGERPRINT}"
} > "${OUT_FILE}"

chmod 600 "${OUT_FILE}"
echo "Wrote ${OUT_FILE} (chmod 600). Add its values to the repo's Actions secrets/variables."
