Labwc is a [wlroots]-based window-stacking compositor for [wayland], inspired by
[openbox].

It is light-weight and independent with a focus on simply stacking windows well
and rendering some window decorations. It relies on clients for panels,
screenshots, wallpapers and so on to create a full desktop environment.

Labwc tries to stay in keeping with [wlroots] and [sway] in terms of general
approach and coding style.

Labwc only understands [wayland-protocols] &amp; [wlr-protocols], and it cannot
be controlled with dbus, sway/i3-IPC or other technology. The reason for this is
that we believe that custom IPCs and protocols create a fragmentation that
hinders general Wayland adoption.

<a href="img/scrot2.png">
  <img src="img/scrot2-small.png">
</a>
<small><a href="https://labwc.github.io/obligatory-screenshot.html">The obligatory screenshot.</a></small>

[wayland]: https://wayland.freedesktop.org/
[openbox]: http://openbox.org/
[wlroots]: https://gitlab.freedesktop.org/wlroots/wlroots
[sway]: https://github.com/swaywm 
[wayland-protocols]: https://gitlab.freedesktop.org/wayland/wayland-protocols
[wlr-protocols]: https://gitlab.freedesktop.org/wlroots/wlr-protocols