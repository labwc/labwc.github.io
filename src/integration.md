# Integration

- 1. Panels
  - [waybar](#waybar)
- 2. [Menu Generators](#menu-generators)


## Panels

### waybar {#waybar}

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

## Menu Generators {#menu-generator}

Several menu-generators exist to automatically create a menu.xml with system
applications:

[labwc-menu-gnome3](https://github.com/labwc/labwc-menu-gnome3)
[obmenu-generator](https://trizenx.blogspot.com/2012/02/obmenu-generator.html)
[openbox-menu](http://fabrice.thiroux.free.fr/openbox-menu_en.html)

They are typically used like this:

```
labwc-menu-gnome3 > ~/.config/labwc/menu.xml
```

