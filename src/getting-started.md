# Getting Started

Labwc is designed to be easy to get started with.

To use the compositor for the first time, there is no need for configuration
files, theme files or even a session file. It should be enough to simply run
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

<img src="img/scrot-first-start.png" />

# Configuration

The default config files are located at `/usr/share/doc/labwc/`. You can either modify those or
create your own ones by copying them to `${XDG_CONFIG_HOME:-$HOME/.config/labwc/}`
(usually `~/.config/labwc/`), with the following five files being used:
[rc.xml], [menu.xml], [autostart], [environment] and [themerc-override].

The example [rc.xml] has been kept simple. For all options and default values,
see [rc.xml.all]

For full details on configuration options, see the man pages: 
[labwc(1)], [labwc-config(5)], [labwc-theme(5)], [labwc-actions(5)] and
[labwc-menu(5)].

Run `labwc --reconfigure` to reload configuration and theme files.

Your OS/Distribution of choice may include these example configuration files in
`/usr/share/doc/labwc/` or similar. If not, you could download them with:

```bash
mkdir -p ~/.config/labwc
wget https://raw.githubusercontent.com/labwc/labwc/master/docs/environment -O ~/.config/labwc/environment
wget https://raw.githubusercontent.com/labwc/labwc/master/docs/autostart -O ~/.config/labwc/autostart
wget https://raw.githubusercontent.com/labwc/labwc/master/docs/menu.xml -O ~/.config/labwc/menu.xml
wget https://raw.githubusercontent.com/labwc/labwc/master/docs/rc.xml -O ~/.config/labwc/rc.xml
```

> **_NOTE:_** Before using these configuration files, please read them through
> and modify the content to suit your specific needs.

For more information about each configuration file and to help create a setup
that work for you, please read through the sections below.

If you get stuck, do reach out on the [IRC Channel] or [Github Discussions].

[rc.xml]: https://github.com/labwc/labwc/blob/master/docs/rc.xml
[rc.xml.all]: https://github.com/labwc/labwc/blob/master/docs/rc.xml.all
[menu.xml]: https://github.com/labwc/labwc/blob/master/docs/menu.xml
[autostart]: https://github.com/labwc/labwc/blob/master/docs/autostart
[environment]: https://github.com/labwc/labwc/blob/master/docs/environment
[themerc-override]: https://github.com/labwc/labwc/blob/master/docs/themerc
[labwc(1)]: https://labwc.github.io/labwc.1.html
[labwc-config(5)]: https://labwc.github.io/labwc-config.5.html
[labwc-menu(5)]: https://labwc.github.io/labwc-menu.5.html
[labwc-environment(5)]: https://labwc.github.io/labwc-environment.5.html
[labwc-theme(5)]: https://labwc.github.io/labwc-theme.5.html
[labwc-actions(5)]: https://labwc.github.io/labwc-actions.5.html
[IRC Channel]: https://web.libera.chat/gamja/?channels=#labwc
[Github Discussions]: https://github.com/labwc/labwc/discussions

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

See further details, see [docs/environment] and [xkeyboard-config(7)].

[xkeyboard-config(7)]: https://manpages.debian.org/testing/xkb-data/xkeyboard-config.7.en.html

## Step 2 - Add some items to the root-menu

Create a `~/.config/labwc/menu.xml` to hand-craft a menu. See [docs/menu.xml]
for inspiration, or use the simple example below

```
<?xml version="1.0" ?>

<openbox_menu>
<menu id="root-menu" label="">
  <item label="Web browser"><action name="Execute" command="firefox" /></item>
  <item label="Terminal"><action name="Execute" command="alacritty" /></item>
  <item label="Reconfigure"><action name="Reconfigure" /></item>
  <item label="Exit"><action name="Exit" /></item>
</menu>
</openbox_menu>
```

See [integration#menu-generators] for ideas on how to automatically create
menu.xml files.

## Step 3 - Set a shortcut to a launcher

If you want to bind a key-combination to a launcher such as rofi or wofi, or
simply a terminal, create a configuration file `~/.config/labwc/rc.xml` and add
a `<keybind>` entry as shown below. In this example `Super-d` is bound to the
terminal sakura:

```
<?xml version="1.0" ?>
<labwc_config>

  <keyboard>
    <default />
    <keybind key="W-d"><action name="Execute" command="sakura" /></keybind>
    <keybind key="W-z"><action name="Execute" command="wofi --show drun" /></keybind>
  </keyboard>

</labwc_config>
```

See [docs/rc.xml.all] for all available configuration options.

To figure out the name of a key, you can use either xev (widely available,
runs via xwayland) or [wev]. Alternatively, search for keysym names directly in
[xkbcommon-keysyms.h].

[wev]: https://git.sr.ht/~sircmpwn/wev
[xkbcommon-keysyms.h]: https://github.com/xkbcommon/libxkbcommon/blob/master/include/xkbcommon/xkbcommon-keysyms.h

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

See further examples in [docs/autostart]

## Step 5 - install some themes for server-side-decorations

Some commonly packaged themes support openbox (and therefore labwc) out of the
box, for example `Numix` and `Adapta`.

Install a theme and set it in rc.xml:

```
  <theme>
    <name>Numix</name>
  </theme>
```

To just use the current GTK theme, you can use [labwc-gtktheme]

Refer to the [man pages] for full documentation.

Enjoy!


[docs/environment]: https://github.com/labwc/labwc/blob/master/docs/environment
[docs/menu.xml]: https://github.com/labwc/labwc/blob/master/docs/menu.xml
[integration#menu-generators]: https://labwc.github.io/integration.html#menu-generators
[docs/rc.xml.all]: https://github.com/labwc/labwc/blob/master/docs/rc.xml.all
[docs/autostart]: https://github.com/labwc/labwc/blob/master/docs/autostart
[labwc-gtktheme]: https://github.com/johanmalm/labwc-gtktheme
[man pages]: manual.html
