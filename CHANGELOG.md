## [3.49.0](https://github.com/crimera/piko-newx/compare/v3.48.0...v3.49.0) (2026-10-03)

### 🐛 Bug Fixes
* **Twitter - newx:** label the For You topic button for what it keeps, not snoozes ([34e7f19](https://github.com/crimera/piko/commit/34e7f198320b500b1a3f8a053cc9a3b79e267c63))
* **Twitter - newx:** don't save timeline positions before the timeline loads ([39fb543](https://github.com/crimera/piko/commit/39fb543865e8f5f12ec22ce434474ce0bdef3762))

### ✨ New Features
* **Twitter - newx:** reopen the last pinned home tab on startup ([0503633](https://github.com/crimera/piko/commit/050363383ff2a4698cc535b2106f3af60870e9f9))
* **Twitter - newx:** restore list, topic and community timeline positions ([834e0d5](https://github.com/crimera/piko/commit/834e0d592175f3202429b0091f04559c9a536503))

### 🔧 Improvements
* **Twitter:** use the shared Utils and AddResourcesPatch from piko-patches-library ([3c8f15a](https://github.com/crimera/piko/commit/3c8f15ae4a9df800628afacd500f9358a098c27d))
* **Twitter - newx:** move the settings registry, screens and widgets into the shared libraries ([025ded0](https://github.com/crimera/piko/commit/025ded0013a4aa625241e6305664a31e30867eda))
* **Twitter - newx:** move server error logging into the shared extension library ([cfe591d](https://github.com/crimera/piko/commit/cfe591d28b2c7cc65ac6f38ccdae826b75497ee3))

### New Patches
* **Twitter:** NewX: Restore pinned home tab

## [3.48.0](https://github.com/crimera/piko-newx/compare/v3.47.0...v3.48.0) (2026-10-02)

### 🐛 Bug Fixes
* **Twitter - newx:** theme inline action counts that the host overrides with white ([dfb54a2](https://github.com/crimera/piko/commit/dfb54a2ca9b8b8fb40cc63def93a180ccb3cb771))

### ✨ New Features
* **Twitter - newx:** give Piko settings rows their own icon ([5ef312b](https://github.com/crimera/piko/commit/5ef312b108e1bd4e0c7ef1090cd49fcdc542a555))

### 🔧 Improvements
* **Twitter - newx:** Scan classes in parallel for whole-APK discovery ([dd61dbd](https://github.com/crimera/piko/commit/dd61dbdc5ed41284a708da8799af9ed88a47e92e))

## [3.47.0](https://github.com/crimera/piko-newx/compare/v3.46.0...v3.47.0) (2026-10-01)

### 🐛 Bug Fixes
* **Twitter - newx:** resolve immersive reply bar renderer on 12.31.0-alpha.04 ([af06413](https://github.com/crimera/piko/commit/af064137c93ce4655e77da436c8f107cc1e3d903))

### ✨ New Features
* **Twitter - newx:** declare 12.31.0-alpha.04 as an experimental target ([9eed2e7](https://github.com/crimera/piko/commit/9eed2e7b5c1f6a5cd8aa39117bd9cf6d76a26f6c))

## [3.46.0](https://github.com/crimera/piko-newx/compare/v3.45.0...v3.46.0) (2026-10-01)

### 🐛 Bug Fixes
* **Twitter - newx:** support 12.31.0-alpha.04 renderer shapes ([20b28a6](https://github.com/crimera/piko/commit/20b28a6607a53a3472563b19766774565fea7007))
* **Twitter - newx:** fail closed on duplicate branding color entries ([6c893c6](https://github.com/crimera/piko/commit/6c893c6a3f6638273788dd1c142343158b2757e8))
* **Twitter - newx:** theme XDS text colors so nested quotes follow Material You ([63ecf14](https://github.com/crimera/piko/commit/63ecf14d8f7af9cf8f308190bd0521d9e51ce47a))
* **Twitter - newx:** number native downloads of multi-media posts ([64ec8a2](https://github.com/crimera/piko/commit/64ec8a267ce421abb2014e9c614658be13eec1c4))
* **Twitter - newx:** keep Twitter branding colors on versions that dropped them ([69ee5fd](https://github.com/crimera/piko/commit/69ee5fd8098bb985de2aa942385deff1142e296d))
* **Twitter - Instagram:** Validate the picked file before restoring settings (#1985) ([1f1f3f7](https://github.com/crimera/piko/commit/1f1f3f7d25ca1159823c55580194c62b1af882ea))
* **Twitter - Instagram:** Refine Focus Lock highlight and slider spacing (#1982) ([c5b8ca5](https://github.com/crimera/piko/commit/c5b8ca5855b04706d86b20de89752780c36a7aa6))
* **Twitter - Instagram:** invoke reflected methods on the correct receiver (#1960) ([e4a9464](https://github.com/crimera/piko/commit/e4a9464792f8990a003a9289fe75243f6a54fa48))
* **Twitter - Instagram:** add auto-scroll persistence flag to recommended flags (#1957) ([096ea87](https://github.com/crimera/piko/commit/096ea8738d2edae3bf1d47aa8404822e6d4ccc5d))
* **Twitter - Instagram:** remove forced HDR brightness on photos and Reels (#1955) ([0084136](https://github.com/crimera/piko/commit/0084136b5ded2210e03d14dceabb09013be1cb3a))
* **Twitter - ci:** Import Crowdin translations onto the latest dev (#1890) ([385a8d1](https://github.com/crimera/piko/commit/385a8d1852434f0529d4a017f723ccc5cae4e0b8))
* **Twitter:** Preserve links when applying custom fonts (#1889) ([f5d1db8](https://github.com/crimera/piko/commit/f5d1db88cb2e1782436604168903347b43d3743c))
* **Twitter - Instagram:** Keep settings switch animations consistent after shortcut launch (#1883) ([6ffb046](https://github.com/crimera/piko/commit/6ffb046f68cf0d82c36d9c9837d695d259838331))
* **Twitter - Instagram:** Preserve the startup tab while editing navigation (#1880) ([cb1241f](https://github.com/crimera/piko/commit/cb1241f236801e8b5d58722e7db0b6d12680d08d))
* **Twitter - Instagram:** Skip event dispatch when analytics are disabled (#1877) ([7a44c6d](https://github.com/crimera/piko/commit/7a44c6d8306a1c2ca32502b3497308af8e1677b0))
* **Twitter - Instagram:** Sync ghost mode icons when settings change (#1875) ([dc12da8](https://github.com/crimera/piko/commit/dc12da8f03703fb6fa50ce11d009e32754c0761b))
* **Twitter - Instagram:** Preserve unobserved theme state (#1872) ([cf7cd66](https://github.com/crimera/piko/commit/cf7cd668dfe554a3a2de016524c88f92e7fb6303))
* **Twitter:** avoid copying editor spans in custom font hook ([c6deb8d](https://github.com/crimera/piko/commit/c6deb8daa5cd1f41a3a368802cf87c6f5dbf2749))
* **Twitter:** Error message is shown with changelog dialog ([e1238c3](https://github.com/crimera/piko/commit/e1238c3ffd38b1573a11a411000080f825f79583))
* **Twitter:** Restore timeline position on startup ([ae231c5](https://github.com/crimera/piko/commit/ae231c596bf9b7d3b1f2a1cff9ef5e74151cd6b9))
* **Twitter:** restore relationship actions in user lists ([854f5e2](https://github.com/crimera/piko/commit/854f5e26831c997e376a7b68094a7fbde89fc790))
* **Twitter - Instagram:** Add missing entity dependencies (#1833) ([a19b255](https://github.com/crimera/piko/commit/a19b255eccd3b2fed5474bc481ab7f3ae6640be9))
* **Twitter:** Revert "fix(twitter - `Bring Back Twitter`): support to new versions" ([df9b407](https://github.com/crimera/piko/commit/df9b4079d33aea17dcda5e4ebacd7bc4307421b9))
* **Twitter - github:** use existing enhancement label and add missing twitter label ([6337845](https://github.com/crimera/piko/commit/63378453c020ce89f490e802356418816be6820a))
* **Twitter:** support to new versions ([ff97563](https://github.com/crimera/piko/commit/ff975634c0e30b87fbb06cdcae556ff00f351a7a))
* **Twitter:** guard null ShareTarget in modern share sheet link hook ([5066035](https://github.com/crimera/piko/commit/5066035bc43b7c27f7e13248f0edec5afa7be85a))
* **Twitter - Instagram:** Recover settings after crash (#1822) ([8391a5b](https://github.com/crimera/piko/commit/8391a5b6817289307eb2fef96837c2055eebea99))
* **Twitter - Instagram:** Prevent newlines in text preferences (#1811) ([2cb1faa](https://github.com/crimera/piko/commit/2cb1faa3e18a7e99a5271957803cc5e6c278692e))
* **Twitter:** Don't rely on obfuscated names in `Show sensitive media` fingerprint ([d70c4d0](https://github.com/crimera/piko/commit/d70c4d008402547055a03777664702e65f2c18eb))
* **Twitter:** Fix `Show sensitive media` on the Compose timeline ([aeeb178](https://github.com/crimera/piko/commit/aeeb178390a8a52ecec1897dd278b6ac38f8f371))
* **Twitter - instagram:** add dialog entity dependency for media downloads ([5987d0b](https://github.com/crimera/piko/commit/5987d0be5704abdf1da15a8609924aa8a1118dbb))
* **Twitter - Bring back Twitter:** restore omitted Twitter 9.98 terminology ([a435e35](https://github.com/crimera/piko/commit/a435e35f9bb5008b39d2f9e2a08bd2c27450913f))
* **Twitter - resources:** support plural overrides for bundled resources ([3acd3aa](https://github.com/crimera/piko/commit/3acd3aa4f7326e606f0bd81e978b735ef0fdc9e9))
* **Twitter:** rewrite repost share links with original author ([11e7222](https://github.com/crimera/piko/commit/11e72222b5b6a974535991e34cf0e9daefb2b537))
* **Twitter - instagram:** preserve material you surface contrast ([0c1fff3](https://github.com/crimera/piko/commit/0c1fff3f8510cfa818e237bf36f74a7ac35a0080))
* **Twitter - Instagram:** follow app theme in deleted messages screen ([36b21b2](https://github.com/crimera/piko/commit/36b21b28d5f5ff5aad85a7329b39d50e7f490375))
* **Twitter:** `Block redirecting to X Lite` patch failed on X 12.6.0-release.0 ([01d4452](https://github.com/crimera/piko/commit/01d445211b68f43cd4dd56f962854f3df20d1f5e))
* **Twitter:** Add `Block update screen` patch ([9f257f7](https://github.com/crimera/piko/commit/9f257f71f927d03b09c1dd1212ccd74d1e5d8413))
* **Twitter - Instagram:** don't record an unsend we never captured (#1728) ([e38bc52](https://github.com/crimera/piko/commit/e38bc52c246992cb5ada60c826b27a2d89163e52))
* **Twitter:** Fix `Show sensitive media` patch (#1723) ([84919ef](https://github.com/crimera/piko/commit/84919ef416924643ec75c6834cb867ec1506a8bc))
* **Twitter - Instagram:** preserve pill button contrast (#1722) ([8e08ffc](https://github.com/crimera/piko/commit/8e08ffcccc675f8f995fe950e71091c9a46eca9b))
* **Twitter - Instagram:** use xml mime type for settings export (#1720) ([accfdc8](https://github.com/crimera/piko/commit/accfdc8066862cc8a80cf022cf8463d951fd9b27))
* **Twitter - Instagram:** Fix more profile options (#1708) ([ebf8ff1](https://github.com/crimera/piko/commit/ebf8ff1d9031c7e3a974a646d8dc4fde4419e1e8))
* **Twitter - Instagram:** Correct shared link sanitization (#1698) ([cbb5577](https://github.com/crimera/piko/commit/cbb55775f3448e0d50322ebde636bfbf4e8db2fd))
* **Twitter - Instagram:** block permission onboarding screens (#1686) ([de6bcea](https://github.com/crimera/piko/commit/de6bceaa0ceace832a63f8c116c8efc562a5c488))
* **Twitter - Instagram:** preserve reels media control colors (#1681) ([3befb48](https://github.com/crimera/piko/commit/3befb4800a92a2a3046b394a4e6c230083fc8bb2))
* **Twitter - instagram:** restore amoled after dark mode returns (#1679) ([96536bb](https://github.com/crimera/piko/commit/96536bbf24544219e0bd279ed6bba357e2b3da28))
* **Twitter - Instagram:** Prevent notification registration crash (#1678) ([4f67a78](https://github.com/crimera/piko/commit/4f67a78430871afa0eff393d9127f78fd11a85e0))
* **Twitter - Instagram:** handle missing context for comment media downloads (#1677) ([4588900](https://github.com/crimera/piko/commit/45889000685d29e07bdf223050ebaa0eadc38eb2))
* **Twitter - Instagram:** Fix default flag state while extracting recommended flags map ([82785a8](https://github.com/crimera/piko/commit/82785a858bae02ee11bd8ff07f06fa260bcceea2))

### ✨ New Features
* **Twitter - newx:** register the logging toggle as a built-in setting ([ccc8138](https://github.com/crimera/piko/commit/ccc8138aec47ed2fcb8ebdcb74d833942673d793))
* **Twitter - Instagram:** add custom font support (#1920) ([065bb95](https://github.com/crimera/piko/commit/065bb95ad626b05c1d11e7ba64698e4e313ce81b))
* **Twitter - Instagram:** Show non-followers in the Following list (#1978) ([f2395c9](https://github.com/crimera/piko/commit/f2395c9c84ccc989771701d6b27bd556c949274c))
* **Twitter - Instagram:** Lock any distraction free setting with Focus Lock (#1953) ([97ea429](https://github.com/crimera/piko/commit/97ea42941f25a68e8fd1080852a576b0b80cd134))
* **Twitter - Instagram:** Add `Focus Lock` patch (#1928) ([2b6b5ac](https://github.com/crimera/piko/commit/2b6b5ac21cb199f40a4e6dfc0dc76c36992fe31f))
* **Twitter - Instagram:** Customize download filenames (#1923) ([8507022](https://github.com/crimera/piko/commit/850702242069fab700d6382ec4287d95f4e1f722))
* **Twitter - Instagram:** Hide Reels follow button (#1911) ([f180a7b](https://github.com/crimera/piko/commit/f180a7b4c628f1f23d9e78fc8ed3715e652b0a03))
* **Twitter - Instagram:** Restore classic search recents (up to 25) (#1741) ([bb98bcb](https://github.com/crimera/piko/commit/bb98bcb219ca0a30ee672db4361dc70abbfe06df))
* **Twitter - Instagram:** Update the Direct icon in settings and in the navigation customization window. (#1888) ([7e50716](https://github.com/crimera/piko/commit/7e507162e87e8ac586216fa7562add6bac355d28))
* **Twitter - Instagram:** Add story seen button (#1884) ([c39e122](https://github.com/crimera/piko/commit/c39e122dbce23d9d603bc73010e0aeaccdfe88bd))
* **Twitter - Instagram:** Add visibility controls for create and notification buttons (#1870) ([a1c0866](https://github.com/crimera/piko/commit/a1c0866824ef72cd40b5d03d3ec2a46bf5f8cdaf))
* **Twitter - Instagram:** Add startup tab selection (#1869) ([d284f62](https://github.com/crimera/piko/commit/d284f629056344bec9351fe86afd73f07ef25818))
* **Twitter - Instagram:** Customize navigation bar (#1867) ([bbd335c](https://github.com/crimera/piko/commit/bbd335ca7764ec99c3c9936e0ffd71723699e627))
* **Twitter:** Add bulk feature flag selection and validation (#1846) ([7b92ac8](https://github.com/crimera/piko/commit/7b92ac8626b2ff907769503ae85b688fd2471c36))
* **Twitter - Instagram:** Embed metadata in downloaded videos (#1828) ([9493252](https://github.com/crimera/piko/commit/949325266af15c51477101be81ad8692bb439557))
* **Twitter - Instagram:** Integrate `Disable onboarding permission prompts` patch into `Disable analytics` (#1771) ([a7974cd](https://github.com/crimera/piko/commit/a7974cd4c66dff557c2905ea92ad73741b46fa44))
* **Twitter - Instagram:** save deleted messages (#1531) ([6c120d6](https://github.com/crimera/piko/commit/6c120d603cb830c0ccc8c4a99acc9eab089f70bd))
* **Twitter - Instagram:** Add custom sharing domain (#1712) ([879f269](https://github.com/crimera/piko/commit/879f269cc6f3e69e489b6b574961da9c9d2096b2))
* **Twitter - Instagram:** Add in-app profile picture viewer (#1721) ([7d34500](https://github.com/crimera/piko/commit/7d34500c7553ed8baf61816ab0bf6ad0ca7f18d8))
* **Twitter - Instagram:** Add loop story (#1713) ([4b75ec7](https://github.com/crimera/piko/commit/4b75ec78428836bb5fd8bedf65a34f52f42a7315))
* **Twitter - Instagram:** Made `Recommended flags` into patch ([f81fc79](https://github.com/crimera/piko/commit/f81fc7992792a72ecfc7d006590db9a506c86caa))

### 🚀 Updated App Support
* **Twitter:** Add HotYuriSex into unofficial instances for deeplinks ([a82c8cc](https://github.com/crimera/piko/commit/a82c8cc364737a4fd9edfa87da8be231a4ef59ac))
* **Twitter:** bump support to `12.19.1-release.0` ([4350e4d](https://github.com/crimera/piko/commit/4350e4d8c073c59f79535f8e3fc63dbeb0d21b81))
* **Twitter:** bump support to `12.17.0-release.0` ([9d08cd3](https://github.com/crimera/piko/commit/9d08cd33d4bdba67cd86d441747a8e3300522aa2))
* **Twitter - Instagram:** improve piko settings handling (#1671) ([15d8d2e](https://github.com/crimera/piko/commit/15d8d2ef015d6548f778006d87ead5ae93663080))
* **Twitter:** Dynamic color (#1652) ([dce8132](https://github.com/crimera/piko/commit/dce813262b9a49f96e952c9bc56fb1f9a05e89b2))

### 🔧 Improvements
* **Twitter - newx:** Cut patch resolution time with narrower lookups ([81685f4](https://github.com/crimera/piko/commit/81685f48df34962448e638bfd9ed749b3b42ffb5))
* **Twitter - Instagram:** Cache track data mappings per TrackDataIntf instance (#1970) ([0cc09e0](https://github.com/crimera/piko/commit/0cc09e09799b506375f04aee66b0c53112f518a0))
* **Twitter:** Use a Set for the feature-flag search-string membership check (#1974) ([6622be4](https://github.com/crimera/piko/commit/6622be4d5c7b3634e09c0f569259d69c72cabdfe))
* **Twitter - Instagram:** Cache extended media data lookups per MediaData instance (#1967) ([b2800b7](https://github.com/crimera/piko/commit/b2800b7adb96b93bada54e745342d9a4add27c17))
* **Twitter - Instagram:** Cache the resolved helper class in DeveloperOptionsItem (#1973) ([e252d0b](https://github.com/crimera/piko/commit/e252d0b3e24f5a75edd21d7d242f13422cfde01a))
* **Twitter - Instagram:** Use a HashSet instead of a List for the feed JSON key filter (#1972) ([daf0a63](https://github.com/crimera/piko/commit/daf0a63f3176a3272aeb846257f295cc233e6850))
* **Twitter - Instagram:** Skip redundant fill-in updates for freshly inserted messages (#1971) ([1bcc99d](https://github.com/crimera/piko/commit/1bcc99d57f7bccd61187666a745bfd4804ef7a09))
* **Twitter - Instagram:** Cache resolved classes in DirectItem instead of calling Class.forName repeatedly (#1969) ([e91f754](https://github.com/crimera/piko/commit/e91f7540724d8c9f9d5bef50cff9ede582c7fb85))
* **Twitter - Instagram:** Cache reflective Field/Method lookups in Entity (#1966) ([5fdc28f](https://github.com/crimera/piko/commit/5fdc28fbaa731f66bc5aaa93133c27a1b1b16796))
* **Twitter - Instagram:** Strip stkn tracking parameter from share links (#1848) ([8340015](https://github.com/crimera/piko/commit/834001582f810033267b307d75b3737eedf3981b))
* **Twitter:** restore legacy follower lists ([6dbe113](https://github.com/crimera/piko/commit/6dbe113c8b7fbcb2daa23d409754029cc9429a69))
* **Twitter:** use stable relationship fingerprints ([6e7aa4a](https://github.com/crimera/piko/commit/6e7aa4ab1fdebe6594fc805ae544f5e4bf8a2a19))
* **Twitter:** inline share link rewriting ([c63d4a0](https://github.com/crimera/piko/commit/c63d4a04390a74c6842659bb09702801427d636e))
* **Twitter - Instagram:** share applySystemBarStyle via InstagramPreferenceStyle ([70cd23c](https://github.com/crimera/piko/commit/70cd23caf31114db8d484fa7c6ce5b4bc95d799a))
* **Twitter - Instagram:** refine friendship indicator styling ([94bed37](https://github.com/crimera/piko/commit/94bed3777b6e67e5decafde3cea9643534337420))
* **Twitter:** Refactor Media resolution fingerprint to support 12.17.xx ([ce77559](https://github.com/crimera/piko/commit/ce77559b3b54918891d4def0c1a46bfb20c1c848))
* **Twitter:** More profile info Id structure ([6c7e10c](https://github.com/crimera/piko/commit/6c7e10c9ed69e9bf6e2cdcb69c8a91e7b7b7f67f))
* **Twitter:** Customise native share menu items ([6e1896d](https://github.com/crimera/piko/commit/6e1896d72a65b8060f613e74f7d35117157efd05))
* **Twitter - Instagram:** rebind settings category icons (#1707) ([3ca930e](https://github.com/crimera/piko/commit/3ca930e9d84a85f737c8f56e9e870b688f225ebb))
* **Twitter - Instagram:** colorize FriendshipStatusIndicator text and improve pill contrast/spacing (#1702) ([6c8182c](https://github.com/crimera/piko/commit/6c8182cbc8ec1188a627a198f932b09cddbf4540))
* **Twitter - Instagram:** Restyle friendship status indicator (#1690) ([6a06d7d](https://github.com/crimera/piko/commit/6a06d7dac9c1f277508e56a106ee786f810e66e5))
* **Twitter:** improve more profile info (#1687) ([46cb754](https://github.com/crimera/piko/commit/46cb754e48b66606f19804b610cd085d54f5d173))
* **Twitter - Instagram:** refresh recommended flags after download (#1685) ([85057c0](https://github.com/crimera/piko/commit/85057c09a76f2efbd481f0ffb6454c40d067cfb7))
* **Twitter - Instagram:** Improve piko settings (#1684) ([17662c3](https://github.com/crimera/piko/commit/17662c3d311a093b4f35545db5ba73d4c8547a6d))
* **Twitter - Instagram:** Change default state of recommended flags ([ae0d9cc](https://github.com/crimera/piko/commit/ae0d9cc2686cbaf794d78adc9c8b95f4924b83e4))
* **Twitter - Instagram:** Turn off `Disable analytics` by default (#1674) ([753a70b](https://github.com/crimera/piko/commit/753a70be81449c27f0a8e056f7f0e938a11e964e))
* **Twitter - Instagram:** Include Recommended flags in about patch section ([422926a](https://github.com/crimera/piko/commit/422926a4a54780e87cd708b1e32a37442e40082e))
* **Twitter:** Check change domain patch before applying ([5a77198](https://github.com/crimera/piko/commit/5a7719819ea4b76f6f30645dd8f7b3098ed93a26))
* **Twitter - Instagram:** Move theme controls to piko settings (#1661) ([803d62d](https://github.com/crimera/piko/commit/803d62dffa94da973e672bf24c27e957a39ebf7d))
* **Twitter - Instagram:** Make recommended flags as list rather than switch ([3e15ee4](https://github.com/crimera/piko/commit/3e15ee4d7f518c1220bf10e1539bb415e594635a))
* **Twitter - Instagram:** Make download function accept runnable ([998ad02](https://github.com/crimera/piko/commit/998ad02c5efdacdf5bbb3f2b6095af3d9f7a3c94))
* **Twitter:** If the setting is off, don't apply flags ([4836298](https://github.com/crimera/piko/commit/4836298fbe321112a206b7b590a1783dd530dc76))

## [3.45.0](https://github.com/crimera/piko-newx/compare/v3.44.0...v3.45.0) (2026-09-30)

### 🐛 Bug Fixes
* **Twitter - newx:** accept one or two video-tab download handlers ([b827ff3](https://github.com/crimera/piko/commit/b827ff3edc9f4b7b665106d0be6eac6c59f8bacc))
* **Twitter - newx:** capture fingerprint shapes instead of hidden patcher fields ([95a259e](https://github.com/crimera/piko/commit/95a259e85ad920771de389979bb97623f4171300))

### ✨ New Features
* **Twitter:** add experimental support for 12.31.0-alpha.02 ([ef85b31](https://github.com/crimera/piko/commit/ef85b31db37bee06e8b912a9a5429111208a4691))
* **Twitter - newx:** customize media long-press menu items ([5e32171](https://github.com/crimera/piko/commit/5e3217147c7ed96bdbaa0ca62dcd46d8fc81b56a))

### New Patches
* **Twitter:** NewX: Customize media menu items

## [3.44.0](https://github.com/crimera/piko-newx/compare/v3.43.0...v3.44.0) (2026-09-29)

### 🐛 Bug Fixes
* **Twitter - newx:** hook the home-nav header state for hide premium upsell ([5505646](https://github.com/crimera/piko/commit/55056469426971b9d8307393733c93bdb680c664))
* **Twitter - newx:** cast the Coil strong-cache wrapper before its map read ([a6159e3](https://github.com/crimera/piko/commit/a6159e30d1ea9768da35d4b2174832094d85b266))
* **Twitter - newx:** read Coil's strong-cache map on the 12.30 merge ([9a9f8c0](https://github.com/crimera/piko/commit/9a9f8c0930b65a2486b27497c6cf9e7bef7fa37a))

### ✨ New Features
* **Twitter - newx:** report thumbnail cache lookup stage and sample keys ([b081e5b](https://github.com/crimera/piko/commit/b081e5b7d27aa1a88a4e2833821be25be208b043))

## [3.43.0](https://github.com/crimera/piko-newx/compare/v3.42.2...v3.43.0) (2026-09-29)

### 🐛 Bug Fixes
* **Twitter - newx:** fingerprint reply facepile lists by parameter provenance ([d3eef3e](https://github.com/crimera/piko/commit/d3eef3edfd9df557b208dbe664fc80b952ca72ce))
* **Twitter - newx:** resolve the widened Glide LRU map field on 12.30 ([03fec1f](https://github.com/crimera/piko/commit/03fec1fc3fc5cdc47315ee9fef7e41a4683531ad))

### ✨ New Features
* **Twitter - newx:** redirect native download buttons to the chosen folder ([d4f1cc7](https://github.com/crimera/piko/commit/d4f1cc75301e531412e5a8789cc13cb516ffd0a1))

### 🔧 Improvements
* **Twitter - newx:** clear resolver anchor backlog and gate the drift rules ([b30b72c](https://github.com/crimera/piko/commit/b30b72cce71ba8f502a9369a01cf2010e2e5cf8b))

### New Patches
* **Twitter:** NewX: Redirect downloads to chosen folder

## [3.42.2](https://github.com/crimera/piko-newx/compare/v3.42.1...v3.42.2) (2026-09-28)

### 🐛 Bug Fixes
* **Twitter - newx:** hide dividers at the shared timeline divider helper ([a3939be](https://github.com/crimera/piko/commit/a3939be95cd27dd9cf72e25afea32285bd7e80ac))
* **Twitter - newx:** match the 12.30 share-image renderer semantically ([2aa5a44](https://github.com/crimera/piko/commit/2aa5a447d76e69a5b6a407c3b9037c8c72c52fa2))
* **Twitter - newx:** follow the reply sorting prefetch seed through object moves ([65a9192](https://github.com/crimera/piko/commit/65a91920bbb1ff0dca5199d5b87c059cdc9ec458))
* **Twitter - newx:** resolve the inlined card URL source on 12.30 ([568b29b](https://github.com/crimera/piko/commit/568b29b2728b27b4843ac0f076fb10c4bcd14944))
* **Twitter - newx:** accept the 12.30 post divider renderer shape ([1335f72](https://github.com/crimera/piko/commit/1335f72a0063703a52707c9f7959d91682550843))
* **Twitter - newx:** resolve the relocated Coil strong cache on 12.30 ([233e858](https://github.com/crimera/piko/commit/233e85804e498ac17f3d7e2153727859caa61d7c))
* **Twitter - newx:** hook the Haze 2.x blur scope recorder on 12.30 ([c0cce3d](https://github.com/crimera/piko/commit/c0cce3d92076fcda08840c62f65d94979d2989cc))
* **Twitter - newx:** survive R8 lambda merging in the navbar content resolver ([3760fd2](https://github.com/crimera/piko/commit/3760fd2094d2ae0080dde49af90e3ab863de6334))
* **Twitter:** navbar customization support for 12.30 alpha 5 ([adfd723](https://github.com/crimera/piko/commit/adfd723a2f1c446cfc0ed5c22d4206942e176fbd))
* **Twitter - newx:** render feature switch list values without Stream.toList ([06e6dd3](https://github.com/crimera/piko/commit/06e6dd323a4e41de1b1c34cbd147ef3fa2796203))

## [3.42.1](https://github.com/crimera/piko-newx/compare/v3.42.0...v3.42.1) (2026-09-28)

### 🐛 Bug Fixes
* **Twitter - newx:** cancel the progress notice when download failures can't notify ([5ea8704](https://github.com/crimera/piko/commit/5ea8704c69614c81a03a8bff68723fba4663bcde))
* **Twitter - newx:** post terminal download notices on a fresh notification id ([64782ba](https://github.com/crimera/piko/commit/64782bae74b34d54ecf24017abf75b566d4a75c3))

## [3.42.0](https://github.com/crimera/piko-newx/compare/v3.41.0...v3.42.0) (2026-09-27)

### 🐛 Bug Fixes
* **Twitter:** flap-riding retries, cancel/share actions, no-connection state ([5cca3fe](https://github.com/crimera/piko/commit/5cca3fef3040e82850805d6343e7f52216279b5f))
* **Twitter:** retry button on failure, stall-tolerant large transfers ([4eeb18b](https://github.com/crimera/piko/commit/4eeb18b6f0311f77533a0d2e8da7fe65bce2a03f))

### ✨ New Features
* **Twitter - newx:** disable themed like button by default ([7750b85](https://github.com/crimera/piko/commit/7750b85af26e530890a7f8af5fbc097e464e7573))
* **Twitter - newx:** add Default theme option with original NewX colors ([0d56c65](https://github.com/crimera/piko/commit/0d56c65a87330e3246c2def3edfd972ec3485349))
* **Twitter - newx:** replace dynamic toggle with Material You/high-contrast/Dim theme chooser ([3967dc1](https://github.com/crimera/piko/commit/3967dc14396943324a4757b96940f3793e557bc5))

## [3.41.0](https://github.com/crimera/piko-newx/compare/v3.40.1...v3.41.0) (2026-09-26)

### ✨ New Features
* **Twitter - newx:** mark and sort newly observed feature switches ([8ac80ff](https://github.com/crimera/piko/commit/8ac80ff7a2e56e84812ba3ecf691f8b8da210934))

## [3.40.1](https://github.com/crimera/piko-newx/compare/v3.40.0...v3.40.1) (2026-09-26)

### 🐛 Bug Fixes
* **Twitter - newx:** share-image captures detail main post instead of stale reply ([badfa75](https://github.com/crimera/piko/commit/badfa75c21b3184ce24a47e69d5acfb036267078))

## [3.40.0](https://github.com/crimera/piko-newx/compare/v3.39.0...v3.40.0) (2026-09-26)

### ✨ New Features
* **Twitter:** add experimental support for 12.29.1-prod.01 ([117b25f](https://github.com/crimera/piko/commit/117b25f803045ecbc100e010e9846979024b8fcf))

## [3.39.0](https://github.com/crimera/piko-newx/compare/v3.38.0...v3.39.0) (2026-09-26)

### 🐛 Bug Fixes
* **Twitter:** enable old inline actions spacing patch by default ([433b259](https://github.com/crimera/piko/commit/433b259e8dcb4542c5c1c7f2b176eea52c718d79))
* **Twitter:** narrow destination-loss detection, fix status toast and merge loss (#38) ([980fc80](https://github.com/crimera/piko/commit/980fc806b3424158471e4be2f5a6052b2df39ac1))
* **Twitter:** fix silent NewX download failures (#38) ([a1ad351](https://github.com/crimera/piko/commit/a1ad3511f90374b92b5afe3020c38bfd507d907b))

### ✨ New Features
* **Twitter - newx:** replace the AMOLED toggle with an amoled/dim dark style chooser ([36e227f](https://github.com/crimera/piko/commit/36e227f71ff11605586f32ca4f36278a3e193e30))

### 🔧 Improvements
* **Twitter - newx:** dedupe repeated dex traversals in slow patches ([4b6bbaa](https://github.com/crimera/piko/commit/4b6bbaa350188a95c7b1736513aba066c911b136))
* **Twitter - newx:** rename the Dynamic color patch to Theme ([e6121e9](https://github.com/crimera/piko/commit/e6121e9c19da2e713eb85097a71bbcc2e49ba58a))
* **Twitter - newx:** port the patch suite to the typed bytecode API ([1505dc6](https://github.com/crimera/piko/commit/1505dc67e32c23b4a3e7b2fd984eb1f5f6853125))

### New Patches
* **Twitter:** NewX: Theme

## [3.38.0](https://github.com/crimera/piko-newx/compare/v3.37.1...v3.38.0) (2026-09-25)

### 🐛 Bug Fixes
* **Twitter - newx:** skip inline-download IconOnly override on legacy boolean kind models ([e44507a](https://github.com/crimera/piko/commit/e44507aa6c203c9365342d81ee893601a2fb464e))
* **Twitter - newx:** inject default media-tab bridge at the 12.29 seed label ([24297e4](https://github.com/crimera/piko/commit/24297e403c902f2fdca1702d206027c0b36dcd6a))
* **Twitter:** 12.29 reply sorting fix ([5c4fe77](https://github.com/crimera/piko/commit/5c4fe773c35c42e1f8fb5f6fe754fcbb6dc70f49))
* **Twitter - newx:** give the injected inline download action the icon-only kind ([5e65767](https://github.com/crimera/piko/commit/5e6576793c536d3b6e4bbe5a99e31f3be3c7b12b))
* **Twitter - newx:** inset 12.29 immersive action row ([5bfd025](https://github.com/crimera/piko/commit/5bfd025085a44883a6c22ca16d6be9ea05c43475))
* **Twitter - newx:** keep the photo screen's gated gesture inset when hiding the reply bar ([a4c0293](https://github.com/crimera/piko/commit/a4c029398eafbe9fd93773a51eadd81ff2f2e36d))
* **Twitter:** select the nav spacer in the 12.29 immersive photo viewer ([b46d10d](https://github.com/crimera/piko/commit/b46d10dc10b8165f5c6d626f9d5f8ca49895b880))
* **Twitter:** keep navigation-bar field reads four-bit on high-register methods ([bd65565](https://github.com/crimera/piko/commit/bd65565f2a1e58d45e1f9da50b6950f8401827f2))
* **Twitter:** identify 12.29 media-tab sub-tab seed semantically ([29903b8](https://github.com/crimera/piko/commit/29903b8f1e6d42720807616ee2340a0bdf4dbfb9))
* **Twitter:** support 12.29 submit handler without POST_SUCCESS ([2c96f24](https://github.com/crimera/piko/commit/2c96f246d251a85478d28b43738689fe21bfa3f2))
* **Twitter:** resolve 12.29 profile-link canonical URL builder ([83e65a6](https://github.com/crimera/piko/commit/83e65a6ad8eeb784f227383bff7aa8161ccc706b))
* **Twitter:** resolve 12.29 hide post dividers null-key lowering ([c39f422](https://github.com/crimera/piko/commit/c39f4224364e896d31d3800aa0c18f9155614bd6))
* **Twitter:** resolve new-post renderer ABI variant for 12.29 ([3f95e24](https://github.com/crimera/piko/commit/3f95e2415086094160ec05b97d85955f736beafe))
* **Twitter:** anchor For You topic request on semantic filters for 12.29 ([d4880c3](https://github.com/crimera/piko/commit/d4880c32aa68aa89858f016d6cc38a70753f701b))
* **Twitter:** resolve VerticalPager owner-agnostically for 12.29 ([7c42e86](https://github.com/crimera/piko/commit/7c42e867a2b7da17f5a4ca2f955e7ee7fdcedc40))
* **Twitter:** port drawer and navigation bar resolvers to 12.29 ([7b489ae](https://github.com/crimera/piko/commit/7b489ae068ebfa6e3196388844e58ab157927df5))
* **Twitter - Custom Sharing Domain:** add support for 12.19 alpha 4 ([8fde3b9](https://github.com/crimera/piko/commit/8fde3b95939f1e15cb517ba6976317e9143c7a96))

### ✨ New Features
* **Twitter:** initial support for 12.29 alpha 4 ([f3b986e](https://github.com/crimera/piko/commit/f3b986eac4459e6f42b5bcb1e0b68e8d4a844348))
* **Twitter - newx:** add classic inline action bar spacing ([c9972f9](https://github.com/crimera/piko/commit/c9972f913caedadfa3100ef647dd8c6dce64d40a))

### New Patches
* **Twitter:** NewX: Classic inline action spacing

## [3.37.1](https://github.com/crimera/piko-newx/compare/v3.37.0...v3.37.1) (2026-09-24)

### 🐛 Bug Fixes
* **Twitter:** add media picker resolution chooser toggle ([40560ca](https://github.com/crimera/piko/commit/40560ca79b091a1c4a23b41c1b61983a26671a90))

## [3.37.0](https://github.com/crimera/piko-newx/compare/v3.36.0...v3.37.0) (2026-09-24)

### 🐛 Bug Fixes
* **Twitter:** keep extension surfaces black without the dynamic color patch ([4c7b8ff](https://github.com/crimera/piko/commit/4c7b8ffd2a683fdbdae901d666de254f8687084e))

### ✨ New Features
* **Twitter:** per-tab navigation bar badge toggles ([0e30ed4](https://github.com/crimera/piko/commit/0e30ed414f459dbbd3fb73227936d5db89662908))

## [3.36.0](https://github.com/crimera/piko-newx/compare/v3.35.0...v3.36.0) (2026-09-24)

### ✨ New Features
* **Twitter:** add hide add-tab toggle and group timeline tab options ([0195f5c](https://github.com/crimera/piko/commit/0195f5c0364eb2d4602ed2b41caa64e7ffc30ccf))

## [3.35.0](https://github.com/crimera/piko-newx/compare/v3.34.1...v3.35.0) (2026-09-23)

### ✨ New Features
* **Twitter:** add inline download resolution chooser and quality preferences ([dbade44](https://github.com/crimera/piko/commit/dbade44644d2fbb3490a6d79788f4c4455abc80c))

## [3.34.1](https://github.com/crimera/piko-newx/compare/v3.34.0...v3.34.1) (2026-09-23)

### 🐛 Bug Fixes
* **Twitter:** newx dim theme chrome backgrounds ([a6af4dc](https://github.com/crimera/piko/commit/a6af4dce4184cea0b5c646eacaa3f2e1f2973667))

## [3.34.0](https://github.com/crimera/piko-newx/compare/v3.33.1...v3.34.0) (2026-09-23)

### 🐛 Bug Fixes
* **Twitter - newx:** apply custom sharing domain on share-sheet URL field ([c7230d2](https://github.com/crimera/piko/commit/c7230d2d3c11bcbb2c20137a83bd1d29512bf0bd))
* **Twitter - newx:** resolve module divider lambda adapter by discriminator ([618c2af](https://github.com/crimera/piko/commit/618c2af3c2c98f036c783c6a591b1700dbd05d8a))
* **Twitter - newx:** use dim surfaces in extension-owned screens ([5fb32a5](https://github.com/crimera/piko/commit/5fb32a59bfe768cfe74707084f0a8486414ee4e5))

### ✨ New Features
* **Twitter - newx:** restore classic dim background when dynamic color and AMOLED are off ([097b782](https://github.com/crimera/piko/commit/097b7824c7481901f0bf6c140706d9a525918753))

## [3.33.1](https://github.com/crimera/piko-newx/compare/v3.33.0...v3.33.1) (2026-09-22)

### 🐛 Bug Fixes
* **Twitter - newx:** rename inline download template token to userName ([c0dd037](https://github.com/crimera/piko/commit/c0dd037aa96ce20b538b523d2af5baae58890e67))

## [3.33.0](https://github.com/crimera/piko-newx/compare/v3.32.0...v3.33.0) (2026-09-22)

### ✨ New Features
* **Twitter:** add support for 12.28.0-prod.01 ([f77d602](https://github.com/crimera/piko/commit/f77d6029120c16c298eb54cc001599de444c216a))

## [3.32.0](https://github.com/crimera/piko-newx/compare/v3.31.0...v3.32.0) (2026-09-22)

### 🐛 Bug Fixes
* **Twitter - newx:** resolve obfuscated Compose types in photos gallery ([61c0a87](https://github.com/crimera/piko/commit/61c0a876d67866ed5530de82580d3fcad37740e8))
* **Twitter - newx:** resolve bottom paginator StateFlow getValue dynamically ([2f284b1](https://github.com/crimera/piko/commit/2f284b194dead1375ac89f5ec1c95a21a52f897b))

### ✨ New Features
* **Twitter:** allow custom download folders ([9cc2c6f](https://github.com/crimera/piko/commit/9cc2c6f3865160c3722cee7d827123bc85662ed8))

## [3.31.0](https://github.com/crimera/piko-newx/compare/v3.30.4...v3.31.0) (2026-09-21)

### ✨ New Features
* **Twitter - newx:** long press inline download to download all media ([5888f3a](https://github.com/crimera/piko/commit/5888f3a40b4bad9318d2c3d0aa94755886f9116c))

## [3.30.4](https://github.com/crimera/piko-newx/compare/v3.30.3...v3.30.4) (2026-09-21)

### 🐛 Bug Fixes
* **Twitter:** paginate Photos gallery when first page underfills viewport ([66e2e1c](https://github.com/crimera/piko/commit/66e2e1c3dac43b52e197ac88c2d7878a7fd215ad))

## [3.30.3](https://github.com/crimera/piko-newx/compare/v3.30.2...v3.30.3) (2026-09-21)

### 🐛 Bug Fixes
* **Twitter - newx:** share-image field-walk parent resolution for B union ([1512f9f](https://github.com/crimera/piko/commit/1512f9f487ef84a4212bfa4ed524357d86699945))
* **Twitter - newx:** share-image explicit spatial c() rect + strong bounds map ([e47559f](https://github.com/crimera/piko/commit/e47559ffb72adb1b52a7f064f329807a178deb75))

## [3.30.2](https://github.com/crimera/piko-newx/compare/v3.30.1...v3.30.2) (2026-09-20)

### 🐛 Bug Fixes
* **Twitter:** Use generated ID for Photos gallery state ([cecd779](https://github.com/crimera/piko/commit/cecd779dc83d6bba444f2e0800e08c80652dac75))

## [3.30.1](https://github.com/crimera/piko-newx/compare/v3.30.0...v3.30.1) (2026-09-20)

### 🐛 Bug Fixes
* **Twitter:** Preserve Photos gallery scroll position ([2498fdf](https://github.com/crimera/piko/commit/2498fdfab06b6e61ef71e69080eb1c4e09f1dde3))
* **Twitter:** NewX Photos gallery pagination ([0a0ad6a](https://github.com/crimera/piko/commit/0a0ad6a88ccd0d278542e4dc7833ff2fcf3b296b))
* **Twitter:** open full viewer with post context from gallery taps ([1dcd2ff](https://github.com/crimera/piko/commit/1dcd2ff674cceef3082ddae38da8b8b1b1a2d2d3))
* **Twitter:** open full screen image in gallery view ([fe9c751](https://github.com/crimera/piko/commit/fe9c751721170a06fd7d11e1f3f34fe92453efd3))

## [3.30.0](https://github.com/crimera/piko-newx/compare/v3.29.1...v3.30.0) (2026-09-20)

### 🐛 Bug Fixes
* **Twitter:** shrink gallery loading spinner (32dp, 4dp stroke) ([3d3077a](https://github.com/crimera/piko/commit/3d3077ae9cfb76c843f66918f7b35f891f62f2ed))
* **Twitter:** custom sharing domain patch support for 12.28 alpha 4 ([d109ef7](https://github.com/crimera/piko/commit/d109ef768eb376dd44f8eec1a2a91eb568790b0f))
* **Twitter:** resolve reply bar renderer across test-tag relocation ([99a39dd](https://github.com/crimera/piko/commit/99a39ddca08d86e2380b5ed0f00c5787645704a2))
* **Twitter:** accept hoisted divider lambda in module divider matcher ([513d36b](https://github.com/crimera/piko/commit/513d36bc409bca8735c8de28b1082fd2457a6701))
* **Twitter:** derive gallery photo navigation from call graph ([61ad517](https://github.com/crimera/piko/commit/61ad5176fef904dc3f351bc34851e266d7d9a792))
* **Twitter:** match inline-action renderer semantically, resolve slots dynamically ([b1fe23a](https://github.com/crimera/piko/commit/b1fe23a9aab7393b62225abf08e4e7884c5b5b63))
* **Twitter:** reserve explicit registers for inline-actions setting read ([7772b6e](https://github.com/crimera/piko/commit/7772b6e0b59343a733e07a81e81222cf9d0da2d5))
* **Twitter:** add bounded gallery thumbnail cache with developer stats screen ([f7377af](https://github.com/crimera/piko/commit/f7377afe26c7ee605fdb7002f0959357d466919e))
* **Twitter:** route profile photo pagination to bottom paginator ([a5855d4](https://github.com/crimera/piko/commit/a5855d400454ec9e533ae3eba01afa3ad09cb2ad))

### ✨ New Features
* **Twitter:** experimental support for 12.28.0-alpha.04 ([8e97eae](https://github.com/crimera/piko/commit/8e97eae57a18d6865d61661fed71c1dd4a07d231))

## [3.29.1](https://github.com/crimera/piko-newx/compare/v3.29.0...v3.29.1) (2026-09-19)

### 🐛 Bug Fixes
* **Twitter:** drop legacy 12.25 targets ([e4a1e2e](https://github.com/crimera/piko/commit/e4a1e2e5026d73277b64b7a65d2d28dc04d69dad))

## [3.29.0](https://github.com/crimera/piko-newx/compare/v3.28.0...v3.29.0) (2026-09-19)

### 🐛 Bug Fixes
* **Twitter:** refactor NewX source identity resolution ([45b230e](https://github.com/crimera/piko/commit/45b230e18a686afd97c6b386077303a2d6bd161d))

### ✨ New Features
* **Twitter:** add profile photos gallery view ([9daf4a3](https://github.com/crimera/piko/commit/9daf4a31a8daf97c8105a5da2e8c1894740d0df6))
* **Twitter:** add more post menu hide options ([2c7c268](https://github.com/crimera/piko/commit/2c7c268aef36aaf0dd365339c137c804ca449e98))
* **Twitter - newx:** add dislike inline action toggle ([ae7cdd2](https://github.com/crimera/piko/commit/ae7cdd2c729e8c30d6dea584320f7efd20f5cb68))

### New Patches
* **Twitter:** NewX: Gallery profile Photos tab

## [3.28.0](https://github.com/crimera/piko-newx/compare/v3.27.1...v3.28.0) (2026-09-19)

### 🐛 Bug Fixes
* **Twitter - newx:** share crash log via direct activity intent ([b942d2b](https://github.com/crimera/piko/commit/b942d2b70bf021844aefba092a9469c672789725))

### ✨ New Features
* **Twitter - newx:** add crash test triggers to developer tools ([5b2b4a4](https://github.com/crimera/piko/commit/5b2b4a456c07063a3710c15b6f988b780ee8d974))
* **Twitter - newx:** add crash logs with share and copy actions ([5feb43d](https://github.com/crimera/piko/commit/5feb43d3ccf0390405963bad742cdcc0e329e21a))

### New Patches
* **Twitter:** NewX: Crash logs

## [3.27.1](https://github.com/crimera/piko-newx/compare/v3.27.0...v3.27.1) (2026-09-18)

### 🐛 Bug Fixes
* **Twitter:** add 12.27 prod ([4821dd1](https://github.com/crimera/piko/commit/4821dd10a7cdbc97a8d78e72e2b2b2b01b471d38))

## [3.27.0](https://github.com/crimera/piko-newx/compare/v3.26.2...v3.27.0) (2026-09-18)

### ✨ New Features
* **Twitter - newx:** hide badges from custom navigation bar items ([6c27e79](https://github.com/crimera/piko/commit/6c27e79dee4e6be5a1bf03e9c85b333f5e14781c))

## [3.26.2](https://github.com/crimera/piko-newx/compare/v3.26.1...v3.26.2) (2026-09-17)

### 🐛 Bug Fixes
* **Twitter:** Move NewX inline download click handling off the UI thread ([632b153](https://github.com/crimera/piko/commit/632b1538c44ae9851ebab03528c48e4599bc1191))

## [3.26.1](https://github.com/crimera/piko-newx/compare/v3.26.0...v3.26.1) (2026-09-17)

### 🐛 Bug Fixes
* **Twitter - newx:** stabilize drawer choice option IDs across app updates ([95226c8](https://github.com/crimera/piko/commit/95226c86aebea587e97d2dbd5e504fa4407a7290))
* **Twitter - newx:** dynamically resolve URT repository request in timeline refresh patch ([96245a7](https://github.com/crimera/piko/commit/96245a7f102042cf847837236ad85fd33ef83dbb))
* **Twitter - newx:** dynamically resolve compose settings row layout for 12.28 ([7bae415](https://github.com/crimera/piko/commit/7bae415ebc05f28daec60a094e4667e58215d9c3))
* **Twitter - newx:** harden drawer patch fingerprint and close argument resolution ([ac32219](https://github.com/crimera/piko/commit/ac32219b45d0ebad7c83fca4ece0ef3726887079))

## [3.26.0](https://github.com/crimera/piko-newx/compare/v3.25.1...v3.26.0) (2026-09-17)

### 🐛 Bug Fixes
* **Twitter - newx:** differentiate navigation editor icon ([1ba8355](https://github.com/crimera/piko/commit/1ba8355fa72811eb6a9ab36cee7bff02025d4e4e))

### ✨ New Features
* **Twitter - newx:** overhaul drawer items customization ([244602b](https://github.com/crimera/piko/commit/244602bdddb581a40a76c989c1172d934dc50ca2))

## [3.25.1](https://github.com/crimera/piko-newx/compare/v3.25.0...v3.25.1) (2026-09-16)

### 🐛 Bug Fixes
* **Twitter - newx:** auto-scroll navbar editor ([3ecf15b](https://github.com/crimera/piko/commit/3ecf15b5dca2d5de53c4721d11a8c37c57359af4))

## [3.25.0](https://github.com/crimera/piko-newx/compare/v3.24.2...v3.25.0) (2026-09-16)

### 🐛 Bug Fixes
* **Twitter - newx:** improve navbar editor drag feedback ([ac98563](https://github.com/crimera/piko/commit/ac985637a8d07c42ffb67abdeb2031635b9dc4c6))

### ✨ New Features
* **Twitter - newx:** overhaul navbar customization ([228171b](https://github.com/crimera/piko/commit/228171b6d9b9a509438009ba93984b60f99e2616))

## [3.24.2](https://github.com/crimera/piko-newx/compare/v3.24.1...v3.24.2) (2026-09-16)

### 🐛 Bug Fixes
* **Twitter - newx:** show selected destination icon ([02f91e5](https://github.com/crimera/piko/commit/02f91e57cf21e45b44c7e2c1dabdbacd9a186604))

## [3.24.1](https://github.com/crimera/piko-newx/compare/v3.24.0...v3.24.1) (2026-09-16)

### 🐛 Bug Fixes
* **Twitter - newx:** reduce navbar patch memory usage ([c36262f](https://github.com/crimera/piko/commit/c36262f1af8dfd29d4833452a1caa58fffd80dab))
* **Twitter - newx:** make restored splash background theme-aware ([84a4a39](https://github.com/crimera/piko/commit/84a4a3996e4b4b7ff58d0391920195a1cffa44b6))
* **Twitter - newx:** restore twitter blue app icon & splash colors ([e0b50c2](https://github.com/crimera/piko/commit/e0b50c2826ee5f9d16e01fb8540ad3b1bf95ca4e))

## [3.24.0](https://github.com/crimera/piko-newx/compare/v3.23.3...v3.24.0) (2026-09-16)

### ✨ New Features
* **Twitter - newx:** add drawer destinations to navbar editor ([d8a1526](https://github.com/crimera/piko/commit/d8a15266fc673fcad19c67532424a33f3ae51846))
* **Twitter - newx:** add customizable navigation bar ([032513b](https://github.com/crimera/piko/commit/032513bc4e04e565cc047a48749fac9f2c0dd76b))

### New Patches
* **Twitter:** NewX: Customize navigation bar

## [3.23.3](https://github.com/crimera/piko-newx/compare/v3.23.2...v3.23.3) (2026-09-14)

### 🐛 Bug Fixes
* **Twitter - newx:** preserve thread connectors when hiding dividers ([68170cd](https://github.com/crimera/piko/commit/68170cd326aeb1c3c5e39b3fc66468dda5782d73))

## [3.23.2](https://github.com/crimera/piko-newx/compare/v3.23.1...v3.23.2) (2026-09-14)

### 🐛 Bug Fixes
* **Twitter:** optimize NewX extension runtime hot paths ([9f8a462](https://github.com/crimera/piko/commit/9f8a462a9502fc283ff443a5691887482471bf68))
* **Twitter:** optimize NewX patch and runtime performance ([5fc1d2f](https://github.com/crimera/piko/commit/5fc1d2fe08ae37c42d1e8c42ee3e35d0f43b3174))

## [3.23.1](https://github.com/crimera/piko-newx/compare/v3.23.0...v3.23.1) (2026-09-14)

### 🐛 Bug Fixes
* **Twitter - newx:** restore Ranked Following scroll position ([26874a4](https://github.com/crimera/piko/commit/26874a446554910f744425074d660b4adfdb1148))

## [3.23.0](https://github.com/crimera/piko-newx/compare/v3.22.0...v3.23.0) (2026-09-14)

### ✨ New Features
* **Twitter - newx:** add customizable post menu with hidden items filter ([d80e46c](https://github.com/crimera/piko/commit/d80e46c660806edab1fea5412ddffb3b5c8420f0))

### New Patches
* **Twitter:** NewX: Customize post menu items

## [3.22.0](https://github.com/crimera/piko-newx/compare/v3.21.2...v3.22.0) (2026-09-14)

### 🐛 Bug Fixes
* **Twitter - newx:** eliminate timeline success constructor register corruption and VerifyError ([6049e08](https://github.com/crimera/piko/commit/6049e089f621a7f3700166a9e7122632655dbab5))
* **Twitter - newx:** make drawer content resolver semantic and deprecate 12.24 ([af4f1e4](https://github.com/crimera/piko/commit/af4f1e433429c44c066f2cdeb580bcfaef7061b9))
* **Twitter - newx:** resolve runtime verify errors and restore inline download icon in 12.27 ([2c4da85](https://github.com/crimera/piko/commit/2c4da853d752f8ab0f40c0c4a07a43ee1e79fe6d))
* **Twitter - newx:** port failing patches to 12.27.0-alpha.01 ([dec951d](https://github.com/crimera/piko/commit/dec951d008d8a617d234b374563408ba5d364c75))
* **Twitter - newx:** custom font patch for 12.27 Compose refactor ([d6efb26](https://github.com/crimera/piko/commit/d6efb26d263000ed9960069dd6fdc93348f12d90))
* **Twitter - newx:** support 12.27 settings renderer ([ee13d2f](https://github.com/crimera/piko/commit/ee13d2f7526d770ffb0b8b95c72fde3e4cd1a62d))

### ✨ New Features
* **Twitter - newx:** add 12.25.2-prod.01 to compatibility targets ([228a344](https://github.com/crimera/piko/commit/228a3440f3998f8e299ea0a484d782ed21d5ceb9))

## [3.21.2](https://github.com/crimera/piko-newx/compare/v3.21.1...v3.21.2) (2026-09-13)

### 🐛 Bug Fixes
* **Twitter - newx:** stabilize inline download icon selection ([764cd7b](https://github.com/crimera/piko/commit/764cd7bf765d96482b3412f356710098ce55fa97))
* **Twitter - newx:** skip disabled inline download render hooks ([3da9efd](https://github.com/crimera/piko/commit/3da9efdbe81d02dabf5c367726069878ab476742))
* **Twitter - newx:** make inline action membership identity based ([d2b0adb](https://github.com/crimera/piko/commit/d2b0adba393b38a49c9a3733f644bb5bd7051ca7))
* **Twitter - newx:** skip unnecessary inline media inspection ([148c74b](https://github.com/crimera/piko/commit/148c74bd9472b8783df5690d4dd25bfb62af0f66))
* **Twitter - newx:** avoid full media parsing during composition ([3bfd7ad](https://github.com/crimera/piko/commit/3bfd7ad087233e3fb867b211635364be21b79357))
* **Twitter - newx:** gate inline download diagnostics ([2391e51](https://github.com/crimera/piko/commit/2391e5129a37c843345c57921ae3d72a5d3f49e2))

### 🔧 Improvements
* **Twitter:** prune low-value NewX tests, add test policy to AGENTS.md ([88bd311](https://github.com/crimera/piko/commit/88bd311247e1992d383bbed8d8fe37b6f5555479))

## [3.21.1](https://github.com/crimera/piko-newx/compare/v3.21.0...v3.21.1) (2026-09-13)

### 🐛 Bug Fixes
* **Twitter:** inline download button showing the share icon ([f94e38c](https://github.com/crimera/piko/commit/f94e38c52418e06d607fdd6382caf027ae0e6760))
* **Twitter - newx:** validate dynamic choice resources ([0c01bf1](https://github.com/crimera/piko/commit/0c01bf1cb8db738d4046eb1602dc2dde56051349))

## [3.21.0](https://github.com/crimera/piko-newx/compare/v3.20.0...v3.21.0) (2026-09-13)

### 🐛 Bug Fixes
* **Twitter:** inline download icon classification ([47e6a6d](https://github.com/crimera/piko/commit/47e6a6db8e42b28301cd2b20a474f80629d0ee34))
* **Twitter:** group custom NewX post menu options ([ddacbad](https://github.com/crimera/piko/commit/ddacbad92cb4c65c8eaa1d3126ec44791121a223))

### ✨ New Features
* **Twitter - newx:** register dynamic choice resources ([fbf56bf](https://github.com/crimera/piko/commit/fbf56bfebdd021c9784ada806f4ed989b5cf4ec9))

### 🔧 Improvements
* **Twitter - newx:** discover drawer options dynamically ([7f21814](https://github.com/crimera/piko/commit/7f2181486a390b2d30ad27263f60340171e24415))

## [3.20.0](https://github.com/crimera/piko-newx/compare/v3.19.3...v3.20.0) (2026-09-13)

### ✨ New Features
* **Twitter - newx:** hide post and reply dividers ([46c7e67](https://github.com/crimera/piko/commit/46c7e6787c7a882485769790e7d8e0e6f6b1d519))

### New Patches
* **Twitter:** NewX: Hide post dividers

## [3.19.3](https://github.com/crimera/piko-newx/compare/v3.19.2...v3.19.3) (2026-09-12)

### 🐛 Bug Fixes
* **Twitter - newx:** support 12.26.0-alpha.03 ([0394de0](https://github.com/crimera/piko/commit/0394de0ff0f6983f175219e27d127c40bb7d8150))

## [3.19.2](https://github.com/crimera/piko-newx/compare/v3.19.1...v3.19.2) (2026-09-12)

### 🐛 Bug Fixes
* **Twitter - newx:** preserve inline download icon on recomposition ([baf3189](https://github.com/crimera/piko/commit/baf3189040abdfddb40cb76ecffd233846d8e995))

## [3.19.1](https://github.com/crimera/piko-newx/compare/v3.19.0...v3.19.1) (2026-09-11)

### 🐛 Bug Fixes
* **Twitter - newx:** keep dynamic color resolver API 29 compatible ([7242871](https://github.com/crimera/piko/commit/72428718c7e5de462ca81fecd9aa72eeedf0d2bf))

## [3.19.0](https://github.com/crimera/piko-newx/compare/v3.18.1...v3.19.0) (2026-09-11)

### 🐛 Bug Fixes
* **Twitter - newx:** scope timeline position restoration ([a238d89](https://github.com/crimera/piko/commit/a238d895f6c442de0d287f2a09ce9482824dc58f))

### ✨ New Features
* **Twitter - newx:** identify download notifications by username ([5554a69](https://github.com/crimera/piko/commit/5554a693357ef7113796496da59f59790cd2e8a8))

## [3.18.1](https://github.com/crimera/piko-newx/compare/v3.18.0...v3.18.1) (2026-09-11)

### 🐛 Bug Fixes
* **Twitter - newx:** support alpha.02 drawer renderer ([a4a44ad](https://github.com/crimera/piko/commit/a4a44ad50c6568822290e81f570b68156bb5e347))

## [3.18.0](https://github.com/crimera/piko-newx/compare/v3.17.0...v3.18.0) (2026-09-11)

### ✨ New Features
* **Twitter - newx:** use native in-app download notifications ([d748bf9](https://github.com/crimera/piko/commit/d748bf98692a78c748d0aabb273c33dfa50b00cc))

### 🔧 Improvements
* **Twitter - newx:** deprecate versions ([ea5edef](https://github.com/crimera/piko/commit/ea5edef5a57e1c8dc1b444a24239d29bff5f354f))

## [3.17.0](https://github.com/crimera/piko-newx/compare/v3.16.0...v3.17.0) (2026-09-10)

### 🐛 Bug Fixes
* **Twitter:** glide thumbnail cache routing ([9c1eb4a](https://github.com/crimera/piko/commit/9c1eb4a16465f8d4d5bbdab2948c2f029b6ddb89))
* **Twitter - newx:** preserve optional resolver fallbacks ([d583480](https://github.com/crimera/piko/commit/d5834805446cbd5537878688b52ba7c0ee53f805))
* **Twitter - newx:** allow missing drawer footer divider ([696e98a](https://github.com/crimera/piko/commit/696e98aba0c450c30dd68430e44b50934e94f4f2))
* **Twitter:** help center not getting hidden ([067a2ad](https://github.com/crimera/piko/commit/067a2ad3dbe8a6e8ae99c748c77baa9cc37229ce))

### ✨ New Features
* **Twitter - newx:** add default profile post sorting ([217326e](https://github.com/crimera/piko/commit/217326e18e8362dd3519ecbead237161b615a708))

### 🔧 Improvements
* **Twitter - newx:** rename default sorting patches ([d662eba](https://github.com/crimera/piko/commit/d662ebaac0d3134195b1521d9893784f381c8830))
* **Twitter - newx:** enforce resolver cardinality ([fad1d44](https://github.com/crimera/piko/commit/fad1d44851a1adfd1c48b4617d26efb5376b95ae))

### New Patches
* **Twitter:** NewX: Set default media tab
* **Twitter:** NewX: Set default profile post sorting
* **Twitter:** NewX: Set default reply sorting

## [3.16.0](https://github.com/crimera/piko-newx/compare/v3.15.0...v3.16.0) (2026-09-10)

### ✨ New Features
* **Twitter - newx:** support Twitter 12.26 alpha ([57eb9ae](https://github.com/crimera/piko/commit/57eb9ae8375f601000fb5834ec3a273fd0441782))

## [3.15.0](https://github.com/crimera/piko-newx/compare/v3.14.0...v3.15.0) (2026-09-10)

### 🐛 Bug Fixes
* **Twitter - newx:** enforce sensitive media write cardinality ([7b7b9d6](https://github.com/crimera/piko/commit/7b7b9d6d888c7c21b4946bb7265a38d73a392a35))
* **Twitter - newx:** enforce For You parameter cardinality ([65c058e](https://github.com/crimera/piko/commit/65c058ec18fbb6e9fde70ff37c8fe00cdd54f2cf))
* **Twitter - newx:** enforce premium accessor cardinality ([1a10f2b](https://github.com/crimera/piko/commit/1a10f2b28e07b9ff3396e1e2193f82dda7fb5583))
* **Twitter - newx:** enforce reply bar lookup cardinality ([4d37b2c](https://github.com/crimera/piko/commit/4d37b2ce2cc957bb7c50afe2c638d550c287323d))
* **Twitter - newx:** enforce inline action lookup cardinality ([6fd7cc3](https://github.com/crimera/piko/commit/6fd7cc3b8c60caf329c0bf883b1bcaa6b2389baf))
* **Twitter - newx:** enforce feature flag lookup cardinality ([736d57e](https://github.com/crimera/piko/commit/736d57eb0609773fc7eb250448d6a56f808ae41b))
* **Twitter - newx:** document dynamic color resolver order ([84a581c](https://github.com/crimera/piko/commit/84a581c223ae29463d23168dfea5de36c246268d))
* **Twitter - newx:** enforce drawer resolver cardinality ([2704191](https://github.com/crimera/piko/commit/2704191ae08bf528ead1d49f96e63c4bbec75fc7))
* **Twitter - newx:** document custom font resolver order ([eee29e6](https://github.com/crimera/piko/commit/eee29e6378694b1c6f723654b4da7e440d07e286))
* **Twitter - newx:** accept current navigation state shape ([51e6793](https://github.com/crimera/piko/commit/51e67935ace5112cac08b1a448336f113b725f08))
* **Twitter - newx:** resolve split drawer row renderers ([df97271](https://github.com/crimera/piko/commit/df97271873bd7cf6de01059f64d650b46485f97d))
* **Twitter - newx:** harden timeline position resolver ([8d0b88d](https://github.com/crimera/piko/commit/8d0b88dacff1052e9c0704be31a7b937117d6955))
* **Twitter - newx:** harden For You topic filter resolver ([6c4fa29](https://github.com/crimera/piko/commit/6c4fa295b6076f58d063875ce85c9439e58930f3))
* **Twitter - newx:** harden timeline tab resolver ([2606017](https://github.com/crimera/piko/commit/26060175647e08839d2d9dbd74ca3da3d15b4a04))
* **Twitter - newx:** harden premium upsell resolver ([36d35f5](https://github.com/crimera/piko/commit/36d35f53ff7765bde2bc694dc80fc1572346b8c7))
* **Twitter - newx:** harden premium fingerprints ([12f6f7a](https://github.com/crimera/piko/commit/12f6f7a13d0f9093890be822cbaa31e7e731e499))
* **Twitter - newx:** harden timeline model resolution ([c9ae181](https://github.com/crimera/piko/commit/c9ae18106c607269a6802004e0799718efe0b58e))
* **Twitter - newx:** harden semantic model introspection ([c52514a](https://github.com/crimera/piko/commit/c52514ac5bea0e681701e42f1380d82e144c317a))
* **Twitter - newx:** harden post model resolution ([e15a687](https://github.com/crimera/piko/commit/e15a68759b0d138f697cf197d4ea777dc7e38b3b))
* **Twitter - newx:** harden share image resolver ([f64d0eb](https://github.com/crimera/piko/commit/f64d0eb49838f68a9b7a8860e837d62625063e55))
* **Twitter - newx:** harden server logging resolver ([be3ad92](https://github.com/crimera/piko/commit/be3ad92170de01fc473f40a9ae5d939278c8d551))
* **Twitter - newx:** harden reply sorting resolver ([2297ebb](https://github.com/crimera/piko/commit/2297ebba12937a04d122ea1f3e46be0ded2227a9))
* **Twitter - newx:** harden post options resolver ([6ed8a40](https://github.com/crimera/piko/commit/6ed8a40cd4195a8b531ee3a4140149f1d2154c7d))
* **Twitter - newx:** harden post reply bar resolver ([6edf348](https://github.com/crimera/piko/commit/6edf3488ac9bfb793448f82ab9683151a78c25c3))
* **Twitter - newx:** harden default media tab resolver ([555a6e7](https://github.com/crimera/piko/commit/555a6e746d83413895b251e08553d4c0236244b2))
* **Twitter - newx:** harden media quality resolver ([df28ff0](https://github.com/crimera/piko/commit/df28ff0ecf4f658816dc125d182ad7746c3287e3))
* **Twitter - newx:** harden feature flag resolver ([166c6c7](https://github.com/crimera/piko/commit/166c6c7f350003ce756e923fc235fe7a828028de))
* **Twitter - newx:** harden dynamic color resolver ([f81859b](https://github.com/crimera/piko/commit/f81859b9ac2d97bf269098dd6d4c56007460158d))
* **Twitter - newx:** harden drawer resolver ([8df3015](https://github.com/crimera/piko/commit/8df301541fe10b583ee90f6d581c8519b7e38486))
* **Twitter - newx:** harden custom sharing domain resolver ([f2c9c4c](https://github.com/crimera/piko/commit/f2c9c4c9aa674a11473cf6dc5caa81683ba4ac52))
* **Twitter - newx:** harden canonical URL resolver ([75823b9](https://github.com/crimera/piko/commit/75823b9f9bdc4014541b816de4cd71fad5cee6b4))

### ✨ New Features
* **Twitter - newx:** add resolver cardinality helpers ([ad21b64](https://github.com/crimera/piko/commit/ad21b649be42715ad9677fef69e8d39dcada186f))

### Commits
* **Twitter - newx:** mark 12.25 prod compatible ([3f70880](https://github.com/crimera/piko/commit/3f70880f96729adf86a4e957ce22332bac379d8d))
* **Twitter - newx:** add resolver cardinality linter ([3ffb421](https://github.com/crimera/piko/commit/3ffb4219ee9599bb12d601e03ba81b4a297f7a77))
* **Twitter:** document newx resolver tooling ([ee694cb](https://github.com/crimera/piko/commit/ee694cb3721827571e103d4d470b7c114f23071b))

## [3.14.0](https://github.com/crimera/piko-newx/compare/v3.13.3...v3.14.0) (2026-09-09)

### ✨ New Features
* **Twitter:** support 12.24.0-prod.02 ([6eb5236](https://github.com/crimera/piko/commit/6eb5236af4088e19f1d3914f1ff9373f2c7d231d))

## [3.13.3](https://github.com/crimera/piko-newx/compare/v3.13.2...v3.13.3) (2026-09-09)

### 🐛 Bug Fixes
* **Twitter - newx:** restore photo viewer navigation inset ([ccb7457](https://github.com/crimera/piko/commit/ccb74571c35cedd8b34aa20deb8556749960477c))

## [3.13.2](https://github.com/crimera/piko-newx/compare/v3.13.1...v3.13.2) (2026-09-09)

### 🐛 Bug Fixes
* **Twitter - newx:** harden reply bar fingerprints ([ca6a72a](https://github.com/crimera/piko/commit/ca6a72ad425a3ff25a1eefa08e335c578378b63c))
* **Twitter - newx:** eliminate post-detail reply bar gradient scrim and insets ([98ee98c](https://github.com/crimera/piko/commit/98ee98c84523b21963bb0dcfbf474855acc1402d))

## [3.13.1](https://github.com/crimera/piko-newx/compare/v3.13.0...v3.13.1) (2026-09-09)

### 🐛 Bug Fixes
* **Twitter - newx:** handle empty timeline pages and external deeplinks ([295ba45](https://github.com/crimera/piko/commit/295ba453f9fdd660fa24a055202a03a246a9a85d))

### Commits
* **Twitter:** update agents.md ([55b0e54](https://github.com/crimera/piko/commit/55b0e547421ef0153bd7cf7dffcf4548c911b3a7))

## [3.13.0](https://github.com/crimera/piko-newx/compare/v3.12.1...v3.13.0) (2026-09-08)

### 🐛 Bug Fixes
* **Twitter - newx:** allow user-initiated topic refresh ([7d4af7d](https://github.com/crimera/piko/commit/7d4af7d59e8986906794ef3bc5d9502e96de52aa))
* **Twitter - newx:** preserve timeline position during deep-link loads ([a04d7c9](https://github.com/crimera/piko/commit/a04d7c9fa3ba1f5ca71126551be8483f2971337c))

### ✨ New Features
* **Twitter - newx:** add piko settings on sidebar ([e2976cf](https://github.com/crimera/piko/commit/e2976cf79e2327c3b15778b8a1d8ea75a021843a))

## [3.12.1](https://github.com/crimera/piko-newx/compare/v3.12.0...v3.12.1) (2026-09-08)

### 🐛 Bug Fixes
* **Twitter - newx:** gate startup refresh on saved timeline position ([449c6d2](https://github.com/crimera/piko/commit/449c6d26d81b4a66f472bd7c7ff98fd33ec570cb))
* **Twitter - newx:** suppress populated timeline auto refresh ([2b48c7b](https://github.com/crimera/piko/commit/2b48c7b267f68bc5e3b28b580c56d6f7ca8c6865))
* **Twitter - newx:** preserve initial timeline load ([2638690](https://github.com/crimera/piko/commit/26386906402fce01e1ad8af86d9997a99128e1e0))
* **Twitter - NewX:** hook Glide thumbnail cache ([b6bed05](https://github.com/crimera/piko/commit/b6bed05f8c5146a814e2992cf25a74ba7a66979e))

### Commits
* **Twitter:** gate thumbnail cache backend ([41d3a33](https://github.com/crimera/piko/commit/41d3a33fe4a0a53b088af69b35441edac5564ef0))

## [3.12.0](https://github.com/crimera/piko-newx/compare/v3.11.0...v3.12.0) (2026-09-08)

### 🐛 Bug Fixes
* **Twitter - newx:** gate For You topic sheet on reselect ([00c446a](https://github.com/crimera/piko/commit/00c446a5ae61bf35d83e23811350e127e78b8b62))
* **Twitter - newx:** support refactored default media tab seed ([d7708ea](https://github.com/crimera/piko/commit/d7708ea92748a0b7aa954bb6d581929cdb39eb1e))
* **Twitter - newx:** support canonical profile links after package move ([5cc1155](https://github.com/crimera/piko/commit/5cc11555186fa34debe4465d220e1a0abb0a5cae))
* **Twitter - newx:** support highest media quality in newer builds ([cbb7f30](https://github.com/crimera/piko/commit/cbb7f307a8f9623ae7a894fbe8a26ccc5b2bae39))
* **Twitter - newx:** support alpha timeline tab route arrays ([6cfc118](https://github.com/crimera/piko/commit/6cfc1189103e3f1e615abf74626258dc4bb8b979))

### ✨ New Features
* **Twitter:** experimental support for 12.25.0-alpha.01 ([cd76e4b](https://github.com/crimera/piko/commit/cd76e4b58441f3bf317f74138fe125a1f8b593b5))
* **Twitter:** Improve NewX timeline patch compatibility ([b89697a](https://github.com/crimera/piko/commit/b89697a4a3398feedbcd61e27b1c03f2395ed8a8))

### Commits
* **Twitter:** update script ([5e76a62](https://github.com/crimera/piko/commit/5e76a627058375039b97799665244ce45e1d78a4))

## [3.11.0](https://github.com/crimera/piko-newx/compare/v3.10.7...v3.11.0) (2026-09-08)

### ✨ New Features
* **Twitter - newx:** add disable blur setting ([1fa4361](https://github.com/crimera/piko/commit/1fa43617f89053fdb1e9241217c200add48d3880))

### Commits
* **Twitter:** untrack recent documentation ([aedc22b](https://github.com/crimera/piko/commit/aedc22b1f22b23dc4076e4594beebc470a1f2088))

### New Patches
* **Twitter:** NewX: Disable blur effects

## [3.10.7](https://github.com/crimera/piko-newx/compare/v3.10.6...v3.10.7) (2026-09-07)

### 🐛 Bug Fixes
* **Twitter:** format changelogs for Morphe app updates ([f66771a](https://github.com/crimera/piko-newx/commit/f66771a2880d3b08515cdb7cd93d6abbd8788735))

### Commits
* **Twitter - newx:** detect hidden media conflicts on AOSP ([9809bbd](https://github.com/crimera/piko/commit/9809bbd1e83aaea8bb105ca7d365bc5ee985e24c))
* **Twitter - newx:** add hide post reply bar toggle ([68a1fb8](https://github.com/crimera/piko/commit/68a1fb866ebbf4936da0eb347d53806a3dc68d3f))
* **Twitter:** add show poll results patch ([09f8bf7](https://github.com/crimera/piko/commit/09f8bf71f530e36c52b7cf52cc249fbb3c48fdb9))

### New Patches
* **Twitter:** NewX: Hide post reply bar
* **Twitter:** NewX: Show poll results

# [v3.10.6](https://github.com/crimera/piko-newx/releases/tag/v3.10.6) (2026-09-06)

### Commits
* [`4f98e4a`](https://github.com/crimera/piko/commit/4f98e4a28c0fde7555faa48eb7dd5d82ab39b448) feat(newx): add timeline tabs bar toggle
* [`bc03fce`](https://github.com/crimera/piko/commit/bc03fce4352bcb7ee89299722d0e900af3fb8a82) fix(newx): harden timeline tabs bar resolver

### New Patches
* **Twitter:** NewX: Hide timeline tabs bar

# [v3.10.5](https://github.com/crimera/piko-newx/releases/tag/v3.10.5) (2026-09-06)

### Commits
* [`eb4054d`](https://github.com/crimera/piko/commit/eb4054d91e21e33ee0f245c8388f0ff95fa8003f) feat(newx): restore twitter bird for notification icons
* [`73449eb`](https://github.com/crimera/piko/commit/73449eb838c0578296309b4213354719f9d26c07) feat(newx): add timeline tab customization

### New Patches
* **Twitter:** NewX: Customize timeline tabs

# [v3.10.4](https://github.com/crimera/piko-newx/releases/tag/v3.10.4) (2026-09-06)

### Commits
* [`6801e73`](https://github.com/crimera/piko/commit/6801e732e976149a74cc3363cf30883614fcbb9a) fix(newx): add toggle to show inline download button on posts without media

# [v3.10.3](https://github.com/crimera/piko-newx/releases/tag/v3.10.3) (2026-09-06)

### Commits
* [`5f0905a`](https://github.com/crimera/piko/commit/5f0905a302310e62279e1fc20b83345e60ecc696) fix(newx): stage inline downloads privately on Q+ to prevent public temp orphans

# [v3.10.2](https://github.com/crimera/piko-newx/releases/tag/v3.10.2) (2026-09-06)

### Commits
* [`c3fad63`](https://github.com/crimera/piko/commit/c3fad63a130bc2fbbbeea824a2147e41bcace1c6) feat(newx): add canonical URL toggle
* [`e1f8991`](https://github.com/crimera/piko/commit/e1f8991fe5b732f77911927574e8bf2e4d06ed57) feat(newx): add custom For You topic selector
* [`0b01176`](https://github.com/crimera/piko/commit/0b011766d5759e5f20c01eebdb7027d7240e5bbb) fix(newx): keep canonical URL hook reachable
* [`ed3f648`](https://github.com/crimera/piko/commit/ed3f648dc1edde1af2972acf2a6f51c092d4a2b1) feat(newx): add For You filtering settings
* [`05dfda1`](https://github.com/crimera/piko/commit/05dfda1c194116a89d676f04cda1056d5bce5f7a) fix(newx): mirror native topic sheet actions
* [`5b0f0f9`](https://github.com/crimera/piko/commit/5b0f0f9920f21e2251878252b269095163d0085d) fix(newx): refresh and scroll For You after topic action
* [`6094a31`](https://github.com/crimera/piko/commit/6094a31ead58e4a910df189c567912e4cb81e130) fix(newx): harden For You topic hook resolution
* [`b1be556`](https://github.com/crimera/piko/commit/b1be5566a94fcea39a7ba477c53092c1c99080ce) fix(newx): scope verified post filtering
* [`ef1166c`](https://github.com/crimera/piko/commit/ef1166ca2153c600aab130770054b04747f3942c) fix(newx): resolve filtered replies through parent chain
* [`b813aa5`](https://github.com/crimera/piko/commit/b813aa5fda6fe0c81d7146d8f781d5d1703001a9) fix(newx): return last resolved root on alias-chain overflow
* [`07e69e4`](https://github.com/crimera/piko/commit/07e69e484cda1fc4b7cbe2f355977d87e21bdd66) fix(newx): scope conversation aliasing to verified thread passes
* [`0115153`](https://github.com/crimera/piko/commit/01151536e57dfd87edda0ee0107383350cf1ae04) feat(newx): keep thread owner replies in their own conversations
* [`47e842f`](https://github.com/crimera/piko/commit/47e842ffe1011f1a00d2e5e778c0816afa6cfc3a) chore(newx): untrack filtering investigation docs
* [`9552264`](https://github.com/crimera/piko/commit/95522646e25ebb59864e576c4641486b1f308146) feat(newx): add toggle for Filtered replies menu item

# [v3.10.1](https://github.com/crimera/piko-newx/releases/tag/v3.10.1) (2026-09-05)

### Commits
* [`4707bcd`](https://github.com/crimera/piko/commit/4707bcd04f5f8e65f73e65cea613ad013f88de87) feat(newx): tint tab labels, icons and indicators with dynamic colors
* [`27c7d51`](https://github.com/crimera/piko/commit/27c7d516c76b57152061f28850839791806e3160) chore(newx): add Twitter 12.23.1 compatibility

# [v3.10.0](https://github.com/crimera/piko-newx/releases/tag/v3.10.0) (2026-09-05)

## Features
- add semantic release versions ([1daf1a3](https://github.com/crimera/piko-newx/commit/1daf1a31861e19cbf8b1b52fac3caa1f18d82d5d))

### Commits
* [`8588480`](https://github.com/crimera/piko/commit/85884801f22198259fc6ab3f08686fa66686d23d) feat(newx): add opt-in server diagnostics
* [`ae5130f`](https://github.com/crimera/piko/commit/ae5130f1014315d73d30352e77220401742ae906) feat: Add NewX color customization patch
* [`d545cd9`](https://github.com/crimera/piko/commit/d545cd9a0243afd390a423c0b89cb991c5762a6d) feat: add verified account filtering and theme custom screens
* [`1772d37`](https://github.com/crimera/piko/commit/1772d37b21aa0a731ad87e499d311b525467f09d) fix: refine NewX filtering settings
* [`b389397`](https://github.com/crimera/piko/commit/b389397710ff80f2e57a421aee1db9860ddbfcc3) fix: NewX accent color propagation

### New Patches
* **Twitter:** NewX: Server error logging
* **Twitter:** NewX: Unlock color customization
* **Twitter:** NewX: Hide posts by verified account type

# [12.22.0-prod.01-01aec60](https://github.com/crimera/piko-newx/releases/tag/12.22.0-prod.01-01aec60) (2026-09-04)

### Commits
* [`01aec60`](https://github.com/crimera/piko/commit/01aec60e581207700d23b32ab378544c5cbb1c90) feat(newx): add setting toggle to show or hide merge button

# [12.22.0-prod.01-e7cb40f](https://github.com/crimera/piko-newx/releases/tag/12.22.0-prod.01-e7cb40f) (2026-09-04)

### Commits
* [`e7cb40f`](https://github.com/crimera/piko/commit/e7cb40fe66408f6da6177f89aed720de80b00f7f) feat(newx): add download and merge action to media picker

# [12.22.0-prod.01-fceaaf2](https://github.com/crimera/piko-newx/releases/tag/12.22.0-prod.01-fceaaf2) (2026-09-04)

### Commits
* [`cfcb6fe`](https://github.com/crimera/piko/commit/cfcb6fee564a6b4a74290419a6f7669b6d851f59) fix(newx): support moved share intent helper
* [`f790f60`](https://github.com/crimera/piko/commit/f790f60c9436a264bd39a3f9f201871ba1ae782e) fix(newx): resolve For You topic constructor parameter
* [`fceaaf2`](https://github.com/crimera/piko/commit/fceaaf29c39c835d02f57c467d65842502465652) chore(newx): add Twitter 12.23.0 compatibility

# [12.22.0-prod.01-3c75b44](https://github.com/crimera/piko-newx/releases/tag/12.22.0-prod.01-3c75b44) (2026-09-04)

### Commits
* [`3c75b44`](https://github.com/crimera/piko/commit/3c75b44c2798b1375e7c1e396a801f080d862ef6) feat(newx): restore Twitter branding patch

### New Patches
* **Twitter:** NewX: Restore Twitter branding

# [12.22.0-prod.01-3a3fa60](https://github.com/crimera/piko-newx/releases/tag/12.22.0-prod.01-3a3fa60) (2026-09-03)

### Commits
* [`708a820`](https://github.com/crimera/piko/commit/708a820b56b44a06e4ab257b27ad54a3d1314865) feat(newx): reuse app image cache for media thumbnails
* [`d006d98`](https://github.com/crimera/piko/commit/d006d985fb4f292e76a971920e7291dedb045cea) fix(newx): reserve parameter registers in cache bridge
* [`ace36be`](https://github.com/crimera/piko/commit/ace36be891b402a285f8044b5c03a2aa1f5021f0) debug(newx): log media thumbnail loading state
* [`a9bb154`](https://github.com/crimera/piko/commit/a9bb1546d87618e760e6a4c2d6ab4216c78314cc) refactor(newx): isolate Coil thumbnail cache bridge
* [`c3fddd2`](https://github.com/crimera/piko/commit/c3fddd2ca39943d5312c21e9748fe662358cc63d) feat(newx): add configurable logging
* [`c4897ba`](https://github.com/crimera/piko/commit/c4897ba51a5ef5ed8814f3074affd989b5d9cdb0) chore(newx): hide cache bridge dependency
* [`3a3fa60`](https://github.com/crimera/piko/commit/3a3fa609f83d4d1a899748de32aa0a81be3c99d7) fix(newx): simplify inline settings

# [12.22.0-prod.01-f384055](https://github.com/crimera/piko-newx/releases/tag/12.22.0-prod.01-f384055) (2026-09-03)

### Commits
* [`18b28ae`](https://github.com/crimera/piko/commit/18b28ae3ce9f8c35660af7a70ccc788f6837eef0) feat(newx): show media thumbnails in download picker
* [`4e952a1`](https://github.com/crimera/piko/commit/4e952a1ca281fcd52c76c5df8f8447af730982c7) feat(newx): add thumbnail loading setting
* [`f384055`](https://github.com/crimera/piko/commit/f384055ecec0e2e6447986a30ddf43cfaa2f835f) feat(newx): group inline download settings

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

