# Getting Started

Labwc is designed to be easy to get started with.

To use the compositor for the first time, there is no need for configuration
files, theme files or even a session file.  It should be enough to simply run
the labwc binary from a TTY or Wayland/X11 session. 

If labwc is not packaged by your OS/distribution of choice, it is quite easy
to build (which should take no more than a few seconds) and run from the build
directory.[^1]

[^1]: The compositor works fine without doing a system-wide installation, but
      just be aware that you will not get localized (translated to local
      language) window context menus, nor will you get a system-wide .desktop
      file where most display managers look for them (if you use one of them).

The first time you run labwc, you'll be greeted by a blank screen. If you click
on the desktop you will see your root-menu containing 'Reconfigure' and 'Exit'.
Although this initial appearance is minimalist and sparse, it is easy to get
started.

Before doing any configuration, you can start labwc with the following command
to start an application (alacritty is used in the example, but it could of
course be any application):

```
labwc -s alacritty
```

Alternatively, if you have bemenu installed, you can use the default keybind
Alt-F3 to launch applications.

<img src="https://i.imgur.com/vn1eGaI.png" />


# Configuration

labwc user configuration files are located at `~/.config/labwc/`. The following
four files are used:

- rc.xml
- autostart
- environment
- menu.xml

The purpose of each of these files should become clear if you take the steps
below.

## Step 1 - Set your keyboard layout

Set the environment variable `XKB_DEFAULT_LAYOUT` with your country code.

For example to start with Swedish keyboard layout, run

```
XKB_DEFAULT_LAYOUT=se labwc
```

Or simply add this line to `~/.config/labwc/environment`

```
XKB_DEFAULT_LAYOUT=se
```

If you are unsure what your country code is, refer to the 'layout' section of
`/usr/share/X11/xkb/rules/evdev.lst`

See further examples in [docs/environment](https://github.com/labwc/labwc/blob/master/docs/environment)

## Step 2 - Add some items to the root-menu

Create a `~/.config/labwc/menu.xml` to hand-craft a menu. See [docs/menu.xml](https://github.com/labwc/labwc/blob/master/docs/menu.xml)
for inspiration, or use the simple example below

```
<?xml version="1.0">

<openbox_menu>
<menu id="root-menu" label="">
  <item label="Web browser"><action name="Execute" command="firefox" /></item>
  <item label="Terminal"><action name="Execute" command="alacritty" /></item>
  <item label="Reconfigure"><action name="Reconfigure" /></item>
  <item label="Exit"><action name="Exit" /></item>
</menu>
</openbox_menu>
```

Run `killall -s SIGHUP labwc` to reload the config files.

See [integration#menu-generators](https://labwc.github.io/integration.html#menu-generators)
for ideas on how to automatically create menu.xml files.

## Step 3 - Set a shortcut to a launcher

If you want to bind a key-combination to a launcher such as rofi or wofi, or
simply a terminal, create a configuration file `~/.config/labwc/rc.xml` and add
a `<keybind>` entry as shown below. In this example `Super-d` is bound to the
terminal sakura:

```
<?xml version="1.0"?>
<labwc_config>

  <keyboard>
    <default />
    <keybind key="W-d"><action name="Execute" command="sakura" /></keybind>
  </keyboard>

</labwc_config>
```

See [docs/rc.xml.all](https://github.com/labwc/labwc/blob/master/docs/rc.xml.all) for all available configuration options.

## Step 4 - Start a background-image client and a panel

To use a background-color/image client or a panel, simply add the command
to `~/.config/labwc/autostart`. See example below for using swaybg and waybar:

```
swaybg -i foo.png >/dev/null 2>&1 &
waybar >/dev/null 2>&1 &
```

The `>/dev/null 2>&1` is simply there to hide the logging.
Don't forget the `&` at the end otherwise the compositor will get stuck on that
line.

See further examples in [docs/autostart](https://github.com/labwc/labwc/blob/master/docs/autostart)

## Step 5 - install some themes for server-side-decorations

Some commonly packaged themes support openbox (and therefore labwc) out of the
box, for example `Numix` and `Adapta`.

Install a theme and set it in rc.xml:

```
  <theme>
    <name>Numix</name>
  </theme>
```

To just use the current GTK theme, you can use [this tool](https://github.com/johanmalm/labwc-gtktheme)

Refer to the [man pages](https://labwc.github.io/manual.html) for full documentation.

Enjoy!
