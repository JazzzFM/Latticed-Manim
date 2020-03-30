from manimlib.imports import *

class Example(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        sphere=Sphere()
        axes = ThreeDAxes()
        self.add(sphere,axes)
        self.move_camera(frame_center=RIGHT*3) # <-- does not do what expected
        self.wait(3)
