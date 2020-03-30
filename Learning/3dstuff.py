from manimlib.imports import *

class Reticula3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70 * DEGREES,theta=-45*DEGREES)
        self.add(axes)
        
        base = {}
        points = {}
        base[0] = np.array([0.0, 0.0, 0.0])
        base[1] = np.array([1.0, 0.0, 0.5])
        base[2] = np.array([0.0, 1.0, 0.5])
        base[3] = np.array([0.0, 0.0, 1.0])
        
        def tarugo3D(center, base0, base1, base2):
            v = {}
            v[0] = ((center + base0) + base1) + base2
            v[1] = (center + base1) + base2
            v[2] = center + base2
            v[3] = (center + base0) + base2
            v[4] = (center + base0) + base1
            v[5] = center + base1
            v[6] = center
            v[7] = center + base0
            for i in range(-0, 8):
                points = {}
                points[i] = Sphere(radius=0.07, color = WHITE).move_to(center)
                self.play(Write(points[i]), run_time = 0.2)


        for i in range(-5, 5):
            for j in range(-5, 5):
                for k in range(-5, 5):
                    tarugo3D(base[0] + (i * base[1]) + (j * base[2]) + (k * base[3]), base[1], base[2], base[3])
        

        self.wait(20)
