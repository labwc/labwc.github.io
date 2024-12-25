# Integration

1. [Introduction](#introduction)
2. [Panels](#panels)
    1. [waybar](#waybar)
    2. [sfwbar](#sfwbar)
    3. [xfce4-panel](#xfce4panel)
    4. [yambar](#yambar)
    5. [lxqt-panel](#lxqt-panel)
3. [Menu Generators](#menu-generators)
4. [CSD](#csd)
5. [Output Management](#output-management)
6. [Screenshots](#screenshots)
7. [Session Lock](#session-lock)
8. [Desktops](#desktops)
9. [Qt](#qt)
10. [Clipboard](#clipboard)
11. [Input Method](#input-method)
12. [GTK](#gtk)

# 1. Introduction {#introduction}

This document describes how clients (not part of the labwc project) can be used
with labwc to create a Desktop Environment. It does not attempt to describe in
detail how to setup and use those other clients, but merely sign-posts to them
and gives some simple hints to get started.

There are two protocols in particularly that are fundamental in integrating
desktop components and that will be referred to through this document namely:
[`wlr-layer-shell`] and [`wlr-foreign-toplevel-management`].

[`wlr-layer-shell`] allows surfaces to be assigned to a "layer" with a defined
z-depth and also to be anchored to the edges/corners of a screen.

[`wlr-foreign-toplevel-management`] provides clients such as taskbars and docks
with a list of opened applications and supports requests for certain actions
such as maximizing, etc.

At the time of writing some common toolkits do not have full support for
[`wlr-layer-shell`], most notably `GTK4` and `Qt <6.5`. In order to integrate
components written in these eco-systems in the short/medium term, window
rules can be used to achieve a reasonable setup. Please note though that the
use of window-rules is a sub-optimal solution which relies on user
configuration and does not always support per-output configuration.

[`wlr-layer-shell`]: https://wayland.app/protocols/wlr-layer-shell-unstable-v1
[`wlr-foreign-toplevel-management`]: https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1

# 2. Panels {#panels}

There are a variety of wayland panels available for __labwc__ ranging
from simple to complex. Below are some that you can try.

Most panels are started from the `~/.config/labwc/autostart` file like so:

```
mypanel >/dev/null 2>&1 &
```

See the [autostart] documentation for further information.

[autostart]: https://github.com/labwc/labwc/blob/master/docs/autostart

## 2.1 waybar {#waybar}

[waybar repository]

Add these two sections to enable a taskbar through the toplevel-foreign 
protocol to the `~/.config/waybar/config` file:

```
"modules-left": ["wlr/taskbar"],
```

```
    "wlr/taskbar": {
        "format": "{app_id}",
        "on-click": "minimize-raise",
    },
```

See the [waybar documentation] for further information.

## 2.2 sfwbar {#sfwbar}

[sfwbar repository]

Configure sfwbar in the `~/.config/sfwbar/sfwbar.config` file. 

The default config will mostly work however for more information see the
[sfwbar man page].

[sfwbar/config] contains example config files (with file extension `.config`)
which can be used by merely copying them to `~/.config/sfwbar/sfwbar.config`.

See example configuration [here](obligatory-screenshot.html#panel).

[sfwbar repository]: https://github.com/LBCrion/sfwbar
[sfwbar man page]: https://github.com/LBCrion/sfwbar/blob/main/doc/sfwbar.rst
[sfwbar/config]: https://github.com/LBCrion/sfwbar/tree/main/config

## 2.3 xfce4-panel {#xfce4panel}

[xfce4-panel repository]

Just after the release of Xfce 4.18 in Dec 2022, Wayland support was added
([MR103]) to [xfce4-panel] including the layer-shell and
foreign-toplevel-management protocols.

For the time being it is best to force all plugins to run as internal:

`xfconf-query -c xfce4-panel -p /force-all-internal -t bool -s true --create`

Until the next release, you can get it going by cloning the master branch and
building with the following (adjusting prefix to suit your system of course):

```
./autogen --prefix=/usr
make
make install
```

On Arch Linux you can simply install the following packages: [xfce4-dev-tools],
[libxfce4util], [libxfce4ui], [libxfce4windowing-devel] and [xfce4-panel-git].

[MR103]: https://gitlab.xfce.org/xfce/xfce4-panel/-/merge_requests/103
[xfce4-panel]: https://docs.xfce.org/xfce/xfce4-panel/start

[xfce4-dev-tools]: https://archlinux.org/packages/extra/x86_64/xfce4-dev-tools/
[libxfce4util]: https://archlinux.org/packages/extra/x86_64/libxfce4util/
[libxfce4ui]: https://archlinux.org/packages/extra/x86_64/libxfce4ui/
[libxfce4windowing-devel]: https://aur.archlinux.org/packages/libxfce4windowing-devel
[xfce4-panel-git]: https://aur.archlinux.org/packages/xfce4-panel-git

## 2.4 yambar {#yambar}

[yambar repository]

Configure yambar in the `~/.config/yambar/config.yml`. Yambar configuration
uses the [`yaml` language].

Read the [yambar documentation] for further information.

## 2.5 lxqt-panel {#lxqt-panel}

Since version `2.0.0`, `lxqt-panel` supports the [`wlr-layer-shell`] protocol
and thus runs natively under Wayland without window rules. Should you have an
older version, it can still be used with a window rule such as:

```
<windowRules>
  <windowRule identifier="lxqt-panel" matchOnce="true" fixedPosition="yes">
    <skipTaskbar>yes</skipTaskbar>
    <action name="MoveTo" x="0" y="0" />
    <action name="ToggleAlwaysOnTop"/>
  </windowRule>
</windowRules>
```

Note: `lxqt-panel` does not support [`wlr-foreign-toplevel-management`] so the
taskbar does not work.

# 3. Menu Generators {#menu-generators}

Several menu-generators exist to automatically create a menu.xml with system
applications:

- [labwc-menu-generator]\: Independent of Desktop Environments and associated
  menu-packages. Very easy to build and use. Written in C.
- [labwc-menu-gnome3]\: Depends on GTK and a menu package such as gnome, mate and
  cinnamon. Written in C.
- [obmenu-generator]\: Popular with openbox communities. Written in Perl.
- [openbox-menu]\: XDG menu spec compliant, using LXDE's library and menu
  package. Used to be packaged by debian, but isn't anymore. Though the Github 
  repos has been frozen, as of November 2024 it works once compiled. Written in C.
- [arch-xdg-menu]\: Arch Linux's xdg-menu package based on SuSE 2003
  implementation. Written in Perl.
- [obamenu]\: Designed for pipemenus, but could easily be modified to produce
  a root-menu. Written in python3.

They are typically used like this:

```
labwc-menu-generator > ~/.config/labwc/menu.xml
```

Some of them support several menu formats, in which case you have to specify
`openbox` format.

# 4. Client Side Decoration (CSD) {#csd}

## 4.1 `gsettings` {#gsettings}

Labwc is designed to use Server Side Decoration (SSD) for windows, but does
support CSD. If you prefer to use CSD or use GTK applications which will not
surrender their CSD, such as nautilus, you may wish to manage some CSD
properties using gsettings and associated [gsettings-desktop-schemas].

For example, to display minimize, maximize and close buttons, rather than
just the default close, issue the following command:

```
gsettings set org.gnome.desktop.wm.preferences button-layout ":minimize,maximize,close"
```

To also show a client-menu button, run this command:

```
gsettings set org.gnome.desktop.wm.preferences button-layout "menu:minimize,maximize,close"
```

[gsettings-desktop-schemas]: https://github.com/GNOME/gsettings-desktop-schemas

## 4.2 Firefox {#firefox}

Firefox prefers CSD by default. In order to disable CSD, take the following steps:

- `Settings` -> `More Tools` -> `Customize toolbar` -> `Title Bar` checkbox (bottom left corner)

# 5. Output Management {#output-management}

To most users the term 'output' refers to the physical display(s) used.

A good starting point for managing wayland outputs is to use [wlr-randr]
which is tool similar to [xrandr] for X11.

Use [wlr-randr] to get your output names and associated properties such as
mode, position, scale and transform by simply running:

```
wlr-randr
```

There is not configuration file for [wlr-randr], but you can use to configure
outputs from the command line like this:

```
wlr-randr --output DP-1 --mode 1920x1080@144.001007Hz
```

> Note: Use all the frequency (Hz) decimals when specifying a mode

If you prefer to have display (output) configuration automatically selected,
try [kanshi] which supports directive definitions (in `~/.config/kanshi/config`)
like this:

```
profile {
  output HDMI-A-1 position 1366,0
  output eDP-1 position 0,0
}
```

[kanshi]: https://sr.ht/~emersion/kanshi/
[xrandr]: https://wiki.archlinux.org/title/xrandr

# 6. Screenshots {#screenshots}

Screenshots can be taken using the `wlr-screencopy` protocol via applications
such as [grim](https://git.sr.ht/~emersion/grim).

Grim is a commandline tool which can be combined with other clients, for
example

- [slurp](https://github.com/emersion/slurp)
- [wl-copy](https://github.com/bugaevc/wl-clipboard)
- [swappy](https://github.com/jtheoof/swappy)

```
grim -g "$(slurp)" - | swappy -f -
grim - | wl-copy
```

# 7. Session Lock {#session-lock}

`labwc` supports the [ext-session-lock] and [ext-idle-notify] protocols and you can use clients such
as `swaylock` to lock your session.

It is common to want to lock the session/screen after a period of inactivity.
This can be achieved by using `swayidle` as follows:

```
swayidle -w \
	timeout 300 'swaylock -f -c 000000' \
	timeout 600 'wlopm --off \*' \
	resume 'wlopm --on \*' \
	before-sleep 'swaylock -f -c 000000' >/dev/null 2>&1 &
```

Note that in the context of idle system power management, it is *NOT* a good
idea to turn off displays by 'disabling outputs' for example by `wlr-randr
--output <whatever> --off` because this re-arranges views. Instead use a
wlr-output-power-management client such as [wlopm]

[chayang] is a small Wayland client which gradually dims the screen. This is
useful for setting up a grace period before turning off the screens. You can
use it with swayidle by changing the timeout arguments to:

`'chayang && swaylock -f'`

[chayang]: https://git.sr.ht/~emersion/chayang
[wlopm]: https://git.sr.ht/~leon_plickat/wlopm
[ext-idle-notify]: https://wayland.app/protocols/ext-idle-notify-v1
[ext-session-lock]: https://wayland.app/protocols/ext-session-lock-v1

# 8. Desktops {#desktops}

## LXQt

Since version `2.0.0`, `pcmanfm-qt --desktop` supports the [`wlr-layer-shell`]
protocol, and thus runs natively without window-rules.

Older version can be run with the rule below in `rc.xml`:

```
<windowRules>
  <windowRule title="pcmanfm-desktop*">
    <skipTaskbar>yes</skipTaskbar>
    <skipWindowSwitcher>yes</skipWindowSwitcher>
    <action name="MoveTo" x="0" y="0" />
    <action name="ToggleAlwaysOnBottom"/>
  </windowRule>
</windowRules>
```

Also, consider tweaking the following in Desktop Preferences:

- General - Margin of Work Area
- Background - Individual wallpaper for each monitor

## Conky

Conky, starting with version 1.19.6, has the ability to run as a true Wayland
application. Not all of the functionality of the X11 version is available,
notably the ability to use lua as it's X11 based. It uses waylands layer
shell, and by default shows across all workspaces. Config file should have
something like this:

```
out_to_x = false,
out_to_wayland = true,
```

# 9. Qt {#qt}

To run Qt applications on Wayland it may be necessary to install a specific
`qt6-wayland` package from the distribution repositories. For examples
on Arch Linux, install [qt6-wayland].

You may use [qt6ct] to configure Qt6 settings such as theme, font and icons;
and set `QT_QPA_PLATFORMTHEME=qt6ct` in `~/.config/labwc/environment`.

[qt6-wayland]: https://archlinux.org/packages/extra/x86_64/qt6-wayland/
[qt6ct]: https://github.com/trialuser02/qt6ct

# 10. Clipboard {#clipboard}

**Labwc** does not store clipboard contents after an application quits.
For this functionality you need a _clipboard manager_.

For example, you could add a line similar to this to
`~/.config/labwc/autostart`:

```
wl-paste --watch cliphist store &
```

This uses [cliphist] and [wl-clipboard]. Other clipboard managers include
[clapboard] and [clipse].

Many clipboard managers have features beyond just keeping the clipboard
alive. See the documentation of the individual tools for further information.

# 11. Input Method {#input-method}

Input methods like Fcitx5 and IBus provide modules for GTK and Qt and an
interface for xserver (xwayland) using D-Bus without wayland protocols.

You can enable input method for those platforms by setting environment
variables like this:

```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

<!-- TODO: remove "in the master branch" when labwc 0.7.2 is released -->
For apps not running on those platforms (e.g. Alacritty), labwc supports
the following wayland protocols in the master branch:

- [text-input-v3]
  - Used by winit apps (e.g. Alacritty) and GTK (without setting
    `GTK_IM_MODULE` environment variable).
- [input-method-v2]
  - Supported by Fcitx5, but not by IBus yet
    ([issue](https://github.com/ibus/ibus/issues/2182)).

Here is a quick guide for using Fcitx5 in labwc:

1. Install fcitx5, GTK/Qt modules, configtool and language-specific module.
    - Arch Linux: `pacman -S fcitx5-im fcitx5-mozc`
    - Ubuntu: `apt install fcitx5 fcitx5-mozc`

    Replace `fcitx5-mozc` with a module for your language.

2. Set `GTK_IM_MODULE`, `QT_IM_MODULE` and `XMODIFIERS` like described earlier.
These are usually saved in files like `~/.config/labwc/environment`,
`~/.profile` and `/etc/environment`.

3. Start `fcitx5`. You can automatically start fcitx5 by adding `fcitx5 &` to
`~/.config/labwc/autostart`.

4. Configure Fcitx5 with configtool to enable the installed language-specific
module and to set up hotkeys. See [Configtool (Fcitx 5) - Fcitx].

5. Activate input method with hotkeys while typing in applications.

<!--- TODO: remove this once Chromium supports text-input-v3 -->
## Input method on Chromium

Chromium (and Electron-based) apps don't support the [text-input-v3] protocol
[at this point](https://chromium-review.googlesource.com/c/chromium/src/+/3750452).
So if you want to use IME with Chromium under labwc, you have following options:

1. Run Chromium under XWayland

    This is the default option. However, some features like touchpad gesture
    don't work.

2. Use GTK IM Module

    By running Chromium with `--enable-features=UseOzonePlatform --ozone-platform=wayland --gtk-version=4`,
    you can enable IME with GTK IM Module (selected by `GTK_IM_MODULE`) under
    wayland. However, IME popups might be incorrectly positioned.

3. Patch labwc and use [text-input-v1] protocol

    Since [text-input-v1] is an outdated protocol, labwc doesn't officially
    support it. However, you can optionally add support for it by installing
    labwc from the [unofficial AUR](https://aur.archlinux.org/packages/labwc-im)
    or by applying its patch. Then, you can enable IME with [text-input-v1] by
    running Chromium with `--enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime`.

# 12. GTK {#gtk}

In some recent GTK (>=4.16) applications (e.g. Gnome's Simple-Scan and Clapper)
the File Chooser defaults to using xdg-portal technology which may not work
depending on your system setup. There are at least two ways to fallback to a
'normal' File Chooser:

1. Set the environment variable `GDK_DEBUG=no-portals` (in for example
   `$HOME/.config/labwc/environment`)
2. Create a portal configuration file in the current user home based on
   [labwc-portals.conf] and add the line `org.freedesktop.impl.portal.FileChooser=none`
   to it. The location of this file should typically be
   `$HOME/.config/xdg-desktop-portal/` but please see [portal-user-home] for
   further details.

[labwc-portals.conf]: https://github.com/labwc/labwc/blob/master/data/labwc-portals.conf
[portal-user-home]: https://flatpak.github.io/xdg-desktop-portal/docs/portals.conf.html

[text-input-v3]: https://wayland.app/protocols/text-input-unstable-v3
[input-method-v2]: https://wayland.app/protocols/input-method-unstable-v2
[Configtool (Fcitx 5) - Fcitx]: https://fcitx-im.org/wiki/Configtool_(Fcitx_5)
[text-input-v1]: https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/unstable/text-input/text-input-unstable-v1.xml

[waybar repository]: https://github.com/Alexays/Waybar
[waybar documentation]: https://github.com/Alexays/Waybar/tree/master/man
[xfce4-panel repository]: https://gitlab.xfce.org/xfce/xfce4-panel
[yambar repository]: https://codeberg.org/dnkl/yambar
[`yaml` language]: https://yaml.org
[yambar documentation]: https://codeberg.org/dnkl/yambar/src/branch/master/doc
[labwc-menu-generator]: https://github.com/labwc/labwc-menu-generator
[labwc-menu-gnome3]: https://github.com/labwc/labwc-menu-gnome3
[obmenu-generator]: https://trizenx.blogspot.com/2012/02/obmenu-generator.html
[openbox-menu]: https://github.com/fabriceT/openbox-menu
[arch-xdg-menu]: https://arch.p5n.pp.ru/~sergej/dl/2018/
[obamenu]: https://github.com/onuronsekiz/obamenu
[wlr-randr]: https://sr.ht/~emersion/wlr-randr/
[cliphist]: https://github.com/sentriz/cliphist
[clapboard]: https://github.com/bjesus/clapboard
[clipse]: https://github.com/savedra1/clipse
[wl-clipboard]: https://github.com/bugaevc/wl-clipboard
