# HiDPI Scaling

1. [Introduction](#introduction)
2. [Scaling](#scaling)
3. [Wayland Applications](#wayland-applications)
4. [XWayland Applications](#xwayland-applications)
5. [Troubleshooting](troubleshooting)

## Introduction

`HiDPI` refers to monitors with high pixels density, such as 4k monitors or
laptops with a high resolution display. On Apple laptops, they are called
Retina displays.

`Pixels density` is the number pixels per unit length and is commonly measured
in Dots Per Inch (DPI).

`Resolution` is the actual pixel size of the monitor, for example 1920x1080.

You can usually tell if you have a HiDPI display by looking at the resolution.
If it's 1920x1080 or 2560x1440, then you don't have a HiDPI display. If it's
3840x2160 or 5120x2880, then you have a HiDPI display. You can also have a high
DPI situation on lower resolutions if the screen is small, e.g. on notebooks,
tablets or phones.

When running Labwc, if the text is tiny, then you probably have a HiDPI display.

This documentation page guides you through setting up HiDPI scaling in Wayland
for the Labwc compositor. An intermediate level of understanding of labwc and
XServer is will be helpful for some of the steps.

A highly recommended resource for further reading is the
[ArchWiki page about HiDPI].

[ArchWiki page about HiDPI]: https://wiki.archlinux.org/title/HiDPI

## Scaling

Labwc supports scaling, which will make Wayland native apps look fantastic.

Wayland has a [fractional-scale-v1] protocol, which is supported by `wlroots`
since version `v0.17` and `labwc` has nearly implemented. Be aware though that
it is still work in progress on XServer and with many applications.

To determine the best scaling setting for your monitor, use [wlr-randr], which
allows you to see your output, current resolution, scale, refresh rate, etc.

Example output:

```sh
eDP-1 "XXX XXX (eDP-1)"
  Physical size: 286x179 mm
  Enabled: yes
  Modes:
    2560x1600 px, 60.000000 Hz (preferred, current)
  Position: 0,0
  Transform: normal
  Scale: 1.000000
  Adaptive Sync: disabled
```

The first section of the `wlr-randr` command is the name of the output
(`eDP-1`), the second section is the name of the monitor. The `Scale` is the
part to take note of for now, as this is the scale of the output. The modes are
a list of resolutions that your supports, and the default.

So to start testing the scale with `wlr-randr`, you can run the following
command, replacing `eDP-1` with the name of your output:

```sh
wlr-randr --output eDP-1 --scale 1.2
```

The base scale is 1.0. So 1.2 means 20% larger than the base scale. You might
need to reopen applications for them to pick up the new scale, as they might
look blurry until you do.

> Tip: To test GTK3 & GTK4 apps, use the `gtk3-demo` and `gtk4-demo` apps, which
> allow you to see how GTK apps look at different scales.

The exact scale that works well for you will depend on your monitor, eye sight,
and personal preference. I (@joshuataylor - the original author of this
document) found that 1.35 works well on a 32" 4k monitor, whereas on a laptop
with a 2560x1600 display 1.25 was suitable. Play with the settings until you
find what works best for you.

Other Operating Systems that support scaling usually start at 150% (1.5), such
as MacOS for their laptops, and Windows recommends 150% (1.5) for 4k monitors as
well.

If you have multiple monitors, a great app to manage scale configuration is
[kanshi], as it also allows you to set the resolution, position, rotation, etc.
of your monitors. It allows you to also set up profiles, so if you have a
laptop and an external monitor, you can set up a profile for each. It's also
handy for a single monitor.

You can create a profile in `~/.config/kanshi/config`, which might look like
this (replace `DP-1` with the name of your output, etc):

[fractional-scale-v1]: https://wayland.app/protocols/fractional-scale-v1
[wlr-randr]: https://sr.ht/~emersion/wlr-randr/
[kanshi]: https://sr.ht/~emersion/kanshi/

```conf
profile {
  output DP-1
  mode 3840x2160@143.9629972Hz
  position 0,0
  scale 1.35
}
```

To make kanshi settings permanent, add a kanshi entry in
`~/.config/labwc/autostart`.

If you change the kanshi config file on a runnnig system, you can trigger a
re-load with `killall -s SIGHUP kanshi`.

## Wayland Applications

Wayland applications are clients which run natively in Wayland, basically not
through [XWayland].  Most apps now support Wayland, with the main exception
being Java.

If you use [Jetbrains Products] such as IntelliJ, CLion, PyCharm, Datagrip,
Rubymine, Goland, Rider, Webstorm or PHPStorm, you're going to have blurry text,
as XWayland does not yet scale properly.

> Sidenote, work is being done in "Project Wakefield" for native Java on Wayland
> [0](https://wiki.openjdk.org/display/wakefield/Work+breakdown),
> [1](https://github.com/openjdk/wakefield/tree/pure_wl_toolkit).

[XWayland]: https://wayland.freedesktop.org/xserver.html
[Jetbrains Products]: https://www.jetbrains.com

You can see which apps use XWayland by using `xlsclients`, which on ArchLinux
is part of the [xorg-xlsclients] package; or by simply using alt-tab and
looking at the first column: `xdg-shell` means wayland native and `xwayland`
means XWayland.

[xorg-xlsclients]: https://archlinux.org/packages/extra/x86_64/xorg-xlsclients/

You can find more information about Wayland on the [Archwiki page about Wayland]
and more information about XWayland [on the Archwiki page].

[Archwiki page about Wayland]: https://wiki.archlinux.org/title/wayland
[on the Archwiki page]: https://wiki.archlinux.org/title/wayland#XWayland

## XWayland Applications

XWayland does not support scaling, and as such, you will have blurry text when
using XWayland apps.

There is ongoing work in xserver to support HiDPI, see [MR #733]. This has
ended up being very contentious topic, as there have been multiple Merge
Requests to add HiDPI support to XWayland, with different approaches.

Until it is merged, you will have to add the patch manually to your XWayland
installation. If you are using ArchLinux, there are AUR packages which have the
patch applied.

See [this page](hidpi-scaling-patches.html) instructions on applying XWayland
related patches.

[MR #733]: https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/733

### Labwc XWayland Settings

To enable scaling in XWayland applications, you will need to run `xprop` as an
autostart command in labwc, and set the `GDK_SCALE` environment variable. You
can also set these properties before running an application during runtime, so
you don't need to restart labwc. You will need to reopen applications for the
changes to take effect.

1. In your `~/.config/labwc/autostart` file, add the following line:

```sh
xprop -root -f _XWAYLAND_GLOBAL_OUTPUT_SCALE 32c -set _XWAYLAND_GLOBAL_OUTPUT_SCALE 2
```

You can also run this when you are logged in, and it will set the scaling for
all XWayland apps. You will need to restart the apps for the changes to take
effect.

2. This step is optional, as it doesn't change non-Wayland GTK apps, but is a
good idea if you want to scale GTK apps as well.

In your `~/.config/labwc/environment` file, add the following line:

```sh
GDK_SCALE=2
```

This will make non-Wayland GTK apps 2x. You can also use `GDK_DPI_SCALE`
environment variable to scale the font size if needed.

To test scaling with GDK, you can use `gtk3-demo` and `gtk4-demo`, which both
run on Wayland:

```sh
GDK_SCALE=2 gtk3-demo
```

## Troubleshooting

As mentioned initially, this is a work in progress, and you will need to tweak
your settings until you find a setting you like. Most apps should behave as
expected, but there are a few issues that you might run into.

### Cursor size is small

Sometimes in XWayland apps, the cursor is half the usual cursor size.

You can try adding the following as a startup script to manage the cursor for
XWayland apps, replacing the cursor theme name and size as needed:

```sh
xsetroot -xcf /usr/share/icons/$your_cursor_theme_name/cursors/left_ptr 48
```

The `-xcf` option tells xsetroot to set the root window's cursor using an X11
cursor file (XCF) format, and 48 is the size of the cursor in pixels.

Another option is to change your XWayland launch script to add the following:

```sh
export XCURSOR_SIZE=48 export XCURSOR_THEME=Adwaita
```

### Font size / DPI issues

#### GTK apps

If you are using GTK apps, you can use the `GDK_SCALE` and `GDK_DPI_SCALE` to
scale the font. You might also need to run `GDK_DPI_SCALE=0.5` to undo the
scaling if needed.

#### Jetbrains

If you have installed Jetbrains applications via the Jetbrains Toolbox, the
.desktop files are located in `~/.local/share/applications` and these can be
modfied to set environment variables in the `Exec=` line, see the
[Modify environment variables](https://wiki.archlinux.org/title/Desktop_entries#Modify_environment_variables)
archwiki page for instructions.

> These will be updated every time the product updates.. So you'll need to keep
> adding them here, which is a pain. You could have another desktop entry, which
> sets then launches this one, but then you'll have two entries in your
> launcher.

Using the Jetbrains Toolbox App you can also create launch scripts, which will
be named `idea.sh`, `clion.sh`, etc. You can edit these to add the
application-specific environment variables.

