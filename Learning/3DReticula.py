from manimlib.imports import *

class ThreeDReticula(ThreeDScene):
    def construct(self):
        def points(center):
            sphere = ParametricSurface(
            lambda u, v: np.array([
                0.08*np.cos(u)*np.cos(v) + center[0],
                1.5*np.cos(u)*np.sin(v) + center[1],
                1.5*np.sin(u) + center[2]
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)
            self.play(Write(sphere), run_time = 0.2)

        def tarugo3D(center, base0, base1, base2):
            v_0 = ((center + base0) + base1) + base2
            v_1 = (center + base1) + base2
            v_2 = center + base2
            v_3 = (center + base0) + base2
            v_4 = (center + base0) + base1
            v_5 = center + base1
            v_6 = center
            v_7 = center + base0
            points(v_0)
            points(v_1)
            points(v_2)
            points(v_3)
            points(v_4)
            points(v_5)
            points(v_6)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70 * DEGREES,theta=-45*DEGREES)
        self.add(axes)

        center = np.array([0.0, 0.0, 0.0])
        Base0  = np.array([1.0, 0.0, 0.5])
        Base1  = np.array([0.0, 1.0, 0.5])
        Base2  = np.array([0.0, 0.0, 1.0])

        #torus(center)
        for i in range(-1, 1):
            for j in range(-1, 1):
                for k in range(0, 1):
                    tarugo3D(center + (i * Base0) + (j * Base1) + (k * Base2), Base0, Base1, Base2)
        
        self.wait(0.1)
