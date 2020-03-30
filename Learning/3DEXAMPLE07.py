from manimlib.imports import *
def stereo_project_point(point, axis=0, r=1, max_norm=10000):
    point = fdiv(point * r, point[axis] + r)
    point[axis] = 0
    norm = get_norm(point)
    if norm > max_norm:
        point *= max_norm / norm
    return point


def stereo_project(mobject, axis=0, r=1, outer_r=10, **kwargs):
    epsilon = 1
    for submob in mobject.family_members_with_points():
        points = submob.points
        n = len(points)
        for i in range(n):
            if points[i, axis] == -r:
                js = it.chain(
                    range(i + 1, n),
                    range(i - 1, -1, -1)
                )
                for j in js:
                    if points[j, axis] == -r:
                        continue
                    else:
                        vect = points[j] - points[i]
                        points[i] += epsilon * vect
                        break
        submob.apply_function(
            lambda p: stereo_project_point(p, axis, r, **kwargs)
        )

        # If all points are outside a certain range, this
        # shouldn't be displayed
        norms = np.apply_along_axis(get_norm, 1, submob.points)
        if np.all(norms > outer_r):
            # TODO, instead set opacity?
            # submob.points[:, :] = 0
            submob.set_fill(opacity=0)
            submob.set_stroke(opacity=0)

    return mobject


class Linus(VGroup):
    CONFIG = {
        "body_config": {
            "stroke_width": 15,
            "stroke_color": LIGHT_GREY,
            "sheen": 0.4,
        },
        "height": 2,
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.body = self.get_body_line()
        self.eyes = Eyes(self.body)

        self.add(self.body, self.eyes)
        self.set_height(self.height)
        self.center()

    def change_mode(self, mode, thing_to_look_at=None):
        self.eyes.change_mode(mode, thing_to_look_at)
        if mode == "sad":
            self.become_squiggle()
        elif mode == "confused":
            self.become_squiggle(factor=-0.1)
        elif mode == "pleading":
            self.become_squiggle(factor=0.3)
        else:
            self.become_line()
        return self

    def change(self, *args, **kwargs):
        self.change_mode(*args, **kwargs)
        return self

    def look_at(self, thing_to_look_at=None):
        self.eyes.look_at(thing_to_look_at)
        return self

    def blink(self):
        self.eyes.blink()
        return self

    def get_squiggle(self, factor=0.2):
        sine_curve = FunctionGraph(
            lambda x: factor * np.sin(x),
            x_min=0, x_max=TAU,
        )
        sine_curve.rotate(TAU / 4)
        sine_curve.match_style(self.body)
        sine_curve.match_height(self.body)
        sine_curve.move_to(self.body, UP)
        return sine_curve

    def get_body_line(self, **kwargs):
        config = dict(self.body_config)
        config.update(kwargs)
        line = Line(ORIGIN, 1.5 * UP, **config)
        if hasattr(self, "body"):
            line.match_style(self.body)
            line.match_height(self.body)
            line.move_to(self.body, UP)
        return line

    def become_squiggle(self, **kwargs):
        self.body.become(self.get_squiggle(**kwargs))
        return self

    def become_line(self, **kwargs):
        self.body.become(self.get_body_line(**kwargs))
        return self

    def copy(self):
        return self.deepcopy()


class Felix(PiCreature):
    CONFIG = {
        "color": GREEN_D
    }


class PushPin(SVGMobject):
    CONFIG = {
        "file_name": "push_pin",
        "height": 0.5,
        "sheen": 0.7,
        "fill_color": GREY,
    }

    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.rotate(20 * DEGREES)

    def pin_to(self, point):
        self.move_to(point, DR)


class Hand(SVGMobject):
    CONFIG = {
        "file_name": "pinch_hand",
        "height": 0.5,
        "sheen": 0.2,
        "fill_color": ORANGE,
    }

    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        # self.rotate(30 * DEGREES)
        self.add(VectorizedPoint().next_to(self, UP, buff=0.17))


class CheckeredCircle(Circle):
    CONFIG = {
        "n_pieces": 16,
        "colors": [BLUE_E, BLUE_C],
        "stroke_width": 5,
    }

    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)
        pieces = self.get_pieces(self.n_pieces)
        self.points = np.zeros((0, 3))
        self.add(*pieces)
        n_colors = len(self.colors)
        for i, color in enumerate(self.colors):
            self[i::n_colors].set_color(color)

class StereoProjectedSphere(Sphere):
    CONFIG = {
        "stereo_project_config": {
            "axis": 2,
        },
        "max_r": 32,
        "max_width": FRAME_WIDTH,
        "max_height": FRAME_WIDTH,
        "max_depth": FRAME_WIDTH,
        "radius": 1,
    }

    def __init__(self, rotation_matrix=None, **kwargs):
        digest_config(self, kwargs)
        if rotation_matrix is None:
            rotation_matrix = np.identity(3)
        self.rotation_matrix = rotation_matrix

        self.stereo_project_config["r"] = self.radius
        ParametricSurface.__init__(
            self, self.post_projection_func, **kwargs
        )
        self.submobjects.sort(
            key=lambda m: -m.get_width()
        )
        self.fade_far_out_submobjects()

    def post_projection_func(self, u, v):
        point = self.radius * Sphere.func(self, u, v)
        rot_point = np.dot(point, self.rotation_matrix.T)
        result = stereo_project_point(
            rot_point, **self.stereo_project_config
        )
        epsilon = 1e-4
        if np.any(np.abs(result) == np.inf) or np.any(np.isnan(result)):
            return self.func(u + epsilon, v)
        return result

    def fade_far_out_submobjects(self, **kwargs):
        max_r = kwargs.get("max_r", self.max_r)
        max_width = kwargs.get("max_width", self.max_width)
        max_height = kwargs.get("max_height", self.max_height)
        max_depth = kwargs.get("max_depth", self.max_depth)
        for submob in self.submobjects:
            violations = [
                np.any(np.apply_along_axis(get_norm, 1, submob.get_anchors()) > max_r),
                submob.get_width() > max_width,
                submob.get_height() > max_height,
                submob.get_depth() > max_depth
            ]
            if any(violations):
                # self.remove(submob)
                submob.fade(1)
        return self

