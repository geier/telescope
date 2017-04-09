
tootsuite/mastodon
==================
A GNU Social-compatible microblogging server
https://github.com/tootsuite/mastodon/releases/

1.1 v1.1 2017-04-07T11:20:47Z
-----------------------------
Regular iterative release in a stable state.

v1.1  2017-04-07T11:08:51Z
--------------------------
Tag release, no description

etesync/pyetesync
=================
EteSync - Client python bindings
https://github.com/etesync/pyetesync/releases/

v0.3.2  2017-04-07T11:07:59Z
----------------------------
Tag release, no description

v0.3.1  2017-04-05T13:04:06Z
----------------------------
Tag release, no description

v0.2.0  2017-04-03T17:20:08Z
----------------------------
Tag release, no description

lgeek/okreader
==============
Free/libre software for Kobo ebook readers
https://github.com/lgeek/okreader/releases/

 a9bf918_build 2017-04-04T00:08:21Z
-----------------------------------

maartenbreddels/ipyvolume
=========================
3d plotting for Python in the Jupyter notebook based on IPython widgets using WebGL
https://github.com/maartenbreddels/ipyvolume/releases/

0.3.2  2017-04-02T13:36:16Z
---------------------------
Tag release, no description

0.3.1  2017-04-02T11:24:30Z
---------------------------
Tag release, no description

SirCmpwn/sway
=============
i3-compatible Wayland compositor
https://github.com/SirCmpwn/sway/releases/

0.12.2 0.12.2 2017-04-03T15:06:28Z
----------------------------------
# Changes

