# Integration

1. [Panels](#panels)
    1. [waybar](#waybar)
    2. [sfwbar](#sfwbar)
    3. [xfce4-panel](#xfce4panel)
    4. [yambar](#yambar)
2. [Menu Generators](#menu-generators)
3. [CSD](#csd)
4. [Output Management](#output-management)
5. [Screenshots](#screenshots)

# 1. Panels {#panels}

There are a variety of wayland panels available for __labwc__ ranging
from simple to complex. Below are some that you can try.

Most panels are started from the `~/.config/labwc/autostart` file like so:

```
mypanel >/dev/null 2>&1 &
```

See the [autostart] documentation for further information.

## 1.1 waybar {#waybar}

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
    }
```

See the [waybar documentation] for further information.

## 1.2 sfwbar {#sfwbar}

[sfwbar repository]

Configure sfwbar in the `~/.config/sfwbar/sfwbar.config` file. 

The default config will mostly work however for more information see the
[sfwbar man page].

## 1.3 xfce4-panel {#xfce4panel}

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

## 1.3 yambar {#yambar}

[yambar repository]

Configure yambar in the `~/.config/yambar/config.yml`. Yambar configuration
uses the [`yaml` language].

Read the [yambar documentation] for further information.

# 2. Menu Generators {#menu-generators}

Several menu-generators exist to automatically create a menu.xml with system
applications:

| Name                   | Language | Comment
| ---------------------- | ---------| -------
| [labwc-menu-generator] | C        | Indepedent of menu-packages. Very easy to build and use.
| [labwc-menu-gnome3]    | C        | Depends on GTK and a menu package such as gnome, mate, cinnamon
| [obmenu-generator]     | Perl     | Popular with openbox communities
| [openbox-menu]         | C        | XDG menu spec compliant, using LXDE's library and menu package. Used to be packaged by debian, but isn't anymore.
| [arch-xdg-menu]        | Perl     | Arch Linux's xdg-menu package based on SuSE 2003 implementation
| [obamenu]              | python3  | Designed for pipemenus, but could easily be modified to produce a root-menu

They are typically used like this:

```
labwc-menu-generator > ~/.config/labwc/menu.xml
```

Some of them support several menu formats, in which case you have to specify
`openbox` format.

# 3. Client Side Decoration (CSD) {#csd}

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

# 4. Output Management {#output-management}

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

> Note: Use all the frequncy (Hz) decimals when specifying a mode

If you prefer to have display (output) configuration automatically selected,
try [kanshi] which supports directive definitions (in `~/.config/kanshi/config`)
like this:

```
profile {
  output HDMI-A-1 position 1366,0
  output eDP-1 position 0,0
}
```

# 5. Screenshots {#screenshots}

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

[autostart]: https://github.com/labwc/labwc/blob/master/docs/autostart
[waybar repository]: https://github.com/Alexays/Waybar
[waybar documentation]: https://github.com/Alexays/Waybar/tree/master/man
[sfwbar repository]: https://github.com/LBCrion/sfwbar
[sfwbar man page]: https://github.com/LBCrion/sfwbar/blob/main/doc/sfwbar.rst
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

[gsettings-desktop-schemas]: https://github.com/GNOME/gsettings-desktop-schemas

[kanshi]: https://sr.ht/~emersion/kanshi/
[wlr-randr]: https://sr.ht/~emersion/wlr-randr/
[xrandr]: https://wiki.archlinux.org/title/xrandr
