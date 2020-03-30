from manimlib.imports import *

class NameParallelepiped(Scene):
    def construct(self):
        word = TextMobject("``Parallelepiped''")
        word.scale(2)
        pp_part1 = VMobject(*word.split()[:len(word.split())/2])
        pp_part2 = VMobject(*word.split()[len(word.split())/2:])
        pp_part1.set_submobject_colors_by_gradient(X_COLOR, Y_COLOR)
        pp_part2.set_submobject_colors_by_gradient(Y_COLOR, Z_COLOR)
        self.play(Write(word))
        self.wait(2)

class DeterminantIsVolumeOfParallelepiped(Scene):
    def construct(self):
        matrix = Matrix([[1, 0, 0.5], [0.5, 1, 0], [1, 0, 1]])
        matrix.shift(3*LEFT)
        matrix.set_column_colors(X_COLOR, Y_COLOR, Z_COLOR)
        det_text = get_det_text(matrix)
        eq = TexMobject("=")
        eq.next_to(det_text, RIGHT)
        words = TextMobject([
            "Volume of this\\\\",
            "parallelepiped"
        ])
        pp = words.split()[1]
        pp_part1 = VMobject(*pp.split()[:len(pp.split())/2])
        pp_part2 = VMobject(*pp.split()[len(pp.split())/2:])
        pp_part1.set_submobject_colors_by_gradient(X_COLOR, Y_COLOR)
        pp_part2.set_submobject_colors_by_gradient(Y_COLOR, Z_COLOR)

        words.next_to(eq, RIGHT)

        self.play(Write(matrix))
        self.wait()
        self.play(Write(det_text), Write(words), Write(eq))
        self.wait()

