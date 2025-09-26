# Configuration

This document contains some popular settings that you may wish to adopt.

## General

### Enable Dropshadows

```
<theme>
  <dropShadows>yes</dropShadows>
</theme>
```

### Enable automatic window placement policy

```
<placement>
  <policy>automatic</policy>
</placement>
```

## Window Switcher

### Show windows regardless of what workspace they are on

```
<windowSwitcher>
  <allWorkspaces>yes</allWorkspaces>
</windowSwitcher>
```

## Keybinds

### Lock Session

```
<keybind key="W-l" name.action="Execute" command.action="swaylock -c 000000"/>
```

### Bind Super to a Menu

Supported since `0.7.3`

```
<keybind key="Super_L" onRelease="yes">
  <action name="Execute" command="rofi -show drun"/>
</keybind>
```

or

```
<keybind key="Super_L" onRelease="yes">
  <action name="ShowMenu" menu="root-menu"/>
</keybind>
```


### Take Screenshot

```
<keybind key="Print">
  <action name="Execute">
    <command>sh -c 'grim -g "$(slurp)"'</command>
  </action>
</keybind>
```

### Screen Record

```
<keybind key="W-F7" name.action="Execute" command.action="wf-recorder --output eDP-1"/>
<keybind key="W-F8" name.action="Execute" command.action="killall SIGINT wf-recorder"/>
```

### Alt-Tab Backwards

```
<keybind key="S-A-Tab" name.action="PreviousWindow"/>
```

### MoveToEdge, ShrinkToEdge and GrowToEdge

```
<keybind key="W-Left">
  <action name="MoveToEdge" direction="left" snapWindows="true"/>
</keybind>
<keybind key="W-Right">
  <action name="MoveToEdge" direction="right" snapWindows="true"/>
</keybind>
<keybind key="W-Up">
  <action name="MoveToEdge" direction="up" snapWindows="true"/>
</keybind>
<keybind key="W-Down">
  <action name="MoveToEdge" direction="down" snapWindows="true"/>
</keybind>
<keybind key="W-S-Left">
  <action name="ShrinkToEdge" direction="left"/>
</keybind>
<keybind key="W-S-Right">
  <action name="GrowToEdge" direction="right"/>
</keybind>
<keybind key="W-S-Up">
  <action name="ShrinkToEdge" direction="up"/>
</keybind>
<keybind key="W-S-Down">
  <action name="GrowToEdge" direction="down"/>
</keybind>
```

### SnapToEdge

```
<keybind key="C-W-Left">
  <action name="SnapToEdge" direction="left"/>
</keybind>
<keybind key="C-W-Right">
  <action name="SnapToEdge" direction="right"/>
</keybind>
<keybind key="C-W-Up">
  <action name="SnapToEdge" direction="up"/>
</keybind>
<keybind key="C-W-Down">
  <action name="SnapToEdge" direction="down"/>
</keybind>
```

## Mousebinds

### Unfosus all windows when clicking on desktop

This relates to `Desktop` in the sense of a layer-shell client such as `swaybg`
which does not receive mouse-events.

Note: Clients such as `xfdesktop` and `pcmanfm --desktop` behave like this
anyway.

```
<context name="Root">
  <mousebind button="Left" action="Press">
    <action name="Unfocus"/>
  </mousebind>
</context>
```

### Directional maximize

```
<context name="Top">
  <mousebind button="Left" action="DoubleClick">
    <action name="ToggleMaximize" direction="vertical"/>
  </mousebind>
</context>
<context name="Bottom">
  <mousebind button="Left" action="DoubleClick">
    <action name="ToggleMaximize" direction="vertical"/>
  </mousebind>
</context>
<context name="Left">
  <mousebind button="Left" action="DoubleClick">
    <action name="ToggleMaximize" direction="horizontal"/>
  </mousebind>
</context>
<context name="Right">
  <mousebind button="Left" action="DoubleClick">
    <action name="ToggleMaximize" direction="horizontal"/>
  </mousebind>
</context>
```

### Magnification

Supported since `0.7.3`

```
<context name="All">
  <mousebind direction="W-Up" action="Scroll">
    <action name="ZoomIn"/>
  </mousebind>
  <mousebind direction="W-Down" action="Scroll">
    <action name="ZoomOut"/>
  </mousebind>
</context>
```

### Switch workspace with super + scroll

Supported since `0.7.3`

```
<context name="All">
  <mousebind direction="W-Up" action="Scroll">
    <action name="GoToDesktop" to="right"/>
  </mousebind>
  <mousebind direction="W-Down" action="Scroll">
    <action name="GoToDesktop" to="left"/>
  </mousebind>
</context>
```

