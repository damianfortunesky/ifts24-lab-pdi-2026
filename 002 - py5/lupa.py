import py5

img = None


def setup():
    global img
    py5.size(800, 400)
    img = py5.load_image("img/imagen.jpg")
    img.resize(400, 400)


def draw():
    py5.background(255)

    py5.image(img, 0, 0)

    mx = py5.constrain(py5.mouse_x, 0, 399)
    my = py5.constrain(py5.mouse_y, 0, 399)

    color_pixel = py5.get_pixels(int(mx), int(my))

    r = py5.red(color_pixel)
    g = py5.green(color_pixel)
    b = py5.blue(color_pixel)

    py5.fill(color_pixel)
    py5.stroke(0)
    py5.rect(450, 50, 300, 300)

    py5.fill(0)
    py5.text_size(18)
    py5.text(f"Posición: ({mx:.0f}, {my:.0f})", 450, 30)
    py5.text(f"R: {r:.0f}   G: {g:.0f}   B: {b:.0f}", 450, 380)


py5.run_sketch()
