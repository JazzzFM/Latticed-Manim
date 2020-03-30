from manimlib.imports import *

class ChangePointRotation(ThreeDScene):
    def construct(self):
        axis=ThreeDAxes()
        self.add(axis)
        phi_init=70 * DEGREES
        theta_init=-135 * DEGREES
        self.set_camera_orientation(phi=phi_init,theta=theta_init)
 
        self.begin_ambient_camera_rotation(rate=0.7)
        self.wait(5)
        self.stop_ambient_camera_rotation()
 
        self.wait()
 
        vector=np.array([-2,-3,1])
 
 
        cx=vector[0]*RIGHT
        cy=vector[1]*UP
        cz=vector[2]*OUT
        dashed_lines=VGroup()
        for ci,cf in zip([cx,cy,cx+cy,cz],[cx+cy,cx+cy,cx+cy+cz,cx+cy+cz]):
            dashed_lines.add(DashedLine(ci,cf))
        dashed_lines.set_color(RED)
 
        sphere=Sphere(radius=0.07, color = WHITE).move_to(vector)
 
        self.play(ShowCreation(sphere))
 
        self.play(ShowCreation(dashed_lines))
 
        self.wait(2)
 
        self.move_camera(theta=theta_init,phi=phi_init)
        self.wait()
 
        self.move_camera(distance=self.camera.distance,
            frame_center=vector
            )
 
        self.wait()
 
        self.begin_ambient_camera_rotation(rate=0.7)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait()

class Plot(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : -10,
        "x_max" : 20,
        "x_min" : -20,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2,  
                                    color = GREEN,
                                    x_min = 0, 
                                    x_max = 7
                                    )
        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()
        self.play(FadeOut(self.axes))
        self.wait()

class Plot2(Scene):
    def construct(self):
        c1 = FunctionGraph(lambda x: 2*np.exp(-2*(x-1)**2))
        c2 = FunctionGraph(lambda x: x**2)
        axes1=Axes(y_min=-200,y_max=10)
        axes2=Axes(y_min=20,y_max=10)
        self.play(ShowCreation(axes1),ShowCreation(c1))
        self.wait()
        self.play(
            ReplacementTransform(axes1,axes2),
            ReplacementTransform(c1,c2)
        )
        self.wait()
