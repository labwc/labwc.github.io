# Integration

1. [Panels](#panels)
    1. [waybar](#waybar)
    2. [sfwbar](#sfwbar)
2. [Menu Generators](#menu-generators)
3. [CSD](#csd)
4. [Output Management](#output-management)
5. [Screenshots](#screenshots)

# 1. Panels {#panels}

## 1.1 waybar {#waybar}

Add these two sections to enable a taskbar through the toplevel-foreign protocol:

```
"modules-left": ["wlr/taskbar"],
```

```
    "wlr/taskbar": {
        "format": "{app_id}",
        "on-click": "minimize-raise",
    }
```

## 1.2 sfwbar {#sfwbar}

Configure sfwbar in `~/.config/sfwbar/sfwbar.config`

Add this to `~/.config/labwc/autostart` file:

```
sfwbar &
```

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
