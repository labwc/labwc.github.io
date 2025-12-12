# Developer Section

1. [Image Buffers](#img-buf)

# 1. Image Buffers {#img-buf}

Ref: [#2489](https://github.com/labwc/labwc/pull/2489)

This relates to the structs `lab_img`, `lab_image_cache` and
`scaled_img_buffer`.

- When creating a `scaled_img_buffer`, `lab_img` is replicated via
  `lab_img_copy()`
- When destroying a `scaled_img_buffer`, `lab_img` is destroyed via
  `lab_img_destroy()`

## The lifetime of `lab_img` and `lab_img_cache`

After startup, theme struct references `lab_img`, which references
`lab_img_cache` with refcount=1. Here, `lab_img_cache` is the wrapper for
`lab_data_buffer` or `RsvgHandle` and represents the actual content of the
loaded image file.

<img src="img/dev/img-buf1.png">

When a window is opened and its decoration is created, the `lab_img` is copied
via `lab_img_copy()` and a new `scaled_img_buffer` references it. Note that the
image content is not copied here; instead, the refcount of `lab_img_cache` is
incremented.

<img src="img/dev/img-buf2.png">

When the theme is de-initialized in `theme_finish()` and the `lab_img`
referenced by theme is destroyed, the `lab_img` referenced by the
`scaled_img_buffer` and `lab_img_cache` outlive. Therefore, it's safe for
`_update_buffer()` in `scaled-img-buffer.c` to be called.

<img src="img/dev/img-buf3.png">

And when the decoration is destroyed via undecorate(), the `scaled_img_buffer`,
`lab_img` and `lab_img_cache` are finally destroyed.

## Motivation for `lab_img_copy()` and `lab_img_cache`

For better understanding of `lab_img` API in general, let me explain the initial
motivation of `lab_img_copy()` and `lab_img_cache`. `lab_img_copy()` was
introduced to share the image content with different variants of buttons
including normal, hovered, rounded, rounded-hovered buttons:

<img src="img/dev/img-buf4.png">

For example, when `close_hover-active.png` is not found, the `lab_img` for
`close-active.png` is copied via `lab_img_copy()` and a "modifier" function
that draws a hover overlay on it is added to the copied `lab_img` via
`lab_img_add_modifier()`. And if the close button is placed at the corner of
the titlebar, the `lab_img` is further copied and the modifier function that
cuts its corner is applied.

