class Vectorco(VectorScene):
    def construct(self):
        plane=Numberplane()
        axes=Axes(tick_frequency=1)
        axes.set_color(YELLOW)
        vector=Vector(RIGHT+2*UP,color=PURPLE)
        coordinates=vector_coordinare_label(vector)
        self.add(plane)
        self.add(axes)
        self.play(Write(vector),Write(coordinates))
