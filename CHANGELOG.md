# [12.22.0-prod.01-b64d10b](https://github.com/crimera/piko-newx/releases/tag/12.22.0-prod.01-b64d10b) (2026-09-03)

### Commits
* [`9e07558`](https://github.com/crimera/piko/commit/9e0755891fb27d7aacb720d1b242aad023822640) feat(newx): add Grok button to customizable drawer items
* [`b64d10b`](https://github.com/crimera/piko/commit/b64d10b74d150035129c92361f7ebd0895b3f63a) feat(newx): add theme toggle to customizable drawer items

# [12.22.0-prod.01-1ea926c](https://github.com/crimera/piko-newx/releases/tag/12.22.0-prod.01-1ea926c) (2026-09-03)

### Commits
* [`09e359e`](https://github.com/crimera/piko/commit/09e359e87de37169916f2a213aca6ba20d554fab) fix(newx): reorder timeline scrolling and refresh settings
* [`1ea926c`](https://github.com/crimera/piko/commit/1ea926cd17b8dab9888cc22917111d8ebf5ebeec) feat(newx): add compatibility for 12.22.0-prod.01

# [12.22.0-beta.01-dfc8c56](https://github.com/crimera/piko-newx/releases/tag/12.22.0-beta.01-dfc8c56) (2026-09-01)

### Commits
* [`dfc8c56`](https://github.com/crimera/piko/commit/dfc8c562dc3dcd9397c65e43ebacc8db12980a1c) fix(newx): support Twitter 12.21.1-prod.05

# [12.22.0-beta.01-d628357](https://github.com/crimera/piko-newx/releases/tag/12.22.0-beta.01-d628357) (2026-08-30)

### Commits
* [`3ef30b7`](https://github.com/crimera/piko/commit/3ef30b795c40ab371497789d019c8188b9df4ef1) fix(newx): preserve initial timeline load on fresh start while suppressing auto-refresh
* [`d628357`](https://github.com/crimera/piko/commit/d628357ababe4866c654fd4be64d5a066b43485f) fix(newx): correct inverted branch in URT repository auto-refresh filter

# [12.22.0-beta.01-f7a090a](https://github.com/crimera/piko-newx/releases/tag/12.22.0-beta.01-f7a090a) (2026-08-30)

### Commits
* [`cd57e8f`](https://github.com/crimera/piko/commit/cd57e8f0335d8462869ccb4b88137d780a395526) feat(newx): enable patches by default except browse object
* [`23a6a29`](https://github.com/crimera/piko/commit/23a6a2920670259adc907515af81516b5a8875bb) feat(newx): filter promoted trends, event summaries, and spotlight ads in Explore feeds
* [`9bdc9ae`](https://github.com/crimera/piko/commit/9bdc9aef5de624292dfdc23cbe7b8aba3d7ec3ed) feat(newx): add Trends and Explore group with toggles for promoted trends and event summaries
* [`ef388aa`](https://github.com/crimera/piko/commit/ef388aa7ff3f0894a4b76bc7975bc982a008fc60) refactor(newx): remove standalone trends toggles in favor of unified ad removal
* [`de7164e`](https://github.com/crimera/piko/commit/de7164e14fcbdea1b292628f5c417d2e7a24a900) fix(newx): resolve ClassCastException in URT timeline and bump target to 12.20.5-prod.01
* [`f3adb53`](https://github.com/crimera/piko/commit/f3adb533ce0de0ec6348148ceb3c15b304039d9a) fix(patches): update custom sharing domain hooks for 12.20.5-prod.01
* [`6d94538`](https://github.com/crimera/piko/commit/6d9453842411e3b3563acc7aacbbb8e6ba985b61) fix(newx): port Inline download button to 12.20.5-prod.01
* [`a8e35c6`](https://github.com/crimera/piko/commit/a8e35c6989231556c2401738c62ed6f6f12dc8ca) fix(newx): resolve DIM palette factory disambiguation in Dynamic color for 12.20.5-prod.01
* [`b0b8ea3`](https://github.com/crimera/piko/commit/b0b8ea3d5f4cadc53396eeb797fedb831f1be18f) fix(newx): broaden immutable list converter fingerprint and add 12.22.0-beta.01 support
* [`f3e3a3f`](https://github.com/crimera/piko/commit/f3e3a3f47d9ad35d109f633c2beff1e8ae0a1a85) fix(newx): handle packed-switch default fallthrough in Dynamic color
* [`dcff33b`](https://github.com/crimera/piko/commit/dcff33b288d5d4dce7284096e75f6a2945ae0042) fix(newx): port default reply sorting for 12.20.5 and 12.22.0
* [`7c80940`](https://github.com/crimera/piko/commit/7c8094046f01ad441599de6ea61a51a5bce52fc7) fix(newx): update video quality bitrate telemetry hooks and strip legacy paths
* [`4e955fb`](https://github.com/crimera/piko/commit/4e955fbdef9df3137c9cb4204e7fa1060297bb9a) fix(newx): resolve post contextual wrapper unwrapping in timeline text adapter
* [`70a92f7`](https://github.com/crimera/piko/commit/70a92f77f959e180ede7385fb90490d21e9c883c) fix(newx): resolve topic_ids field from GraphQL serializer in For You topic filter
* [`7a71dc2`](https://github.com/crimera/piko/commit/7a71dc23225cfaff5ba9e067305c2caeb9685966) fix(newx): port disable video player scrolling to merged Compose VerticalPager
* [`3548b06`](https://github.com/crimera/piko/commit/3548b068b4e8fcd715afed13f2986e5f3ea2a674) fix(newx): hook stable onResume lifecycle listener in Disable auto refresh
* [`ce1c30f`](https://github.com/crimera/piko/commit/ce1c30fc457ab2825c0be2d81b9a31f86d8cca6a) fix(newx): port restore timeline position to stable component scroll state
* [`fe36aee`](https://github.com/crimera/piko/commit/fe36aee54ab11b10ec416fc24c3bcac5497c18af) fix(newx): port open canonical URLs to unified navigation handlers
* [`8499638`](https://github.com/crimera/piko/commit/8499638e6b581b328f3c4f7ec48b89cc22ed9a9b) chore: update patches-list.json with supported targets 12.20.5-prod.01 and 12.22.0-beta.01
* [`d9f111a`](https://github.com/crimera/piko/commit/d9f111a35f78bfcd9359dd33cfd4a287f38fb528) fix(newx): unshorten rich-text and bio display URLs in canonical URLs patch
* [`efce4de`](https://github.com/crimera/piko/commit/efce4dee9e8aa6b27bfb1aba8f8941c06dc8cce1) fix(newx): canonicalize profile links
* [`a68e7f5`](https://github.com/crimera/piko/commit/a68e7f5af39b467688112f1ef596a39f012bce74) fix(newx): scope timeline auto-refresh disable to home reselect and prevent breaking post details
* [`da04712`](https://github.com/crimera/piko/commit/da04712b50edabfaf0ae65dcc251740b521ec7d0) fix(newx): suppress URT lifecycle refresh exclusively for FOR_YOU and FOLLOWING
* [`553294c`](https://github.com/crimera/piko/commit/553294c3baa2d30d8dfecd90b91f7c462d86f42b) fix(newx): apply custom sharing domain to post copy link and system share intent
* [`f7a090a`](https://github.com/crimera/piko/commit/f7a090a85035259ccc671d1c9714f2eb4aca45e1) fix(newx): hook share sheet copy link callbacks for custom sharing domain

# [12.19.1-release.0-229b738](https://github.com/crimera/piko-newx/releases/tag/12.19.1-release.0-229b738) (2026-08-28)

### New Patches
* **Twitter:** NewX: Disable video player scrolling

### Commits
* [`229b738`](https://github.com/crimera/piko/commit/229b738ca4152b826765d18f4676c0d4e58748fd) feat(newx): add video player scroll toggle

# [12.19.1-release.0-b1f727c](https://github.com/crimera/piko-newx/releases/tag/12.19.1-release.0-b1f727c) (2026-08-27)

### New Patches
* **Twitter:** NewX: Remove ads
* **Twitter:** NewX: Browse tweet object
* **Twitter:** NewX: Open canonical URLs
* **Twitter:** NewX: Custom font
* **Twitter:** NewX: Custom sharing domain
* **Twitter:** NewX: Customize drawer items
* **Twitter:** NewX: Dynamic color
* **Twitter:** NewX: Feature switch overrides
* **Twitter:** NewX: Customize inline actions
* **Twitter:** NewX: Inline download button
* **Twitter:** NewX: Force highest video/audio quality
* **Twitter:** NewX: Customize default media tab
* **Twitter:** NewX: Customize navigation bar items
* **Twitter:** NewX: Customize default reply sorting
* **Twitter:** NewX: Share post as image
* **Twitter:** NewX: Hide premium upsell
* **Twitter:** NewX: Unlock downloads
* **Twitter:** NewX: Disable automatic timeline refresh
* **Twitter:** NewX: Filter For You by topic
* **Twitter:** NewX: Hide AI-generated posts
* **Twitter:** NewX: Hide Discover more
* **Twitter:** NewX: Hide compose button
* **Twitter:** NewX: Hide new posts pill
* **Twitter:** NewX: Hide Spaces bar
* **Twitter:** NewX: Hide who to follow
* **Twitter:** NewX: Restore timeline position
* **Twitter:** NewX: Show sensitive media
* **Twitter:** NewX: Filter posts by keyword

### Commits
* [`20d89d3`](https://github.com/crimera/piko/commit/20d89d310a2ad7f8afba1b5b98437c40b0159b48) fix(newx): make force highest video quality resilient across 12.17-12.19 and fix VerifyError
* [`d094d4e`](https://github.com/crimera/piko/commit/d094d4e372d02ad942fd401a8415973dea31171e) feat(newx): update checkbox element to match Twitter circular style with dynamic tint
* [`b1f727c`](https://github.com/crimera/piko/commit/b1f727c4f47cd15f8fe23ae6c9c7e5417ae48c66) fix(newx): route video downloads to Movies directory for MediaStore compliance

# [12.19.1-release.0-56f2321](https://github.com/crimera/piko-newx/releases/tag/12.19.1-release.0-56f2321) (2026-08-26)

### Commits
* [`8f55018`](https://github.com/crimera/piko/commit/8f55018a812f34519d5ae93da6d7039d9c505292) feat(newx): add BottomSheetView component and update media picker dialog
* [`0cf7122`](https://github.com/crimera/piko/commit/0cf71227da21742ed990781bb3b6ae56cad2d3b3) fix(newx): resolve original screen name for credited media in inline downloads
* [`df606e4`](https://github.com/crimera/piko/commit/df606e42ad860964969d565dfc01705ca92648d7) fix(newx): support registers >= v16 in injectReadWithDefault
* [`56f2321`](https://github.com/crimera/piko/commit/56f2321326e3d5e5241c24977028d1e34bc71dc8) feat(newx): add patch to force highest video and audio quality

# [12.18.0-beta.0-e8e5496](https://github.com/crimera/piko-newx/releases/tag/12.18.0-beta.0-e8e5496) (2026-08-26)

### Commits
* [`247cdfd`](https://github.com/crimera/piko/commit/247cdfdf5da70f191c485c2b18b4cc1c58839370) fix(xlite): unbind Compose reply sort UI state from unstable package
* [`47c58bd`](https://github.com/crimera/piko/commit/47c58bd5faaa7d86845356bfe5e99fcc589edf10) fix(xlite): dynamically resolve feature-switch repository for 12.19.0 compatibility
* [`bbb3529`](https://github.com/crimera/piko/commit/bbb35297136e60a026458b31943371ad6c781c59) fix(xlite): adapt canonical URLs card navigation for 12.19.0 while preserving 12.18 compatibility
* [`e34ab0e`](https://github.com/crimera/piko/commit/e34ab0e9ee45feae6966c710e0a9af2be1000af5) feat(xlite): open canonical URLs for profile website links
* [`e8e5496`](https://github.com/crimera/piko/commit/e8e5496a27281305f8f538a5d78a8a2e594c7ecc) fix(xlite): strip leading reply mentions from post keyword filter

