import numpy as np
import os
import itertools as it
from PIL import Image
import random
from manimlib.constants import *
from manimlib.animation.composition import AnimationGroup
from manimlib.animation.indication import ShowPassingFlash
from manimlib.mobject.geometry import Vector
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.types.vectorized_mobject import VMobject
from manimlib.utils.bezier import inverse_interpolate
from manimlib.utils.bezier import interpolate
from manimlib.utils.color import color_to_rgb
from manimlib.utils.color import rgb_to_color
from manimlib.utils.config_ops import digest_config
from manimlib.utils.rate_functions import linear
from manimlib.utils.simple_functions import sigmoid
from manimlib.utils.space_ops import get_norm
from manimlib.utils.space_ops import normalize


def get_vector(self, point, **kwargs):
    output = np.array(self.func(point))
    norm = get_norm(output)
    if norm == 0:
        output *= 0
    else:
        output *= self.length_func(norm) / norm
        vector_config = dict(self.vector_config)
        vector_config.update(kwargs)
        vect = Vector(output, **vector_config)
        vect.shift(point)
        fill_color = rgb_to_color(
            self.rgb_gradient_function(np.array([norm]))[0]
        )
        vect.set_color(fill_color)
        return vect

 def construct(self):
        screen_grid = ScreenGrid()
        self.add(screen_grid)
        v_1 = np.array([1, 0.4, 0])
        v_2 = np.array([1.2, 0.2, 0])
        self.play(FadeIn(Vector(v_1, color = BLUE)))
        self.play(FadeIn(Vector(v_2, color = GREEN)))
        vectors1 = {}
        vectors2 = {}

        for i in range(-15, 15):
            vectors1[i] = i * v_1
            vectors2[i] = i * v_2
            self.add(screen_grid, Vector(vectors1[i], color = BLUE, stroke = 0.2))
            self.play(ReplacementTransform(Vector(vectors1[i]), Dot(vectors1[i])), run_time = 0.125)
            self.play(FadeIn(Vector(vectors2[i], color = GREEN, stroke = 0.2), run_time = 0.125))
            self.play(ReplacementTransform(Vector(vectors2[i]),  Dot(vectors2[i])), run_time = 0.125)

        vector_sum = {}

        for j in range (-15, 15):
            for i in range (-15, 15):
                vector_sum[(i,j)] = (i * v_1) + (j * v_2)
                self.play(FadeIn(Vector(vector_sum[(i,j)], color = ORANGE, stroke = 0.2), run_time = 0.125))
                self.play(ReplacementTransform(Vector(vector_sum[(i,j)]), Dot(vector_sum[(i,j)])), run_time = 0.125)


        self.wait(5)

