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


