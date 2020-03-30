from manimlib.imports import *

class LinearTransformation(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "foreground_plane_kwargs": {
            "x_radius": FRAME_WIDTH,
            "y_radius": FRAME_WIDTH,
            "secondary_line_ratio": 0
        },
        "background_plane_kwargs": {
            "color": BLUE,
            "secondary_color": DARK_GREY,
            "axes_color": GREY,
            "stroke_width": 2,
        },
        "show_coordinates": True,
        "show_basis_vectors": False,
        "basis_vector_stroke_width": 6,
        "i_hat_color": X_COLOR,
        "j_hat_color": Y_COLOR,
        "leave_ghost_vectors": False,
    }

    def construct(self):
         center = np.array([[1], [1]])
         v_1 = np.array([[0.5], [2]])
         v_2 = np.array([[1], [0]])
         v_3 = center + v_2
         suma = center + v_1
         Dot = v_1

         self.add_vector(center, color = RED)
         self.add_vector(v_3, color = GREEN)
         self.add_vector(suma, color = ORANGE)
         self.add_play 


         self.wait(5)

