Builds and publishes the [NewX](https://github.com/crimera/piko/tree/x-lite) patch bundle from the [Piko `x-lite` branch](https://github.com/crimera/piko/tree/x-lite).

[Latest Release](https://github.com/crimera/x-lite-apk/releases/latest)

# Releasing

Each release publishes the built `bins/patches.mpp` bundle. Optionally, a detached
GPG signature (`bins/patches.mpp.asc`) is attached alongside it, mirroring how
Morphe/Piko ship a `<bundle>.mpp.asc` next to the patch bundle.

To enable signing, add these to the repo's **Settings → Secrets and variables**:

- `GPG_PRIVATE_KEY` (repo secret) — armored private key
- `GPG_PASSPHRASE` (repo secret) — key passphrase
- `GPG_FINGERPRINT` (repo variable) — key fingerprint

Without them the workflow skips signing and still ships the unsigned bundle.

# Credits
- [morphe](https://github.com/MorpheApp) - patcher
- [revanced](https://github.com/ReVanced) - previous patcher
- [j-hc](https://github.com/j-hc) - Project is inspired by j-hc's revanced builder template.
