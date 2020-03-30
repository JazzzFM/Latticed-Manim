# python3.7 -m manim Learning/Firstplane.py LinearTransformation -pm
from manimlib.imports import *

class FirstLattice(LinearTransformationScene):
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
      
        v_1 = np.array([[1], [2]])
        self.add_vector(v_1, color = RED)
        v_2 = np.array([[-1], [0.5]])
        self.add_vector(v_2, color = GREEN)


        vectors1 = {}
        vectors2 = {}
        vectors1[1] = v_1
        vectors2[1] = v_2

        for i in range(1, 5):
            vectors1[i+1] = i * v_1
            vectors2[i+1] = i * v_2
            self.add_vector(vectors1[i+1], color = RED)
            #self.play(FadeOut(vectors1[i+1]))
            self.add_vector(vectors2[i+1], color = GREEN)
            #self.play(FadeIn(Dot(vectors1[i+1])))
           # self.play(FadeOut(vectors2[i+1]))

       
       
        vector_sum = {}
        vector_sum[1] = v_1 + v_2
        self.add_vector(vector_sum[1], color = ORANGE)

        for j in range (-3, 3):
            for i in range (-3, 3):
                vector_sum[i+j+1] = (i * v_1) + (j*v_2)
                self.add_vector(vector_sum[i+j+1], color = ORANGE)
    
       



        self.wait(6)

