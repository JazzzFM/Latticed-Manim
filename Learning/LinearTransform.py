from manimlib.imports import *

class LinearTransformation(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "foreground_plane_kwargs": {
            "x_radius": FRAME_WIDTH,
            "y_radius": FRAME_HEIGHT,
            "secondary_line_ratio": 0
        },
        "background_plane_kwargs": {
            "color": GREY,
            "secondary_color": DARK_GREY,
            "axes_color": GREY,
            "stroke_width": 2,
        },
        "show_coordinates": False,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 6,
        "i_hat_color": X_COLOR,
        "j_hat_color": Y_COLOR,
        "leave_ghost_vectors": False,
    }
    def construct(self):
        mob = Circle()
        mob.move_to(RIGHT+UP*2)
        vector_array = np.array([[1], [2]])
        matrix = [[0, 1], [-1, 1]]

        self.add_transformable_mobject(mob)

        self.add_vector(vector_array)

        self.apply_matrix(matrix)

        self.wait()


