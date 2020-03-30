from manimlib.imports import *

class NameColumnSpace(Scene):
    def construct(self):
        matrix = Matrix(np.array([
            [1, 1, 0],
            [0, 1, 1],
            [-1, -2, -1],
        ]).T)
        matrix.set_column_colors(X_COLOR, Y_COLOR, Z_COLOR)
        matrix.to_corner(UP+LEFT)
        cols = list(matrix.copy().get_mob_matrix().T)
        col_arrays = list(map(Matrix, cols))

        span_text = TexMobject(
            "\\text{Span}", 
            "\\Big(",
            matrix_to_tex_string([1, 2, 3]),
            ",",
            matrix_to_tex_string([1, 2, 3]),
            ",",
            matrix_to_tex_string([1, 2, 3]),
            "\\big)"
        )
        for i in 1, -1:
            span_text[i].stretch(1.5, 1)
            #span_text[i].do_in_place(
             #   span_text[i].set_height, 
              #  span_text.get_height()
            #)
        for col_array, index in zip(col_arrays, [2, 4, 6]):
            col_array.replace(span_text[index], dim_to_match = 1)
            span_text.submobjects[index] = col_array
        span_text.arrange(RIGHT, buff = 0.2)

        arrow = DoubleArrow(LEFT, RIGHT)
        column_space = TextMobject("``Column space''")
        for mob in column_space, arrow:
            mob.set_color(TEAL)
        text = VMobject(span_text, arrow, column_space)
        text.arrange(RIGHT)
        text.next_to(matrix, DOWN, buff = 1, aligned_edge = LEFT)

        self.add(matrix)
        self.wait()
        self.play(*[
            Transform(
                VMobject(*matrix.copy().get_mob_matrix()[:,i]),
                col_arrays[i].get_entries()
            )
            for i in range(3)
        ])
        self.play(
            Write(span_text),
            *list(map(Animation, self.get_mobjects_from_last_animation()))
        )
        self.play(
            ShowCreation(arrow),
            Write(column_space)
        )
        self.wait()
        self.play(FadeOut(matrix))
        self.clear()
        self.add(text)

        words = TextMobject(
            "To solve", 
            "$A\\vec{\\textbf{x}} = \\vec{\\textbf{v}}$,\\\\",
            "$\\vec{\\textbf{v}}$", 
            "must be in \\\\ the",
            "column space."
        )
        VMobject(*words[1][1:3]).set_color(PINK)
        VMobject(*words[1][4:6]).set_color(YELLOW)
        words[2].set_color(YELLOW)
        words[4].set_color(TEAL)
        words.to_corner(UP+LEFT)

        self.play(Write(words))
        self.wait(2)
        self.play(FadeOut(words))

        brace = Brace(column_space, UP)
        rank_words = brace.get_text(
            "Number of dimensions \\\\ is called",
            "``rank''"
        )
        rank_words[1].set_color(MAROON)
        self.play(
            GrowFromCenter(brace),
            Write(rank_words)
        )
        self.wait()
        self.cycle_through_span_possibilities(span_text)

    def cycle_through_span_possibilities(self, span_text):
        span_text.save_state()
        two_d_span = span_text.copy()
        for index, arr, c in (2, [1, 1], X_COLOR), (4, [0, 1], Y_COLOR):
            col = Matrix(arr)
            col.replace(two_d_span[index])
            two_d_span.submobjects[index] = col
            col.get_entries().set_color(c)
        for index in 5, 6:
            two_d_span[index].scale(0)
        two_d_span.arrange(RIGHT, buff = 0.2)
        two_d_span[-1].next_to(two_d_span[4], RIGHT, buff = 0.2)
        two_d_span.move_to(span_text, aligned_edge = RIGHT)
        mob_matrix = np.array([
            two_d_span[i].get_entries().split()
            for i in (2, 4)
        ])

        self.play(Transform(span_text, two_d_span))
        #horrible hack
        span_text.shift(10*DOWN)
        span_text = span_text.copy().restore()
        ###
        self.add(two_d_span)
        self.wait()
        self.replace_number_matrix(mob_matrix, [[1, 1], [1, 1]])
        self.wait()
        self.replace_number_matrix(mob_matrix, [[0, 0], [0, 0]])
        self.wait()
        self.play(Transform(two_d_span, span_text))
        self.wait()
        self.remove(two_d_span)
        self.add(span_text)
        mob_matrix = np.array([
            span_text[i].get_entries().split()
            for i in (2, 4, 6)
        ])
        self.replace_number_matrix(mob_matrix, [[1, 1, 0], [0, 1, 1], [1, 0, 1]])
        self.wait()
        self.replace_number_matrix(mob_matrix, [[1, 1, 0], [0, 1, 1], [-1, -2, -1]])
        self.wait()
        self.replace_number_matrix(mob_matrix, [[1, 1, 0], [2, 2, 0], [3, 3, 0]])
        self.wait()
        self.replace_number_matrix(mob_matrix, np.zeros((3, 3)).astype('int'))
        self.wait()


    def replace_number_matrix(self, matrix, new_numbers):
        starters = matrix.flatten()
        targets = list(map(TexMobject, list(map(str, np.array(new_numbers).flatten()))))
        for start, target in zip(starters, targets):
            target.move_to(start)
            target.set_color(start.get_color())
        self.play(*[
            Transform(*pair, path_arc = np.pi)
            for pair in zip(starters, targets)
        ])