* 444 is permitted as an access mode for security configs (@jnsaff - #1117)

# Bugs fixed

* `move next` could cause crashes (@oranenj - #1130)
* New windows could steal focus from fullscreen windows (@zandrmartin - #1126)
* Fix problem with workspace_layout auto (@oranenj - #1119)
* Fix build for systems where wlc headers are not installed globally (@snoack - #1115)

gogits/gogs
===========
Gogs is a painless self-hosted Git service.
https://github.com/gogits/gogs/releases/

0.11.4 v0.11.4 2017-04-05T17:28:12Z
-----------------------------------
#### Bug fixes

- Client is not informed to provide credentials during HTTP/HTTPS push/pull
- Mirror credentials are not URL encoded [#4014](https://github.com/gogits/gogs/issues/4014)
- Create pull request buttons are showed on branches page when pull request is disabled [#4377](https://github.com/gogits/gogs/issues/4377)
- Panic if user has validation error on installation [#4383](https://github.com/gogits/gogs/issues/4383)

0.11 v0.11 2017-04-04T00:34:24Z
-------------------------------
#### Bug fixes

- Profile editing looses changes on validation error [#1123](https://github.com/gogits/gogs/issues/1123)
- Wrong repository count in organization dashboard [#4351](https://github.com/gogits/gogs/issues/4351)
- Fail to migrate from version prior to 0.10 [#4355](https://github.com/gogits/gogs/issues/4355)
- Private repository with public issues didn't handle anonymous visit properly [#4359](https://github.com/gogits/gogs/issues/4359)

v0.11.4  2017-04-05T17:26:53Z
-----------------------------
Tag release, no description

v0.11  2017-04-04T00:06:15Z
---------------------------
Tag release, no description

neurophysik/jitcode
===================
Just-in-Time Compilation for Ordinary Differential Equations
https://github.com/neurophysik/jitcode/releases/

0.51  2017-04-08T10:46:09Z
--------------------------
Tag release, no description

gorhill/uMatrix
===============
uMatrix: Point and click matrix to filter net requests according to source, destination and type
https://github.com/gorhill/uMatrix/releases/

 1.0.0 2017-04-07T19:41:17Z
---------------------------
## Changes:

Media resources are now reported in the ~`image`~ `plugin` column (to be renamed `media`), having these reported in the `other` column does not make much sense. Typically, users of uMatrix would have the click-to-play setting for plug-ins enabled in their browser -- this has always been the recommended settings. Hence this means that if one allow media, this won't necessarily allow plugins, these will still be click-to-play. Plugins are slowly disappearing, and having a column strictly dedicated to plugins is wasteful, thus I decided to merge media and plugins.

Websocket connection attempts are reported in the `xhr` column.

There is now a badge on the per-site switches icon, which badge displays the number of switches which are currently turned on. This should help remind user to also check for these switches when trying to un-break a web page.

The assets management code has been refactored by importing code from uBlock Origin. Given the amount of work required and given the not-enough-time issue, all the hosts files you may have un-selected will be selected again. You will have to un-selected them again. Sorry, I just do not have the time for backward compatibility.

There is now a hybrid webextension version for uMatrix, see `uMatrix.webext.zip` below. The migration process is exactly the same as with uBlock Origin, see <https://github.com/gorhill/uBlock/releases>.

## Closed as fixed:

### Chromium
- [Add Support for WebSocket Connections for Chromium](https://github.com/gorhill/uMatrix/issues/727)
- [UI glitch](https://github.com/gorhill/uMatrix/issues/711)
    - Possibly a browser bug as the issue didn't exist until recent Chromium versions (57+). However I do not have time to investigate, the fix is to work around the weird issue observed in Chromium.

#### Firefox
- [uBO broken on Firefox mozilla-central tip](https://github.com/gorhill/uBlock/issues/2493) (fixed by @gijsk through pull request #2493)
- [Incompatibility between ABP and uBO over FETCH (json)](https://github.com/gorhill/uBlock/issues/2226)
- [IPv6 password form submission fails](https://github.com/gorhill/uMatrix/issues/597)

#### SeaMonkey
- [Error when dealing with DOMParser.parseFromString()](https://github.com/gorhill/uMatrix/issues/706)
- [Toolbar icon gone in private browsing window](https://github.com/gorhill/uMatrix/issues/586)

#### Core
- [Images loaded via `<img srcset="...">` are shown in 'other' column](https://github.com/gorhill/uMatrix/issues/752)
- [IPv6 rules are not saved across restarts and not properly applied](https://github.com/gorhill/uMatrix/issues/747)
- [Why not grey out three dots for better clarity?](https://github.com/gorhill/uMatrix/issues/484)
  - The chosen solution is to display the number of currently turned on switches as a badge on the icon.

 0.9.9b12 2017-04-03T03:31:32Z
------------------------------
## Changes:

Media resources are now reported in the ~`image`~ `plugin` column (to be renamed `media`), having these reported in the `other` column does not make much sense. Typically, users of uMatrix would have the click-to-play setting for plug-ins enabled in their browser -- this has always been the recommended settings. Hence this means that if one allow media, this won't necessarily allow plugins, these will still be click-to-play. Plugins are slowly disappearing, and having a column strictly dedicated to plugins is wasteful, thus I decided to merge media and plugins.

Websocket connection attempts are reported in the `xhr` column.

There is now a badge on the per-site switches icon, which badge displays the number of switches which are currently turned on. This should help remind user to also check for these switches when trying to un-break a web page.

The assets management code has been refactored by importing code from uBlock Origin. Given the amount of work required and given the not-enough-time issue, all the hosts files you may have un-selected will be selected again. You will have to un-selected them again. Sorry, I just do not have the time for backward compatibility.

There is now a hybrid webextension version for uMatrix, see `uMatrix.webext.zip` below. The migration process is exactly the same as with uBlock Origin, see <https://github.com/gorhill/uBlock/releases>.

## Closed as fixed:

### Chromium
- [Add Support for WebSocket Connections for Chromium](https://github.com/gorhill/uMatrix/issues/727)
- [UI glitch](https://github.com/gorhill/uMatrix/issues/711)
    - Possibly a browser bug as the issue didn't exist until recent Chromium versions (57+). However I do not have time to investigate, the fix is to work around the weird issue observed in Chromium.

#### Firefox
- [uBO broken on Firefox mozilla-central tip](https://github.com/gorhill/uBlock/issues/2493) (fixed by @gijsk through pull request #2493)
- [Incompatibility between ABP and uBO over FETCH (json)](https://github.com/gorhill/uBlock/issues/2226)
- [IPv6 password form submission fails](https://github.com/gorhill/uMatrix/issues/597)

#### SeaMonkey
- [Error when dealing with DOMParser.parseFromString()](https://github.com/gorhill/uMatrix/issues/706)
- [Toolbar icon gone in private browsing window](https://github.com/gorhill/uMatrix/issues/586)

#### Core
- [Images loaded via `<img srcset="...">` are shown in 'other' column](https://github.com/gorhill/uMatrix/issues/752)
- [IPv6 rules are not saved across restarts and not properly applied](https://github.com/gorhill/uMatrix/issues/747)
- [Why not grey out three dots for better clarity?](https://github.com/gorhill/uMatrix/issues/484)
  - The chosen solution is to display the number of currently turned on switches as a badge on the icon.

1.0.0  2017-04-07T19:38:43Z
---------------------------
Tag release, no description

0.9.9b12  2017-04-03T03:22:11Z
------------------------------
Tag release, no description

be5invis/Iosevka
================
Slender typeface for code, from code.
https://github.com/be5invis/Iosevka/releases/

Iosevka, version 1.12.3, codename Lorraine-3 v1.12.3 2017-04-05T08:08:34Z
-------------------------------------------------------------------------
### Modifications since version 1.11.5
- **1.12.3**
  - (Ligation) Fixed broken arrows like `<------>`.
  - (Ligation) Added ligation for `<|`, `|>` and `<|>`.
  - (Symbols) Fixing and adding more arrows.
- **1.12.2**
  - (Building) Added `clean` target for a clean build.
  - (Symbols) Added support for double arrows like `⇒`.
  - (Styles) Added `ss10` style set.
- **1.12.1**
  - Refactored building scripts.
  - Optimized shapes of several Cyrillic letters.
  - Added `stress-fw` building option.
- **1.12.0**
  - Added new character variants for `$`, `Q`, `t` and `#`.

---

### Download Options

#### Iosevka

Iosevka provides a large variety of variants. 

- **Shape**: The shape of letter `i` and `l`.
  ![Styles Preview](https://raw.githubusercontent.com/be5invis/Iosevka/master/images/variants.png)
- **Spacing**: How wide some specific characters are.
  - _Default_: The default variant with ligatures and semantic full-width glyphs.
  - _Terminal_: Exact monospaced font without ligatures and full-width glyphs. Since some environments cannot interpret Iosevka as monospaced, and have difficulties with ligatures included, you can use Iosevka Term as an alternative.
  - _Typesetting_: Similar to _Default_, but more mathematical symbols are wider.
  - _CC_: Some of the symbols are en-widen to maintain compatibility with CJK typefaces. Ligatures are included.
- **Slab**: Whether the font is slab-serif.
- **Ligatures**: Whether the ligatures is included. The “no-ligature” variants are used for some Linux-based environments cannot handle ligatures correctly.
- **Family Name**: The family name of the font in your OS after installation. If two variants share the same family name, they cannot be installed together.

| Download Option | Shape | Spacing | Slab | Ligatures | Family Name |
| --- | --- | --- | --- | --- | --- |
| `01-iosevka-#.#.#` | _Default_ | _Default_ | No | **Yes** | `Iosevka` |
| `02-iosevka-term-#.#.#` | _Default_ | _Terminal_ | No | No | `Iosevka Term` |
| `03-iosevka-type-#.#.#` | _Default_ | _Typesetting_ | No | **Yes** | `Iosevka Type` |
| `04-iosevka-cc-#.#.#` | _Default_ | _CC_ | No | **Yes** | `IosevkaCC` |
| `05-iosevka-slab-#.#.#` | _Default_ | _Default_ | **Yes** | **Yes** | `Iosevka Slab` |
| `06-iosevka-term-slab-#.#.#` | _Default_ | _Terminal_ | **Yes** | No | `Iosevka Term Slab` |
| `07-iosevka-type-slab-#.#.#` | _Default_ | _Typesetting_ | **Yes** | **Yes**| `Iosevka Type Slab` |
| `08-iosevka-cc-slab-#.#.#` | _Default_ | _CC_ | **Yes** | **Yes** | `IosevkaCC Slab` |
| `09-iosevka-hooky-#.#.#` | _Hooky_ | _Default_ | No | **Yes** | `Iosevka` |
| `10-iosevka-hooky-term-#.#.#` | _Hooky_ | _Terminal_ | No | No | `Iosevka Term` |
| `11-iosevka-zshaped-#.#.#` | _Z-shaped_ | _Default_ | No | **Yes** | `Iosevka` |
| `12-iosevka-zshaped-term-#.#.#` | _Z-shaped_ | _Terminal_ | No | No | `Iosevka Term` |

The bundled `iosevka-pack-#.#.#` option contains all packages from `01.iosevka-#.#.#` to `08.iosevka-cc-slab-#.#.#`.

#### Inziu Iosevka

Inziu Iosevka is provided in two formats:

- `inziu-iosevka-#.#.#` : Fonts bundled as TTCs.
- `inziu-iosevka-ttfs-#.#.#` : Fonts bundled as TTFs.

Iosevka, version 1.12.2, codename Lorraine-2 v1.12.2 2017-04-03T07:20:01Z
-------------------------------------------------------------------------
### Modifications since version 1.11.5
- **1.12.2**
  - (Building) Added `clean` target for a clean build.
  - (Symbols) Added support for double arrows like `⇒`.
  - (Styles) Added `ss10` style set.
- **1.12.1**
  - Refactored building scripts.
  - Optimized shapes of several Cyrillic letters.
  - Added `stress-fw` building option.
- **1.12.0**
  - Added new character variants for `$`, `Q`, `t` and `#`.

Iosevka, version 1.12.1, codename Lorraine-1 v1.12.1 2017-04-01T17:10:58Z
-------------------------------------------------------------------------
### Modifications since version 1.11.5
- **1.12.1**
  - Refactored building scripts.
  - Optimized shapes of several Cyrillic letters.
  - Added `stress-fw` building option.
- **1.12.0**
  - Added new character variants for `$`, `Q`, `t` and `#`.

v1.12.3  2017-04-05T07:51:43Z
-----------------------------
Tag release, no description

v1.12.2  2017-04-03T07:17:39Z
-----------------------------
Tag release, no description

v1.12.1  2017-04-01T17:05:34Z
-----------------------------
Tag release, no description

nvdv/vprof
==========
Visual Python profiler
https://github.com/nvdv/vprof/releases/

v0.36 v0.36 2017-04-09T08:36:15Z
--------------------------------
vprof 0.36 has been released.

## New features

### Code heatmap shows run times for individual lines
Now you can see run time distribution over executed lines on code heatmap tab. 
The feature is experimental and will be improved in future versions.


![4ebd7ec4-042d-11e7-9489-e821b449bd6f](https://cloud.githubusercontent.com/assets/745431/24835955/1898f356-1d18-11e7-80f4-bfb0e4a43c0c.png)

syl20bnr/spacemacs
==================
A community-driven Emacs distribution - The best editor is neither Emacs nor Vim,  it's Emacs *and* Vim!
https://github.com/syl20bnr/spacemacs/releases/

Version 0.200.9 v0.200.9 2017-04-07T03:16:24Z
---------------------------------------------
- [Fixes](#0-200-9-sec-1)

# Fixes<a name="0-200-9-sec-1"></a>

-   Fix theme loading with terminal Emacs (thanks to wang0z)

Version 0.200.8 v0.200.8 2017-04-02T06:19:54Z
---------------------------------------------
- [Convention changes](#0-200-8-sec-1)
- [Dotspacemacs changes](#0-200-8-sec-2)
- [Core changes](#0-200-8-sec-3)
- [Distribution layer changes](#0-200-8-sec-4)
- [Layer changes](#0-200-8-sec-5)
  - [Ansible](#0-200-8-sec-5-1)
  - [Auto-completion](#0-200-8-sec-5-2)
  - [Better defaults](#0-200-8-sec-5-3)
  - [Chinese](#0-200-8-sec-5-4)
  - [Chrome](#0-200-8-sec-5-5)
  - [Clojure](#0-200-8-sec-5-6)
  - [Common Lisp](#0-200-8-sec-5-7)
  - [CSharp](#0-200-8-sec-5-8)
  - [Elixir](#0-200-8-sec-5-9)
  - [Emacs Lisp](#0-200-8-sec-5-10)
  - [Extra-langs](#0-200-8-sec-5-11)
  - [Finance](#0-200-8-sec-5-12)
  - [Games](#0-200-8-sec-5-13)
  - [Go](#0-200-8-sec-5-14)
  - [Haskell](#0-200-8-sec-5-15)
  - [Html](#0-200-8-sec-5-16)
  - [IBuffer](#0-200-8-sec-5-17)
  - [IPthon-notebook](#0-200-8-sec-5-18)
  - [Ivy](#0-200-8-sec-5-19)
  - [Javascript](#0-200-8-sec-5-20)
  - [LaTeX](#0-200-8-sec-5-21)
  - [Markdown](#0-200-8-sec-5-22)
  - [Org](#0-200-8-sec-5-23)
  - [Prodigy](#0-200-8-sec-5-24)
  - [Python](#0-200-8-sec-5-25)
  - [Restclient](#0-200-8-sec-5-26)
  - [Ruby-On-Rails](#0-200-8-sec-5-27)
  - [Rust](#0-200-8-sec-5-28)
  - [Scala](#0-200-8-sec-5-29)
  - [Scheme](#0-200-8-sec-5-30)
  - [Semantic](#0-200-8-sec-5-31)
  - [Shaders](#0-200-8-sec-5-32)
  - [Spell-checking](#0-200-8-sec-5-33)
  - [Themes](#0-200-8-sec-5-34)
  - [Typescript](#0-200-8-sec-5-35)
  - [Version control](#0-200-8-sec-5-36)
  - [Ymcd](#0-200-8-sec-5-37)
- [Improvements](#0-200-8-sec-6)

# Convention changes<a name="0-200-8-sec-1"></a>

-   Update debug conventions
    -   Step in and Step out are now, `i` and `o` respectively
    -   Inspect a value is now `v`
    -   Next step is now `s`

# Dotspacemacs changes<a name="0-200-8-sec-2"></a>

-   Improve variable `dotspacemacs-line-numbers`. The variable can now take a property list with the following keywords supported: `:relative t` to turn on relative lines, `:disabled-for-modes mode1 mode2 ...` to disable line numbers in specific major modes and `:size-limit-kb n` to disable line numbers when the size of the buffer is greater than n (thanks to deb0ch)

# Core changes<a name="0-200-8-sec-3"></a>

-   Import `quela`, `package-build`, `ido-vertical-mode` and `spacemacs-theme` in `core/libs`
-   Speedup `SPC h SPC` loading.
-   Force installation of `org-contrib-plus` instead of `org` effectively avoiding to install Org twice.
-   Display some additional information message in mode-line at startup.
-   Throw an error instead of a warning if emacs version is too old (thanks to deb0ch)
-   Refactor `rotate-windows` (thanks to bmag)
-   Don’t toggle maximized window at startup if already maximized (thanks to TheBB)
-   Set default value of `dotspacemacs-enable-paste-transient-state` to nil to reflect its value in the doftile template (tanks to toupeira)
-   which-key: Update usage of replacement alists (thanks to justbur)
-   which-key: Fix transient state descriptions (thanks to justbur)
-   which-key: Implement combined select window keys (thanks to justbur)
-   Maximize frame earlier in the startup process (thanks to deb0ch)
-   Fix unbound holy-mode error (thanks to TheBB)
-   Fix error on footer insertion when window is narrow (thanks to deb0ch)
-   Fix encoding of `;` in issue report body (thanks to d12frosted)
-   Fix variable is void: system-info in spacemacs/report-issue
-   Fix delayed warning display in emacs 25.5
-   Fix computation of package installation lazyness
-   Fix false warning about duplicate layers at startup. (thanks to puzl)
-   Fix indentation rules for declare-prefix functions
-   Add support for interpreter-mode-alist to layer lazy installation
-   Add support for local elpa repositories
-   Always return \`t\` from use-package pre/post hooks. (thanks to Stebalien)
-   Jump-handers `:async` keyword can now take a predicate function
-   home buffer: update quickhelp.txt in [?] (thanks to kccai)
-   Filter out private vars in dotspacemacs/get-variable-string-list
-   Add support for go to definition in other window with `SPC m g G`
-   Scope minor-mode specific key bindings under major-mode leader

# Distribution layer changes<a name="0-200-8-sec-4"></a>

-   New key binding `SPC w +` to toggle between vertical and horizontal windows layout (thanks to nixmaniack, bmag)
-   New key binding `SPC w TAB` to go to last selected window (thanks to adelq)
-   New key binding `gf` in compilation mode to find file at point (thanks to FrancescElies)
-   New key binding `gD` to jump to definition in another window (thanks to quicknir)
-   New key binding `SPC x l S` to reverse sort lines (duianto)
-   New key bindings `SPC x l c` and `SPC x l C` to sort lines by column (duianto)
-   New key binding `SPC f T` to jump to currently opened file in `neotree` (thanks to arjun-urs)
-   New key binding `'` in `neotree` to take a quick look at the currently selected file (thanks to sdwolf)
-   Overhaul the buffer transient state on `SPC b .` (thanks to quicknir)
-   Improve `spacemacs/count-word-analysis` by including information from `count-words` function
-   Use use `winum.el` instead of `window-numbering.el` for window numbers (thanks to deb0ch)
-   Add copy key to neotree under `C` (thanks to lanejo01)
-   Move generation of tags from `SPC p C-g` to easier `SPC p G` (thanks to TheBB)
-   Add duplicate-line-or-region on `SPC x l d` (thanks to deb0ch)
-   Integrate `auto-highlight-symbol` with `evil` as well as `isearch` (thanks to TheBB)
-   Change default fringe color for centered-buffer-mode.
-   Use `helm` or `ivy` as completion framework for `dumb-jump` (thanks to deuill)
-   Hide PROPERTIES drawers in space-doc-mode (thanks to nikolaiam)
-   Disable auto-revert of `buffer-menu-mode` (thanks to bgamari)
-   Fix spacemacs/rename-current-buffer-file on non-file buffers (thanks to lislon)

# Layer changes<a name="0-200-8-sec-5"></a>

## Ansible<a name="0-200-8-sec-5-1"></a>

-   Add support for `ansible-vault` (auto-de/encryption of files)
-   Add support for `company` with `company-ansible` package

## Auto-completion<a name="0-200-8-sec-5-2"></a>

-   Add new package `fuzzy` for `auto-complete`.

## Better defaults<a name="0-200-8-sec-5-3"></a>

-   Add new package `unfill` (thanks to d12frosted)

## Chinese<a name="0-200-8-sec-5-4"></a>

-   Move `pyim` into the `.cache` directory (thanks to DCPRevere)

## Chrome<a name="0-200-8-sec-5-5"></a>

-   Add package `flymd`. Flymd is a realtime markdown preview (hodge)

## Clojure<a name="0-200-8-sec-5-6"></a>

-   Update debugger key bindings to meet new conventions
-   Add new key bindings to convert collections (thanks to benedekfazekas)
-   Fix calls to `cider-test-xxxx` functions (thanks to mahinshaw)

## Common Lisp<a name="0-200-8-sec-5-7"></a>

-   Add neew key binding `SPC m h i` to inspect a definition
-   Set jump handler to `slime-edit-definition` (thanks to phoe)

## CSharp<a name="0-200-8-sec-5-8"></a>

-   Fix Omnisharp jump handler by marking it async (thanks to razzmatazz)

## Elixir<a name="0-200-8-sec-5-9"></a>

-   Add support for `credo` (denin)
-   Prevent from inserting too many "end"s in Elixir (thanks to michalmuskala)

## Emacs Lisp<a name="0-200-8-sec-5-10"></a>

-   Fix cursor position for `eval-last-sexp`.
-   Add `SPC m e c` to evaluate current sexp. Evaluation of current `setq` or `defun` form is under `SPC m e C`.
-   Add support for `debugger` and `edebug`, see tutorial in `README.org` file.

## Extra-langs<a name="0-200-8-sec-5-11"></a>

-   Add extension `.wl` for `wolfram-mode` (kenkangxgwe)

## Finance<a name="0-200-8-sec-5-12"></a>

-   Add new key bindings for ledger account reconciliation (thanks to timjaeger)

## Games<a name="0-200-8-sec-5-13"></a>

-   Add `sudoku` game. (thanks to et2010)

## Go<a name="0-200-8-sec-5-14"></a>

-   Fix void reference to `go--position-bytes` (thanks to db47h)

## Haskell<a name="0-200-8-sec-5-15"></a>

-   Update debugger key bindings to meet new conventions

## Html<a name="0-200-8-sec-5-16"></a>

-   Defer `company-web` loading (ralesi)

## IBuffer<a name="0-200-8-sec-5-17"></a>

-   New key bindings `g r` to update buffer, `g j` to move to next filter group and `g k` to move to previous filter group (thanks to donm)

## IPthon-notebook<a name="0-200-8-sec-5-18"></a>

-   Fix `axes.color_cycle` warning in matplotlibrc (thanks to Retorz)

## Ivy<a name="0-200-8-sec-5-19"></a>

-   Rebind `SPC f b` to `counsel-bookmark` (thanks to gilbertw1)
-   Add confirmation between deleting a file with `d` (thanks to d12frosted)
-   Add C-c C-e to edit counsel-ag search results (thanks to aaronjensen)
-   Correctly close `ivy` layout transient state when pressing `b` (thanks to gilbertw1)

## Javascript<a name="0-200-8-sec-5-20"></a>

-   Fix jump handler using `tern` by marking it async (thanks to coreygrunewald)

## LaTeX<a name="0-200-8-sec-5-21"></a>

-   Add new key bindings for folding functions (thanks to nashamri)

## Markdown<a name="0-200-8-sec-5-22"></a>

-   Add new key binding `SPC m i t` to insert a Table of Contents
-   Fix activation of `mmm-mode`
-   Add support for ini files
-   Hide `MMM` linter in mode-line

## Org<a name="0-200-8-sec-5-23"></a>

-   New key binding `,` for `org-edit-src-exit` (thanks to david-sawatzke)
-   New key binding `SPC m i a` for `org-attach` (thanks to smile12341234)
-   Move `SPC m e` to `SPC m e e` for `org-export-dispatch`
-   Fix `o` on folded headings (thanks to dschoepe)

## Prodigy<a name="0-200-8-sec-5-24"></a>

-   Add new key binding `R` to refresh buffer (thanks to FrancescElies)
-   Add new key binding `gf` to go to file at point (thanks to FrancescElies)

## Python<a name="0-200-8-sec-5-25"></a>

-   New layer variable `python-auto-set-local-pyvenv-virtualenv` to autoload a virtual env with a `.venv` file (thanks to korayal)
-   Simplify python test runner setup (thanks to TheBB)
-   Fix debug string for python3 (thanks to yangguang760)
-   Fix python path with virtualenv on Windows in Python nose package (thanks to brenttaylor)
-   Fix python-enable-yapf-format-on-save (thanks to magia)

## Restclient<a name="0-200-8-sec-5-26"></a>

-   Add package `ob-restclient` to add `org-babel` support to `restclient`
-   Add helm support to jump to variable or request with `SPC m j` (thanks to tko)
-   Add autocompletion for methods and headers (thanks to tko)
-   Add key bindings for jump to next / previous query with `SPC m n` and `SPC m p` (thanks to tko)

## Ruby-On-Rails<a name="0-200-8-sec-5-27"></a>

-   Use projectile-rails-global-mode if available (thanks to asok)

## Rust<a name="0-200-8-sec-5-28"></a>

-   Add binding for describing symbol at point under `SPC m h h` (thanks to NJBS)
-   Add key binding to run current Rust file under `SPC m q` (thanks to swaroopch)
-   Make Racer respect `help-window-select` (thanks to bmag)

## Scala<a name="0-200-8-sec-5-29"></a>

-   Update debugger key bindings to meet new conventions
-   Update deprecated `ensime` variable name `user-emacs-ensime-directory` (thanks to brakhane)
-   Remove sbt-hydra rename wrapper (thanks to jdnavarro)

## Scheme<a name="0-200-8-sec-5-30"></a>

-   Fix void-variable `company-backends-scheme-mode` (thanks to pnagy)

## Semantic<a name="0-200-8-sec-5-31"></a>

-   Make Semantic fast (thanks to tudho)

## Shaders<a name="0-200-8-sec-5-32"></a>

-   Add support for `company` with `glsl-company` package (thanks to d12frosted)

## Spell-checking<a name="0-200-8-sec-5-33"></a>

-   Defer loading of `flyspell-correct-helm` and `flyspell-correct` (thanks to ralesi and d12frosted)

## Themes<a name="0-200-8-sec-5-34"></a>

-   Add sourcerer theme to themes-megapack (thanks to gilbertw1)
-   Added new base16 themes (thanks to bezhermoso and metamode)
-   Add madhat2r theme to megapack (thanks to madhat2r)

## Typescript<a name="0-200-8-sec-5-35"></a>

-   Fix eldoc initialization in typescript layer. (thanks to Stebalien)

## Version control<a name="0-200-8-sec-5-36"></a>

-   New layer variable `version-control-diff-side` to set the fringe side where to display version control info (thanks to emmanueltouzery)
-   Add a transient state for `smerge-mode` on `SPC g r` (thanks to perfectayush)

## Ymcd<a name="0-200-8-sec-5-37"></a>

-   Add ycmd-eldoc to ycmd layer (thanks to quicknir)

# Improvements<a name="0-200-8-sec-6"></a>

-   Improve home buffer responsiveness, add centering for release notes and lists (thanks to deb0ch)
-   Add keybindings to move buffers by window number with `SPC b #` where `#` is a number between 0 and 9 (thanks to quicknir)
-   Add toggle to display time in modeline on `SPC t m t`. Toggle of the modeline is now in `SPC t m T`. (thanks to jupl)
-   Add toggle for syntax highlighting on `SPC t h s` (thanks to jupl)
-   Message instead of warn on failed auto-evilify (thanks to TheBB)
-   Warn if both helm and ivy are enabled (thanks to TheBB)
-   Add new documentation file `doc/BEGINNERS_TUTORIAL.org` (nikolaiam)
-   Various documentation improvements (thanks to antonshwab, benbotwin, bmag, cyberxndr, d12frosted, duianto, erictapen, FrancescElies, idoo, jr0cket, jgertm, jumarko, jwintz, LemmingAvalanche, lpenz, Melon-Bread, mineo, nightuser, nikolaiam, primeos, rodonn, roryokane, rski, skade, smile12341234, stratosgear, Trevoke, xiaohanyu, Wiliamvdv, zetok, zhexuany)

v0.200.9  2017-04-07T03:12:47Z
------------------------------
Tag release, no description

v0.200.8  2017-04-02T05:24:36Z
------------------------------
Tag release, no description

alfredodeza/khuno.vim
=====================
A Python Flakes plugin
https://github.com/alfredodeza/khuno.vim/releases/

v1.0.2  2017-04-07T12:19:29Z
----------------------------
Tag release, no description

pypa/setuptools_scm
===================
the blessed package to manage your versions by scm tags
https://github.com/pypa/setuptools_scm/releases/

 v1.15.5 2017-04-08T16:48:32Z
-----------------------------

 v1.15.4 2017-04-08T12:39:43Z
-----------------------------

 v1.15.3 2017-04-07T21:17:01Z
-----------------------------

v1.15.5  2017-04-08T16:47:02Z
-----------------------------
Tag release, no description

v1.15.4  2017-04-08T11:43:14Z
-----------------------------
Tag release, no description

v1.15.3  2017-04-07T20:59:42Z
-----------------------------
Tag release, no description

siacs/Conversations
===================
Conversations is an open source XMPP/Jabber client for the Android platform
https://github.com/siacs/Conversations/releases/

 1.18.0 2017-04-07T09:59:17Z
----------------------------
* Conversations <1.16.0 will be unable to receive OMEMO encrypted messages
* OMEMO: put auth tag into key (verify auth tag as well)
* offer to block entire domain in message from stranger snackbar 
* treat URL as file if URL is in oob or contains key

aio-libs/aiohttp
================
Async http client/server framework (asyncio) 
https://github.com/aio-libs/aiohttp/releases/

aiohttp 2.0.6 2.0.6 2017-04-06T14:53:54Z
----------------------------------------
Changes
---------

- Fix ``web.run_app`` not to bind to default host-port pair if only socket is
  passed #1786

- Keeping blank values for `request.post()` and `multipart.form()` #1765

- TypeError in ResponseHandler.data_received #1770

inducer/pudb
============
Full-screen console debugger for Python
https://github.com/inducer/pudb/releases/

v2017.1.2  2017-04-05T22:09:38Z
-------------------------------
Tag release, no description

darktable-org/darktable
=======================
darktable is an open source photography workflow application and raw developer
https://github.com/darktable-org/darktable/releases/

darktable 2.2.4 release-2.2.4 2017-04-03T06:56:20Z
--------------------------------------------------
we're proud to announce the fourth bugfix release for the 2.2 series of darktable, 2.2.4!

as always, please don't use the autogenerated tarball provided by github, but only our tar.xz. the checksum is:

    $ sha256sum darktable-2.2.4.tar.xz
    bd5445d6b81fc3288fb07362870e24bb0b5378cacad2c6e6602e32de676bf9d8  darktable-2.2.4.tar.xz
    $ sha256sum darktable-2.2.4.dmg
    ???  darktable-2.2.4.dmg

#### Important note: to make sure that darktable can keep on supporting the raw file format for your camera, please help us by visiting https://raw.pixls.us/ and making sure that we have the full raw sample set for your camera under CC0 license!

and the changelog as compared to 2.2.3 can be found below.

## New features:

- Better brush trace handing of opacity to get better control.
- tools: Add script to purge stale thumbnails
- tools: A script to watch a folder for new images

## Bugfixes:

- DNG: fix camera name demangling. It used to report some wrong name for some cameras.
- When using wayland, prefer XWayland, because native Wayland support is not fully functional yet
- EXIF: properly handle image orientation '2' and '4' (swap them)
- OpenCL: a few fixes in profiled denoise, demosaic and colormapping
- tiling: do not process uselessly small end tiles
- masks: avoid assertion failure in early phase of path generation,
- masks: reduce risk of unwanted self-finalization of small path shapes
- Fix rare issue when expanding $() variables in import/export string
- Camera import: fix ignore_jpg setting not having an effect
- Picasa web exporter: unbreak after upstream API change
- collection: fix query string for folders ( 'a' should match 'a/b' and 'a/c', but not 'ac/' )

## Base Support:

- Fujifilm X-T20 (only uncompressed raw, at the moment)
- Fujifilm X100F (only uncompressed raw, at the moment)
- Nikon COOLPIX B700 (12bit-uncompressed)
- Olympus E-M1MarkII
- Panasonic DMC-TZ61 (4:3, 3:2, 1:1, 16:9)
- Panasonic DMC-ZS40 (4:3, 3:2, 1:1, 16:9)
- Sony ILCE-6500

## Noise Profiles:

- Canon PowerShot G7 X Mark II
- Olympus E-M1MarkII
- Lge Nexus 5X

paradoxxxzero/butterfly
=======================
A web terminal based on websocket and tornado
https://github.com/paradoxxxzero/butterfly/releases/

3.0.3  2017-04-04T16:14:27Z
---------------------------
Tag release, no description

deanmalmgren/textract
=====================
extract text from any document. no muss. no fuss.
https://github.com/deanmalmgren/textract/releases/

v1.6.0 v1.6.0 2017-04-03T08:31:31Z
----------------------------------
psv/tsv parsers, user-provided filename extensions, audio parsing with pocketsphinx, and several other bug fixes

syncthing/syncthing
===================
Open Source Continuous File Synchronization
https://github.com/syncthing/syncthing/releases/

v0.14.27-rc.2 v0.14.27-rc.2 2017-04-07T07:28:49Z
------------------------------------------------
This is a release candidate for v0.14.27.

Resolved issues since v0.14.27-rc.1

* #4082: Per remote device transfer rates should follow setting

Resolved issues since v0.14.26:

* #219: Devices can now have a list of allowed subnets (advanced config)
* #234: The transfer rate units can now be changed by clicking on the value
* #1819: UI text explaining "Introducer" is improved
* #2267: Advanced config editor can now edit lists of things
* #2519: Directories created for new folders now obey the user umask setting (on Unixes)
* #3608: Ignore patterns can now be edited at folder creation time
* #4053: Incoming index updates are consistency checked better

v0.14.27-rc.1 v0.14.27-rc.1 2017-04-06T07:49:09Z
------------------------------------------------
This is a release candidate for v0.14.27.

Resolved issues since v0.14.26:

* #219: Devices can now have a list of allowed subnets (advanced config)
* #234: The transfer rate units can now be changed by clicking on the value
* #1819: UI text explaining "Introducer" is improved
* #2267: Advanced config editor can now edit lists of things
* #2519: Directories created for new folders now obey the user umask setting (on Unixes)
* #3608: Ignore patterns can now be edited at folder creation time
* #4053: Incoming index updates are consistency checked better

v0.14.26 v0.14.26 2017-04-04T05:59:38Z
--------------------------------------
This is a regularly scheduled stable release.

Resolved issues since v0.14.25:

* #4035: Symlinks are now properly ignored on Windows.
* #2344: Discovery errors are more clearly displayed in the GUI.
* #3913: The language dropdown menu in the GUI is now correctly sorted.

Also:

* When there are items that could not be synced, their full path is displayed in the GUI.

davidhalter/jedi
================
Awesome autocompletion and static analysis library for python.
https://github.com/davidhalter/jedi/releases/

v0.10.2  2017-04-05T18:00:16Z
-----------------------------
Tag release, no description

v0.10.1  2017-04-04T23:06:48Z
-----------------------------
Tag release, no description

fullcalendar/fullcalendar
=========================
Full-sized drag & drop event calendar (jQuery plugin)
https://github.com/fullcalendar/fullcalendar/releases/

 v3.3.1 2017-04-01T17:11:40Z
----------------------------
Bugfixes:
- stale calendar title when navigate away from then back to the a view (#3604)
- js error when gotoDate immediately after calendar initialization (#3598)
- agenda view scrollbars causes misalignment in jquery 3.2.1 (#3612)
- navigation bug when trying to navigate to a day of another week (#3610)
- dateIncrement not working when duration and dateIncrement have different units

v3.3.1  2017-04-01T16:48:27Z
----------------------------
Tag release, no description
