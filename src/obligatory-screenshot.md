# Obligatory Screenshot

1. [Introduction](#introduction)
2. [Background](#background)
3. [Tweaks](#tweaks)
4. [Theme](#theme)
5. [Panel](#panel)
6. [Screenshots](#screenshots)

# 1. Introduction {#introduction}

The [obligatory screenshot] used on the `labwc` website index page and GitHub
repo README.md was created a long time ago and can not easily be re-produced as
it was made with experimental tools and long lost config files.

In response to frequent requests, this document describes a setup that brings
you pretty close using tools that are maintained and readily available.

[obligatory screenshot]: img/scrot1.png

# 2. Background {#background}

```
swaybg -c '#21333b'
```

# 3. Tweaks {#tweaks}

The window is an early version of the [labwc-tweaks] config tool.

# 4. Theme {#theme}

The GTK/Openbox theme is [BL-Lithium]. To use it, copy the [BL-Lithium]
directory to `~/.local/share/themes/` and use [labwc-tweaks] to apply it.

[BL-Lithium]: https://github.com/BunsenLabs/bunsen-themes/tree/beryllium/themes/BL-Lithium
[labwc-tweaks]: https://github.com/labwc/labwc-tweaks

# 5. Panel {#panel}

Use [sfwbar].

Create a `~/.config/sfwbar/sfwbar.config` with the content below.

Copy `{battery-svg,startmenu,winops}.widget` from [sfwbar/config] to
`~/.config/sfwbar/`.

```
Set Term = "sakura"

function("SfwbarInit") {
  SetBarId "bar-0"
  SetLayer "top"
}

include("winops.widget")

layout "sfwbar" {
  include("startmenu.widget")

  button {
    style = "launcher"
    value = $Term
    action = Exec $Term
  }

  button {
    style = "launcher"
    value = "firefox"
    action = "firefox"
  }

  taskbar {
    rows = 1
    group = true
    group cols = 1
    group style = "taskbar_group"
    group labels = true
    group icons = true
    icons = true
    labels = true
    action[3] = Menu "winops"
  }

  label { css = "* { -GtkWidget-hexpand: true; min-height: 30x; }" }

  include("battery-svg.widget")

  label {
    value = Time("%k:%M")
    style ="clock"
  }
}

#CSS
@define-color lab_bg_color RGBA(0, 0, 0, 0.85);
@define-color lab_active_color #bc4b4f;
@define-color lab_hover_color RGBA(255, 255, 255, 0.1);
@define-color lab_text_color #d1d1d1;
@define-color lab_menu_bg_color #353535;

window {
  -GtkWidget-direction: bottom;
  background-color: @lab_bg_color;
}

label {
  font-size: 14px;
  color: @lab_text_color;
  text-shadow: none;
}

button,
button image {
  outline-style: none;
  box-shadow: none;
  background-image: none;
  border-image: none;
  border-radius: 0;
  min-height: 30px;
  min-width: 30px;
  margin: 0px;
  margin-right: 3px;
  border: 0px;
  background-color: RGBA(0, 0, 0, 0.0);
  -GtkWidget-valign: center;
}

button:hover {
  background-color: @lab_hover_color;
}

button#taskbar_group_normal,
button#taskbar_group_normal:hover,
button#taskbar_group_active {
  border: 0px;
  -GtkWidget-valign: center;
}

button#taskbar_group_active {
  background-color: @lab_active_color;
}

button#taskbar_group_active:hover {
  background-color: @lab_hover_color;
}

#menu_item,
#menu_item *,
#menu_item image,
#menu_item label {
  -GtkWidget-halign: start;
  color: white;
}

#menu_item image {
  min-width: 16px;
  min-height: 16px;
  padding-right: 2px;
  margin-right: 7px;
  margin-left: 3px;
}

menu {
  background-color: @lab_menu_bg_color;
}

menu arrow {
  background: none;
}

label#clock {
  color: @lab_text_color;
  -GtkWidget-vexpand: true;
  -GtkWidget-valign: center;
  font-size: 18px;
  margin-right: 8px;
}
```

[sfwbar]: https://github.com/LBCrion/sfwbar
[sfwbar/config]: https://github.com/LBCrion/sfwbar/tree/main/config


# 6. Screenshots {#screenshots}

With described tools and config:

<a href="img/scrot2.png">
  <img src="img/scrot2-small.png">
</a>

Original:

<a href="img/scrot1.png">
  <img src="img/scrot1-small.png">
</a>

