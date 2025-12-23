# Frequently Asked Questions

1. [Keybinds](#keybinds)
    1. [Unset Keybinds](#unset-keybinds)
    2. [Common Keybinds](#common-keybinds)
    3. [Keybind Forwarding](#keybind-forwarding)
2. [Theme](#theme)
    1. [Server Side Decoration](#server-side-decoration)
3. [Mouse and Trackpads](#mouse-and-trackpads)
    1. [Libinput](#libinput)
    2. [Mousebinds](#mousebinds)
    3. [Cursor](#cursor)
4. [XML](#xml)
    1. [XML Nodenames](#xml-nodenames)
5. [Scripting](#scripting)
    1. [Run or Raise](#run-or-raise)
6. [Environment Variables](#environment-variables)
7. [Nested XWayland](#nested-xwayland)
8. [Hardware](#hardware)
    1. [Nvidia](#nvidia)
    2. [Laptop Lid](#laptop-lid)
9. [Applications](#applications)
    1. [gparted](#gparted)
    2. [GTK4](#gtk4)

# 1. Keybinds {#keybinds}

## 1.1 Unset keybinds {#unset-keybinds}

### Q: How do I get `Alt+Left/Right` to not move windows? I want these to navigate forward/backwards in File Managers and Firefox.

You could either copy `rc.xml.all` and just remove the entries you do not want, such as `<keybind key="A-Left">`

Or you could use the `None` action or simply define a keybind with no action (which does the same). For example:

```
  <keyboard>
    <default/>
    <keybind key="A-Left"/>
    <keybind key="A-Right"/>
  </keyboard>
```

## 1.2 Common keybinds {#common-keybinds}

### Q: How do I get `Windows+Up` to maximize/restore-to-previous-size a window?

```
<keybind key="W-Up"><action name="ToggleMaximize"/></keybind>
```

See [ToggleMaximize] action.

[ToggleMaximize]: https://labwc.github.io/labwc-actions.5.html#entry_action_name=togglemaximize

### Q: Is it possible to launch wofi with only the Super key?

```
<keybind key="Super_L" onRelease="true">
  <action name="Execute" command="wofi"/>
</keybind>
```

### Q: Is it possible to show gaps for maximized windows?

Use `<action name="SnapToEdge" direction="center" />`.

### Q: How do I close windows with `W-q`?

```
<keybind key="W-q"><action name="Close"/></keybind>
```

### Q: Keybinds to switch-to / move-a-window-to workspace 1, 2 etc.?

In true `sway` style:

```
<keybind key="W-1"><action name="GoToDesktop" to="1"/></keybind>
<keybind key="W-2"><action name="GoToDesktop" to="2"/></keybind>
<keybind key="W-3"><action name="GoToDesktop" to="3"/></keybind>

<keybind key="W-S-1"><action name="SendToDesktop" to="1" follow="false"/></keybind>
<keybind key="W-S-2"><action name="SendToDesktop" to="2" follow="false"/></keybind>
<keybind key="W-S-3"><action name="SendToDesktop" to="3" follow="false"/></keybind>
```

## 1.3 Keybind Forwarding {#keybind-forwarding}

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

# 2. Theme {#theme}

## 2.1 Server Side Decoration {#server-side-decoration}

### Q: Is it possible to completely remove windows' title-bars?

Yes.

Action `SetDecorations` can be used for this. This action can be used with
key/mousebinds or with window rules like this:

```
<windowRules>
  <windowRule identifier="*">
    <action name="SetDecorations" decorations="border" />
  </windowRule>
</windowRules>
```

With window rules it can be achieve more simply as in the example below, but
that will remove borders too:

```
<windowRules>
  <windowRule identifier="*" serverDecoration="no" />
</windowRules>
```

### Q: I'd like to be able to remove the client-menu button. How can this be done?

Add this to `~/.config/labwc/themerc-override`:

```
window.active.button.menu.unpressed.image.color: #000000 0
window.inactive.button.menu.unpressed.image.color: #000000 0
```

# 3. Mouse and Trackpads {#mouse-and-trackpads}

## 3.1 Libinput {#libinput}

### Q: How to scroll with the right edge of the trackpad?

```
<libinput>
  <device>
    <scrollMethod>edge</scrollMethod>
  </device>
</libinput>
```

## 3.2 Mousebinds {#mousebinds}

### Q: I'm used to MS Windows and would like all window to unfocus when I click the desktop. How can this be achieved?

```
<mouse>
  <default />
  <context name="Root">
    <mousebind button="Left" action="Press">
      <action name="Unfocus" />
    </mousebind>
  </context>
</mouse>
```

## 3.3 Cursor {#cursor}

### Q: I cannot see a cursor. What should I do?

If no cursor is showing (sometimes reported by people running vwmare), try
adding `WLR_NO_HARDWARE_CURSORS=1` to `~/.config/labwc/environment`.

If cursors do not update as expected, try installing a cursor theme (for
example `Adwaita`) and set `XCURSOR_THEME` in `~/.config/labwc/environment`
accordingly (for example `XCURSOR_THEME=Adwaita`).  `labwc` handles missing
cursor themes by falling back on builtin old X11 cursors, but some applications
do not resulting in the wrong or no cursor being set.

# 4. XML {#xml}

## 4.1 XML Nodenames {#xml-nodenames}

### Q: My config file does not work. How can I debug it?

You a can a nested instance of labwc in a terminal to see the error messages
relating to bad XML syntax of missing elements/attributes.

For more fine-grained analysis you can see the config/menu file nodenames when
`labwc` starts, by setting the following environment variables:

```
LABWC_DEBUG_CONFIG_NODENAMES=1
LABWC_DEBUG_MENU_NODENAMES=1
```

With `labwc` a nodename is a way to refer to each element and attribute in an
XML tree.  For example, the `<c>` element below would be assigned the nodename
`c.b.a`:

```
<a>
  <b>
    <c>foo</c>
  </b>
</a>
```

Please note that `labwc` also parses the rc.xml configuration file in an
element/attribute agnostic way, which means that `<a><b>foo</b></a>` is
equivalent to `<a b="foo"/>`. Be careful though, because this does not apply to
some aspects of menu.xml (specifically the attributes id, label and execute).

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

See [labwc-config(5)-syntax] for more details.

[labwc-config(5)-syntax]: https://labwc.github.io/labwc-config.5.html#syntax

# 5. Scripting {#scripting}

## 5.1 Run or Raise {#run-or-raise}

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

As of labwc version 0.7.2 it is also possible to create a run or raise keybind
with the `ForEach` action:

```
<keybind key="W-F1">
  <action name="ForEach">
    <query identifier="foot" />
    <then>
      <action name="Raise" />
      <action name="Focus" />
    </then>
    <none>
      <action name="Execute" command="foot" />
    </none>
  </action>
</keybind>
```

[wlrctl]: https://git.sr.ht/~brocellous/wlrctl
[lswt]: https://sr.ht/~leon_plickat/lswt/
[wlr-foreign-toplevel-management]: https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1

# 6. Environment Variables {#environment-variables}

There are a number of advanced settings that can be invoked for `wlroots` by
setting some environment variables.

For example `labwc` can be run nested on Wayland with multiple outputs using
the following: `WLR_WL_OUTPUTS=2 labwc`

See the wlroots repo [env_vars.md] file for details.

[env_vars.md]: https://gitlab.freedesktop.org/wlroots/wlroots/-/blob/master/docs/env_vars.md

# 7. Nested XWayland {#nested-xwayland}

To run a nested instance of openbox on labwc:
 
```
Xwayland -decorate -noreset :55
DISPLAY=:55 dbus-run-session openbox-session
  
```
 
# 8. [Hardware]{#hardware}

## 8.1 [Nvidia]{#nvidia}

If Electron clients are glitchy or lagging try setting these environment
variables:

```
GBM_BACKEND=nvidia-drm
__GLX_VENDOR_LIBRARY_NAME=nvidia
```

## 8.2 [Laptop Lid]{#laptop-lid}

When using a laptop with an external monitor and the built-in monitor is closed,
the system may go into hibernation when disconnecting. To avoid this, edit the
configuration file `etc/systemd/logind.conf' and set following to ignore (see
logind.conf(5) manual for more info):

```
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
```

# 9. [Applications]{#applications}

## 9.1 [gparted]{#gparted}

### Q: I'm having some trouble starting gparted

> Note: It is not recommended to run GUI clients as root.

```
$ pkexec --disable-internal-agent /usr/sbin/gparted
Invalid MIT-MAGIC-COOKIE-1 key
(gpartedbin:1286199): Gtk-WARNING **: 17:31:50.245: cannot open display: :0
```

Either install `xauth` or run `xhost +si:localuser:root` as the user who
started labwc (not root) to fix this.

If `xauth` and/or `xhost` are not installed, it is possible to run with
`sudo -E gparted`.

## 9.2 [GTK4]{#gtk4}

### Q: My compose key stopped working

This is due to a change in GTK4 which now requires input methods for compose.
Either install a input method like ibus or fcitx5 or force GTK4 to use its
built-in compose method by adding `GTK_IM_MODULE=simple` to
`~/.config/labwc/environment`.
