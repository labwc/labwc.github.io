### Installing the XOrg XWayland Patch

#### ArchLinux

You can install the
[xorg-xwayland-hidpi-xprop](https://aur.archlinux.org/packages/xorg-xwayland-hidpi-xprop)
package from AUR.

#### Other distros

You will need to patch xorg-xwayland yourself, and then compile it. Depending on
your distro, there might be a package out there so you don't have to recompile,
but compiling xorg-xwayland is pretty fast. The steps should be as follows:

1. Find out what version of xorg-server you have installed.
2. If it's 23.1.1 (or similar), [download the patch from
AUR](https://aur.archlinux.org/cgit/aur.git/tree/hidpi.patch?h=xorg-xwayland-hidpi-xprop).
3. Apply the patch - `patch -Np1 -i hidpi.patch`
4. Build xorg-xwayland as you normally would.

### Installing the Wlroots Patch

#### ArchLinux

You can install the
[wlroots-hidpi-xprop-git](https://aur.archlinux.org/packages/wlroots-hidpi-xprop-git)
package from AUR.

> NOTE: If you wish, you can compile labwc with wlroots as a subproject, with
> the patch applied. This makes it easier to try the scaling without having to
> install the `wlroots-hidpi-xprop-git` AUR package globally. See below for
> details on how to do this.

#### Other distros

You can [compile
wlroots](https://gitlab.freedesktop.org/wlroots/wlroots#building) as you
normally would:

1. `git clone https://gitlab.freedesktop.org/wlroots/wlroots.git`
2. `cd wlroots`
3. Revert
[18595000f3a21502fd60bf213122859cc348f9af](https://gitlab.freedesktop.org/wlroots/wlroots/-/commit/18595000f3a21502fd60bf213122859cc348f9af),
as it can cause issues with certain XWayland apps: `git revert -n
18595000f3a21502fd60bf213122859cc348f9af`
4. `meson setup build/`
5. `ninja -C build/`
6. To install it globally: `sudo ninja -C build/ install`

#### As a subproject in labwc

A convenient way to test scaling without installing the patched version of
wlroots globally is to compile labwc with wlroots as a subproject. This does
require compiling Labwc with an [in-progress Pull
Request](https://github.com/labwc/labwc/pull/626) which adds support for wlroots
0.17.

You can compile labwc with wlroots as a subproject as follows:

1. `git clone https://github.com/labwc/labwc --branch=master`
2. `cd labwc`
3. Download the `wlroots-0.17` patch, and apply it:

```sh
wget https://patch-diff.githubusercontent.com/raw/labwc/labwc/pull/626.patch patch -p1 < 626.patch
```

4. Download the required wlroots patches:

```sh
mkdir subprojects/packagefiles
wget https://raw.githubusercontent.com/joshuataylor/wlroots-hidpi-xprop-git/8f14904f40f22b5ad247f022de21875c5a4d1050/0001-xwayland-support-HiDPI-scale.patch -P subprojects/packagefiles
wget https://raw.githubusercontent.com/joshuataylor/wlroots-hidpi-xprop-git/8f14904f40f22b5ad247f022de21875c5a4d1050/0002-Fix-configure_notify-event.patch -P subprojects/packagefiles
```

5. If you are using Meson 0.63 or above, you can use the
[diff_files](https://mesonbuild.com/Wrap-dependency-system-manual.html#diff-files)
feature to apply this patch for you, and keep the subproject up to date. If you
are using an older version of Meson, you will have to apply the patch manually,
and update it when you want to update the subproject.

To find out which version of Meson you are using, run `meson --version`.

Meson 0.63 and above: Add the following to the `subprojects/wrap/wlroots.wrap`
file, as the last option in `[wrap-git]`:

```sh
diff_files = 0001-xwayland-support-HiDPI-scale.patch 0002-Fix-configure_notify-event.patch
```

Meson 0.62 and below, follow the steps until step 6, where you will need to
apply the patch manually.

6. Delete the current `build` directory, and subprojects/wlroots directory:

```sh
rm -rf build
rm -rf subprojects/wlroots
```

7. Run `meson setup`, forcing the fallback for wlroots:

```sh
meson setup build --force-fallback-for=wlroots
```

> If you are using Meson 0.63 or above, you can skip this next step, as the
> patch will be applied automatically.

7a. If you are on Meson 0.62 and below, you will need to apply the patch
manually:

```sh
cd subprojects/wlroots
patch -p1 < ../packagefiles/0001-xwayland-support-HiDPI-scale.patch
patch -p1 < ../packagefiles/0002-Fix-configure_notify-event.patch
```

8. Configure meson with a directory prefix (replacing the below with your own
directory):

```sh
meson configure build -Dprefix=/opt/labwc/hidpi
```

9. Compile:

```sh
meson compile -C build
```

10. Install:

```sh
sudo meson install --skip-subprojects -C ./build
```

`--skip-subprojects` prevents installing the wlroots headers.

