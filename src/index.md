<h2><img src="img/labwc.png" alt="labwc" height="64px" /><br />labwc</h2>

[<a href="https://github.com/labwc/labwc#readme">readme</a>]
[<a href="integration.html">integration</a>]
[<a href="manual.html">manual</a>]

Labwc is a wlroots-based stacking compositor for Wayland.

It is light-weight and independent with a focus on simply stacking windows well and rendering some window decorations. It takes a no-bling/frills approach and says no to features such as icons (except window buttons), animations, decorative gradients and any other options not required to reasonably render common themes. It relies on clients for panels, screenshots, wallpapers and so on to create a full desktop environment.

Labwc tries to stay in keeping with [wlroots] and [sway] in terms of general approach and coding style.

Labwc only understands [wayland-protocols] &amp; [wlr-protocols], and it cannot be controlled with dbus, sway/i3-IPC or other technology. The reason for this is that we believe that custom IPCs and protocols create a fragmentation that hinders general Wayland adoption.

<a href="https://i.imgur.com/vOelinT.png"><img src="https://i.imgur.com/vOelinT.png" width=640 height=360></a>

[wlroots]: https://gitlab.freedesktop.org/wlroots/wlroots
[sway]: https://github.com/swaywm 
[wayland-protocols]: https://gitlab.freedesktop.org/wayland/wayland-protocols
[wlr-protocols]: https://gitlab.freedesktop.org/wlroots/wlr-protocols 
