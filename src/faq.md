# Frequently Asked Questions

1. [Keybinds](#keybinds)
    1. [Unset Keybinds](#unset-keybinds)
    2. [Common Keybinds](#common-keybinds)
2. [Theme](#theme)
    1. [Server Side Decoration](#server-side-decoration)
3. [Mouse and Trackpads](#mouse-and-trackpads)
    1. [Libinput](#libinput)

# 1. Keybinds {keybinds}

## 1.1 Unset keybinds {unset-keybinds}

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

## 1.2 Common keybinds {common-keybinds}

### Q: How do I get `Windows+Up` to maximize/restore-to-previous-size a window?

```
<keybind key="W-Up"><action name="ToggleMaximize"/></keybind>
```

See [ToggleMaximize] action.

[ToggleMaximize]: https://labwc.github.io/labwc-actions.5.html#entry_action_name=togglemaximize

### Q: Is it possible to launch wofi with only the Super key?

No. I'm afraid that is not yet implemented.

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

# 2. Theme {theme}

## 2.1 Server Side Decoration {server-side-decoration}

### Q: Is it possible to completely remove windows' title-bars?

Yes. Action `ToggleDecoration`, but it removes borders too.

```
<windowRule title="*" >
  <action name="ToggleDecoration"/>
</windowRule>
```

# 3. Mouse and Trackpads {mouse-and-trackpads}

## 3.1 Libinput {libinput}

### Q: How to scroll with the right edge of the trackpad?

Not yet implemented.

