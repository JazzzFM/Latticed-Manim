from manimlib.imports import *

class VectorsToDotsScene(VectorScene):
    CONFIG = {
        "num_vectors" : 16,
        "start_color" : PINK,
        "end_color" : BLUE_E,
    }
    def construct(self):
        self.lock_in_faded_grid()

        vectors = self.get_vectors()
        colors = Color(self.start_color).range_to(
            self.end_color, len(vectors)
        )
        for vect, color in zip(vectors, colors):
            vect.set_color(color)

        #a = int((3*len(vectors)/4))
        prototype_vector = vectors[0]

        vector_group = VMobject(*vectors)
        self.play(
            ShowCreation(
                vector_group,
                run_time = 3
            )
        )
        vectors.sort(key=lambda v: v.get_length())
        self.add(*vectors)
        def v_to_dot(vector):
            return Dot(vector.get_end(), fill_color = vector.get_stroke_color())
        self.wait()
        vectors.remove(prototype_vector)
        self.play(*list(map(FadeOut, vectors))+[Animation(prototype_vector)])
        self.remove(vector_group)
        self.add(prototype_vector)
        self.wait()
        self.play(Transform(prototype_vector, v_to_dot(prototype_vector)))
        self.wait()
        self.play(*list(map(FadeIn, vectors)) + [Animation(prototype_vector)])
        rate_functions = [
            squish_rate_func(smooth, float(x)/(len(vectors)+2), 1)
            for x in range(len(vectors))
        ]
        self.play(*[
            Transform(v, v_to_dot(v), rate_func = rf, run_time = 2)
            for v, rf in zip(vectors, rate_functions)
        ])
        self.wait()
        self.remove(prototype_vector)
        self.play_final_animation(vectors, rate_functions)
        self.wait()

    def get_vectors(self):
        raise Exception("Not implemented")

    def play_final_animation(self, vectors, rate_functions):
        raise Exception("Not implemented")

class VectorsOnALine(VectorsToDotsScene):
    def get_vectors(self):
        return [
            Vector(a*np.array([1.5, 1]))
            for a in np.linspace(
                -FRAME_Y_RADIUS, FRAME_Y_RADIUS, self.num_vectors
            )
        ]

    def play_final_animation(self, vectors, rate_functions):
        line_copies = [
            Line(vectors[0].get_end(), vectors[-1].get_end())
            for v in vectors
        ]
        self.play(*[
            Transform(v, mob, rate_func = rf, run_time = 2)
            for v, mob, rf in zip(vectors, line_copies, rate_functions)
        ])


