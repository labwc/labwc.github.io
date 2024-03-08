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

`lxqt-panel` does not support [`wlr-layer-shell`] and
[`wlr-foreign-toplevel-management`] but can be run with the following window
rules.

```
<windowRules>
  <windowRule identifier="lxqt-panel" matchOnce="true" fixedPosition="yes">
    <skipTaskbar>yes</skipTaskbar>
    <action name="MoveTo" x="0" y="0" />
    <action name="ToggleAlwaysOnTop"/>
  </windowRule>
</windowRules>
```

# 3. Menu Generators {#menu-generators}

Several menu-generators exist to automatically create a menu.xml with system
applications:

- [labwc-menu-generator]\: Independent of Desktop Environments and associated
  menu-packages. Very easy to build and use. Written in C.
- [labwc-menu-gnome3]\: Depends on GTK and a menu package such as gnome, mate and
  cinnamon. Written in C.
- [obmenu-generator]\: Popular with openbox communities. Written in Perl.
- [openbox-menu]\: XDG menu spec compliant, using LXDE's library and menu
  package. Used to be packaged by debian, but isn't anymore. Written in C.
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

`labwc` supports the [ext-session-lock] and [kde-idle] protocols and you can use clients such
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
[kde-idle]: https://wayland.app/protocols/kde-idle

# 8. Desktops {#desktops}

`pcmanfm-qt --desktop` does not support the wlr-layer-shell protocol, but can
be used with the following window-rule in `rc.xml`:

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

# 9. Qt {#qt}

To run Qt applications on Wayland it may be necessary to install a specific
`qt6-wayland` package from the distribution repositories. For examples
on Arch Linux, install [qt6-wayland].

You may use [qt6ct] to configure Qt6 settings such as theme, font and icons;
and set `QT_QPA_PLATFORMTHEME=qt6ct` in `~/.config/labwc/environment`.

[qt6-wayland]: https://archlinux.org/packages/extra/x86_64/qt6-wayland/
[qt6ct]: https://github.com/trialuser02/qt6ct
[waybar repository]: https://github.com/Alexays/Waybar
[waybar documentation]: https://github.com/Alexays/Waybar/tree/master/man
[xfce4-panel repository]: https://gitlab.xfce.org/xfce/xfce4-panel
[yambar repository]: https://codeberg.org/dnkl/yambar
[`yaml` language]: https://yaml.org
[yambar documentation]: https://codeberg.org/dnkl/yambar/src/branch/master/doc
[labwc-menu-generator]: https://github.com/labwc/labwc-menu-generator
[labwc-menu-gnome3]: https://github.com/labwc/labwc-menu-gnome3
[obmenu-generator]: https://trizenx.blogspot.com/2012/02/obmenu-generator.html
[openbox-menu]: http://fabrice.thiroux.free.fr/openbox-menu_en.html
[arch-xdg-menu]: https://arch.p5n.pp.ru/~sergej/dl/2018/
[obamenu]: https://github.com/onuronsekiz/obamenu
[wlr-randr]: https://sr.ht/~emersion/wlr-randr/
