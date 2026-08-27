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