class StereoProjectedSphereFromHypersphere(StereoProjectedSphere):
    CONFIG = {
        "stereo_project_config": {
            "axis": 0,
        },
        "radius": 2,
        "multiply_from_right": False,
    }

    def __init__(self, quaternion=None, null_axis=0, **kwargs):
        if quaternion is None:
            quaternion = np.array([1, 0, 0, 0])
        self.quaternion = quaternion
        self.null_axis = null_axis
        ParametricSurface.__init__(self, self.q_mult_projection_func, **kwargs)
        self.fade_far_out_submobjects()

    def q_mult_projection_func(self, u, v):
        point = list(Sphere.func(self, u, v))
        point.insert(self.null_axis, 0)
        if self.multiply_from_right:
            post_q_mult = q_mult(point, self.quaternion)
        else:
            post_q_mult = q_mult(self.quaternion, point)
        projected = list(self.radius * stereo_project_point(
            post_q_mult, **self.stereo_project_config
        ))
        if np.any(np.abs(projected) == np.inf):
            return self.func(u + 0.001, v)
        ignored_axis = self.stereo_project_config["axis"]
        projected.pop(ignored_axis)
        return np.array(projected)
class RotateCubeThreeTimes(SpecialThreeDScene):
    def construct(self):
        cube = RubiksCube()
        cube.set_fill(opacity=0.8)
        cube.set_stroke(width=1)
        randy = Randolph(mode="pondering")
        randy.set_height(cube.get_height() - 2 * SMALL_BUFF)
        randy.move_to(cube.get_edge_center(OUT))
        randy.set_fill(opacity=0.8)
        # randy.set_shade_in_3d(True)
        cube.add(randy)
        axes = self.get_axes()

        self.add(axes, cube)
        self.move_camera(
            phi=70 * DEGREES,
            theta=-140 * DEGREES,
        )
        self.begin_ambient_camera_rotation(rate=0.02)
        self.wait(2)
        self.play(Rotate(cube, TAU / 4, RIGHT, run_time=3))
        self.wait(2)
        self.play(Rotate(cube, TAU / 4, UP, run_time=3))
        self.wait(2)
        self.play(Rotate(cube, -TAU / 3, np.ones(3), run_time=3))
        self.wait(7)

#class StereoProjectedSphereFromHypersphere(StereoProjectedSphere):
#   CONFIG = {
#      "stereo_project_config": {
#            "axis": 0,
#        },
#        "radius": 2,
#        "multiply_from_right": False,
#    }
#
#    def __init__(self, quaternion=None, null_axis=0, **kwargs):
#        if quaternion is None:
#            quaternion = np.array([1, 0, 0, 0])
#        self.quaternion = quaternion
#        self.null_axis = null_axis
#        ParametricSurface.__init__(self, self.q_mult_projection_func, **kwargs)
#        self.fade_far_out_submobjects()
#
#    def q_mult_projection_func(self, u, v):
#        point = list(Sphere.func(self, u, v))
#        point.insert(self.null_axis, 0)
#        if self.multiply_from_right:
#            post_q_mult = q_mult(point, self.quaternion)
#        else:
#            post_q_mult = q_mult(self.quaternion, point)
#        projected = list(self.radius * stereo_project_point(
#            post_q_mult, **self.stereo_project_config
#        ))
#        if np.any(np.abs(projected) == np.inf):
#            return self.func(u + 0.001, v)
#        ignored_axis = self.stereo_project_config["axis"]
#   projected.pop(ignored_axis)
#        return np.array(projected)

#class RotationsIn3d(SpecialThreeDScene):
#    def construct(self):
#        self.set_camera_orientation(**self.get_default_camera_position())
#        self.begin_ambient_camera_rotation(rate=0.02)
#        sphere = self.get_sphere()
#        vectors = VGroup(*[
#            Vector(u * v, color=color).next_to(sphere, u * v, buff=0)
#            for v, color in zip(
#                [RIGHT, UP, OUT],
#                [GREEN, RED, BLUE],
#            )
#            for u in [-1, 1]
#        ])
#        vectors.set_shade_in_3d(True)
#        sphere.add(vectors)
#
#        self.add(self.get_axes())
#        self.add(sphere)
#        angle_axis_pairs = [
#            (90 * DEGREES, RIGHT),
#            (120 * DEGREES, UR),
#            (-45 * DEGREES, OUT),
#            (60 * DEGREES, IN + DOWN),
#            (90 * DEGREES, UP),
#            (30 * DEGREES, UP + OUT + RIGHT),
#        ]
#        for angle, axis in angle_axis_pairs:
#            self.play(Rotate(
#                sphere, angle,
#                axis=axis,
#                run_time=2,
#            ))
#            self.wait()
