# Integration

## Table of Contents

Panels

- [waybar](#waybar)

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

