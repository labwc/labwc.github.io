# Obligatory Screenshot

The screenshot was created with the following desktop components and themes:

1. [pcmanfm-qt --desktop](https://github.com/lxqt/pcmanfm-qt) for the background color (`#161616`) and desktop icons
2. [xfce4-panel]
3. [labwc-tweaks] configuration tool
4. [labwc-menu-generator] to generate the content for the built-in compositor menu
5. [labTeallach] compositor theme
6. [WhiteSur-opaqueDark] Kvantum theme for Qt applications
7. [Papirus] icon theme

[pcmanfm-qt --desktop]: https://github.com/lxqt/pcmanfm-qt
[xfce4-panel]: https://gitlab.xfce.org/xfce/xfce4-panel
[labwc-tweaks]: https://github.com/labwc/labwc-tweaks
[labwc-menu-generator]: https://github.com/labwc/labwc-menu-generator
[labTeallach]: https://github.com/labwc/labwc-themes/tree/master/labTeallach/labwc
[WhiteSur-opaqueDark]: https://github.com/vinceliuice/WhiteSur-kde/tree/master/Kvantum/WhiteSur-opaque
[Papirus]: https://github.com/PapirusDevelopmentTeam/papirus-icon-theme

Full size image <a href="img/scrot0-landing-page.png">here</a>

The compositor root-menu was defined by the files below.

`~/.config/labwc/menu.xml`

```
<openbox_menu>
  <menu id="root-menu" label="" execute="menu.sh"/>
</openbox_menu>
```

`~/bin/menu.sh`

```
#!/bin/sh

printf '%b\n' '
<openbox_pipe_menu>

  <item label="Web Browser" name.action="Execute" command.action="firefox" icon="firefox" />
  <item label="Terminal" name.action="Execute" command.action="foot" icon="utilities-terminal" />
  <item label="File Manager" name.action="Execute" command.action="pcmanfm-qt" icon="system-file-manager" />
  <item label="Tweaks" name.action="Execute" command.action="labwc-tweaks" icon="configure" />

  <separator />'

labwc-menu-generator -b -I -t foot

printf '%b\n' '
  <separator />

  <menu id="help" label="Help" icon="help">
    <separator label="Online Help" />
    <item label="labwc.github.io" name.action="Execute" command.action="firefox https://labwc.github.io" icon="applications-development-web" />

    <separator label="Man Pages" />
    <item label="labwc(1)" name.action="Execute" command.action="firefox https://labwc.github.io/labwc.1.html" icon="deepin-manual" />
    <item label="labwc-config(5)" name.action="Execute" command.action="firefox https://labwc.github.io/labwc-config.5.html" icon="deepin-manual" />
    <item label="labwc-theme(5)" name.action="Execute" command.action="firefox https://labwc.github.io/labwc-theme.5.html" icon="deepin-manual" />
    <item label="labwc-menu(5)" name.action="Execute" command.action="firefox https://labwc.github.io/labwc-menu.5.html" icon="deepin-manual" />
    <item label="labwc-actions(5)" name.action="Execute" command.action="firefox https://labwc.github.io/labwc-actions.5.html" icon="deepin-manual" />
    <item label="labnag(1)" name.action="Execute" command.action="firefox https://labwc.github.io/labnag.1.html" icon="deepin-manual" />
  </menu>

  <menu id="Preferences" label="Preferences" icon="applications-engineering">
    <item label="Edit rc.xml" name.action="Execute" command.action="featherpad ~/.config/labwc/rc.xml" icon="text-x-generic" />
    <item label="Edit autostart" name.action="Execute" command.action="featherpad ~/.config/labwc/autostart" icon="text-x-generic" />
  </menu>

  <menu id="Exit" label="Exit" icon="application-exit">
    <item label="Reconfigure" name.action="Reconfigure" icon="labwc" />
    <item label="Logout" name.action="Exit" icon="application-exit" />
  </menu>

</openbox_pipe_menu>'
```
