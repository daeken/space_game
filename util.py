def trans(image, size):
    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b, a = image.get_at((x, y))
            if r == 0 and g == 255 and b == 128:
                image.set_at((x, y), (0, 0, 255, 0))

def trans_to_clear(image, size):
    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b, a = image.get_at((x, y))
            if r == 0 and g == 255 and b == 128:
                image.set_at((x, y), (0, 0, 0, 255))
