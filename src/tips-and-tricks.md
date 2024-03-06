# Tips & Tricks

1. [XML Nodenames](#xml-nodenames)
2. [Keybind Forwarding](#keybind-forwarding)
3. [Run or Raise](#run-or-raise)
4. [Environment Variables](#environment-variables)
5. [Nested XWayland](#nested-xwayland)

## XML Nodenames

`labwc` refers to each element and attribute in an XML tree by a nodename.  For
example, the `<c>` element below would be assigned the nodename `c.b.a`:

```
<a>
  <b>
    <c>foo</c>
  </b>
<a>
```

`labwc` also parses XML in an element/attribute agnostic way, which means that
`<a><b>foo</b></a>` is equivalent to `<a b="foo"/>`.

To see the config/menu file nodenames when `labwc` starts, set the following
environment variables:

```
LABWC_DEBUG_CONFIG_NODENAMES=1
LABWC_DEBUG_MENU_NODENAMES=1
```

In practical terms, this means that the following syntax could be used:

```
<keybind key="W-l" name.action="Execute" command.action="swaylock -c 000000"/>
```

...rather than then lengthier:

```
<keybind key="W-l">
  <action name="Execute">
    <command>swaylock -c 000000"</command>
  </action>
</keybind>
```

See [labwc-config(5)-syntax] for examples and more detail.

[labwc-config(5)-syntax]: https://labwc.github.io/labwc-config.5.html#syntax

## Keybind Forwarding

The [ToggleKeybinds] action allows better control of Virtual Machines, VNC
clients, nested compositors or similar.

For example, to make alt-tab work in a nested compositor add the code below to
`~/.config/labwc/rc.xml` and then press F12 to disable all keybinds in the
parent compositor and thereby forward them to the nested instance.

```
<keybind key="F12">
	<action name="ToggleKeybinds"/>
</keybind>
```

[ToggleKeybinds]: https://labwc.github.io/labwc-actions.5.html#entry_action_name=togglekeybinds

## Run or Raise

The [wlr-foreign-toplevel-management] protocol provides clients with a list of
opened applications and lets them request certain actions on them, like
maximizing, focusing, etc. This can be used for scripting with clients such as
[wlrctl] and [lswt]. For example, the script below launches an application
if it is not already running, or focuses the application's most recently opened
window if it is already running:

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

[wlrctl]: https://git.sr.ht/~brocellous/wlrctl
[lswt]: https://sr.ht/~leon_plickat/lswt/
[wlr-foreign-toplevel-management]: https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1

## Environment Variables

There are a number of advanced settings that can be invoked for `wlroots` by
setting some environment variables.

For example `labwc` can be run nested on Wayland with multiple outputs using
the following: `WLR_WL_OUTPUTS=2 labwc`

See the wlroots repo [env_vars.md] file for details.

[env_vars.md]: https://gitlab.freedesktop.org/wlroots/wlroots/-/blob/master/docs/env_vars.md

## Nested XWayland

To run a nested instances of openbox on labwc:

```
Xwayland -decorate -noreset :55
DISPLAY=:55 dbus-run-session openbox-session
```


