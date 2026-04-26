import py5

img = None


def setup():
    global img
    py5.size(800, 400)
    img = py5.load_image("img/imagen.jpg")
    img.resize(400, 400)


def draw():
    py5.background(35)

    py5.image(img, 0, 0)

    factor_rojo = py5.remap(py5.mouse_x, 0, py5.width, 0, 2.5)
    factor_rojo = py5.constrain(factor_rojo, 0, 2.5)

    img.load_pixels()
    py5.load_pixels()

    for x in range(img.width):
        for y in range(img.height):
            indice_img = x + y * img.width
            pixel = img.pixels[indice_img]

            r = py5.red(pixel)
            g = py5.green(pixel)
            b = py5.blue(pixel)

            r = r * factor_rojo

            if r > 255:
                r = 255

            indice_canvas = (x + 400) + y * py5.width
            py5.pixels[indice_canvas] = py5.color(r, g, b)

    py5.update_pixels()


py5.run_sketch()
