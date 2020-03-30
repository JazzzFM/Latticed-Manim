from manimlib.imports import *

class Redes(Scene):
    def construct(self):
        twitter = Twitter().set_fill("#12C0FF").set_stroke("#12C0FF").scale(0.6)
        facebook = Facebook().set_fill("#3C5A9A").set_stroke("#3C5A9A").scale(0.6)
        github = GitHub()
        youtube=YouTube().set_fill("#FE0000").set_stroke("#FE0000").scale(0.6)
        facebook.shift(LEFT*2)
        github.set_height(facebook.get_height()).scale(0.96)
        twitter.next_to(facebook,LEFT,buff=1)
        youtube.next_to(facebook,RIGHT,buff=1)
        github.next_to(youtube,RIGHT,buff=1)
        redes_s=VGroup(twitter,facebook,youtube,github)
        redes_s.move_to(ORIGIN)
        redes_f=redes_s.copy()
        redes_f.arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=0.4
            )
        texto=VGroup(
            TextMobject("\\tt twitter").match_color(twitter),
            TextMobject("\\tt facebook").match_color(facebook),
            TextMobject("\\tt youtube").match_color(youtube),
            TextMobject("\\tt github").match_color(github)
            )
        redes_f.to_edge(LEFT).scale(0.7).shift(LEFT*0.7)
        for i in range(len(texto)):
            texto[i].next_to(redes_f[i],RIGHT,buff=0.8)


        self.play(DrawBorderThenFill(redes_s),run_time=3)
        self.play(ReplacementTransform(redes_s,redes_f))
        self.wait(0.1)
        self.add_foreground_mobject(redes_f)
        circles=VGroup(*[Dot(redes_f[i].get_center(),color=WHITE,radius=twitter.get_width()*0.5).scale(0.9)for i in range(len(redes_f)-1)])
        texto.shift(RIGHT*2)
        punto=Dot(redes_f.get_center()).shift(RIGHT*2)
        vector=punto.get_center()[0]-redes_f.get_center()[0]
        circles.set_fill(None,0)
        self.add(circles)
        def update(grupo):
            for i in range(len(grupo)):
                grupo[i].move_to(redes_f[i].get_center())
                dif=(punto.get_center()[0]-grupo.get_center()[0])
                grupo.set_fill(WHITE,smooth(1-dif/vector))
            return grupo

        #self.play(FadeIn(circles))
        self.play(redes_f.shift,RIGHT*2,
            UpdateFromFunc(circles,update),
            *[Escribe(texto[i],color_orilla=texto[i].get_color(),factor_desvanecimiento=8,stroke_width=0.7)for i in range(len(texto))])
        circles.set_fill(WHITE,1)
        self.add(circles)
        redes_fc=redes_f.copy()
        redes_fc.set_fill(opacity=0)
        redes_fc.set_stroke(WHITE,3)
        redes_fc[-1].set_stroke(BLACK,1.5)
        
        
        for x in range(2):
            self.play(
                ShowPassingFlash(redes_fc=x, 
                    time_width = 0.5,
                    run_time = 2,
                    rate_func=linear
                )
            )
        
        self.wait()
