from PIL import Image, ImageDraw
import math
import random
from image_creator import ImageCreator


def better_round(value):
    if value - int(value) > 0.5:
        return int(value) + 1
    else:
        return int(value)


class Shape:
    def __init__(self, length, pattern, radius, center):
        self.length = length
        self.center = center
        self.radius = radius

        if pattern is None:
            self.pattern = []
            for i in range(length):
                self.pattern.append((better_round(self.center[0] + math.cos(i) * self.radius),
                                     better_round(self.center[1] / 2 + math.sin(i) * self.radius)))
                # print(self.pattern[i])


def paint(pixels_array, color, shape):
    try:
        for i in shape.pattern:
            pixels_array[i] = color
        return pixels_array
    finally:
        print('Failed')


img_creator = ImageCreator(250, 250, (73, 103, 221), "my_image.png")
img_creator.divide_image(random.randint(5, 20), (-60, -60, -60))
