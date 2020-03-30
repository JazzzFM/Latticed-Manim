from manimlib.imports import *

class AudioTest(Scene):
    def construct(self):
        group_dots=VGroup(*[Dot()for _ in range(3)])
        group_dots.arrange_submobjects(RIGHT)
        for dot in group_dots:
            self.add_sound("click",gain=-10)
            self.add(dot)
            self.wait()
        self.wait()
 
class SVGTest(Scene):
    def construct(self):
        svg = SVGMobject("T_ciberseguridad")
        #svg = SVGMobject("camera")
        self.play(DrawBorderThenFill(svg,rate_func=linear))
        self.wait()
 
class ImageTest(Scene):
    def construct(self):
        image1 = ImageMobject("CIBERSEG")
        image2 = ImageMobject("T_ciberseguridad")
        image3 = ImageMobject("cicipn")

        
        image1.move_to(LEFT*3 + UP*2)
        self.play(GrowFromCenter(image1, color = BLUE))
        self.wait(0.5)
        
        image3.move_to(LEFT)
        self.play(GrowFromCenter(image3, color = BLUE))
        self.wait(0.5)

        image2.move_to(RIGHT*2 + DOWN*2)
        self.play(GrowFromCenter(image2, color = BLUE))
        self.wait(0.5)

        
        self.wait()
