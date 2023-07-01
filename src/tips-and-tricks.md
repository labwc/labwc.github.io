# Tips & Tricks

## XML

`labwc` parses XML in an element/attribute agnostic way. This is a design
decision to increase config file flexibility and keep code simple. In practical
terms, this means that `<a><b>c</b></a>` is equivalent to `<a b="c" />`.  See
(labwc-config.5.syntax)[https://labwc.github.io/labwc-config.5.html#syntax] for
examples and more detail.


