from PIL import Image
import random
import math

import my_utilities as ut


class ImageCreator:
    def __init__(self, height, width, base_color, name, layers=None):
        self.height = height
        self.width = width
        self.base_color = base_color
        self.name = name
        self.layers = layers

        self.image = Image.new("RGB", (self.height, self.width), self.base_color)
        self.pixels = self.image.load()
        self.image.save(self.name)

        self.points = []

    def paint_image(self):
        pass

    def point_image(self, quantity, color_shading):
        color = ((self.base_color[0] + color_shading[0]) % 256,
                 (self.base_color[1] + color_shading[1]) % 256,
                 (self.base_color[2] + color_shading[2]) % 256)

        for point in range(quantity):
            coord = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            self.pixels[coord] = color
            self.points.append(coord)

        self.image.save(self.name)

    def divide_image(self, quantity, color_shading):
        self.points = []
        self.point_image(quantity, color_shading)

        for x in range(self.width):
            for y in range(self.height):

                distance_to_point = []
                for j in self.points:
                    distance_to_point.append(math.sqrt((x - j[0]) ** 2 + (y - j[1]) ** 2))

                color_grad = min(distance_to_point) + 255

                self.pixels[x, y] = (int((color_grad / 256 ** 2) % 256),
                                     int((color_grad / 256) % 256),
                                     int(color_grad % 256))
        self.image.save(self.name)

    def place_corner(self):
        self.pixels[0, 0] = (0, 0, 0)
        self.pixels[0, self.height - 1] = (0, 0, 0)
        self.pixels[self.width - 1, 0] = (0, 0, 0)
        self.pixels[self.width - 1, self.height - 1] = (0, 0, 0)
        self.image.save(self.name)

    def apply_layers(self):
        for layer in self.layers:
            for x in range(self.width):
                for y in range(self.height):
                    if layer.visible_range[0] < \
                            layer.function((x / self.width) * 100, (y / self.height) * 100) \
                            < layer.visible_range[1]:
                        self.pixels[x, y] = layer.color_modifier(self.pixels[x, y])
        self.image.save(self.name)


class Pixel:
    def __init__(self, position):
        self.color = (0, 0, 0)
        self.position = position
        self.group = None
