# Troubleshooting

## Nvidia

If Electron clients are glitchy or lagging try setting these environment
variables:

```
GBM_BACKEND=nvidia-drm
__GLX_VENDOR_LIBRARY_NAME=nvidia
```

## Cursors

If no cursor is showing (sometimes reported by people running vwmare), try
adding `WLR_NO_HARDWARE_CURSORS=1` to `~/.config/labwc/environment`.

If cursors do not update as expexted, try installing a cursor theme (for
example `Adwaita`) and set `XCURSOR_THEME` in `~/.config/labwc/environment`
accordingly (for example `XCURSOR_THEME=Adwaita`).  `labwc` handles missing
cursor themes by falling back on builtin old X11 cursors, but some applications
do not resulting in the wrong or no cursor being set.
