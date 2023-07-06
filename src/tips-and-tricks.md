# Tips & Tricks

## XML Flexibility

`labwc` parses XML in an element/attribute agnostic way. This is a design
decision to increase config file flexibility and keep code simple. In practical
terms, this means that `<a><b>c</b></a>` is equivalent to `<a b="c" />`.

See [labwc-config(5)-syntax] for examples and more detail.

[labwc-config(5)-syntax]: https://labwc.github.io/labwc-config.5.html#syntax

## Keybind Forwarding

The [`ToggleKeybinds`] action allows better control of Virtual Machines,
VNC clients, nested compositors or similar.

For example, to make alt-tab work in a nested compositor add the code below to
`~/.config/labwc/rc.xml` and then press F12 to disable all keybinds in the
parent compositor and thereby forward them to the nested instance.

```
<keybind key="F12">
	<action name="ToggleKeybinds"/>
</keybind>
```

[`ToggleKeybinds`]: https://labwc.github.io/labwc-actions.5.html#entry_action_name=togglekeybinds

## Run or Raise

The `wlr-foreign-toplevel-managment` protocols provides clients with a list of
opened applications and lets them request certain actions on them, like
maximizing, focusing, etc. This can be used for scripting with clients such as
[`wlrctl`] and [`lswt`]. For example, see below a a script which (a) launches
an application if it is not already running, or (b) focuses the application's
most recently opened window if it is already running:

```
#!/bin/sh

if test -z "$1"; then
	echo "Usage: runraise app_id [executable]"
	exit 1
fi

app_id=$1
executable=$2
test -z "$executable" && executable=$app_id

if ! wlrctl window focus "$app_id"; then
	$executable &
	disown
fi
```

[`wlrctl`]: https://git.sr.ht/~brocellous/wlrctl
[`lswt`]: https://sr.ht/~leon_plickat/lswt/
[`wlr-foreign-toplevel-managment`]: https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1
