from manimlib.imports import *

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "include_background_plane": False,
        "include_foreground_plane": False,
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
        "show_coordinates": False,
        "show_basis_vectors": False,
        "basis_vector_stroke_width": 6,
        "i_hat_color": X_COLOR,
        "j_hat_color": Y_COLOR,
        "leave_ghost_vectors": False,
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.125,
        "labels_buff": 0,
        "number_decimals": 0
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)

def InputVectors():
    m = []
    a_1 = float(input("Ingrese los escalares del vector, entrada ["+str(1)+"] : "))
    m.append(a_1)
    a_2 = float(input("Ingrese los escalares del vector, entrada ["+str(2)+"] : "))
    m.append(a_2)
    m.append(0)
    print("\n")
    return np.array(m)

def Polygon3D(listOfPoints, aes_color = RED,opacity = 0.5):
    H1 =   listOfPoints
    H2 =   []
    
    for i in range(len(H1)):
        H2.append([H1[i][0],H1[i][1],H1[i][2]])
            
    S=[]

    for i in range(len(H2)-1):
        s1= [(H2[i][0],H2[i][1],H2[i][2]),
            (H2[i+1][0],H2[i+1][1],H2[i+1][2]),
            (H2[i+1][0],H2[i+1][1],H1[i+1][2]),
            (H2[i][0],H2[i][1],H1[i][2])]
        S.append(Polygon(*s1,fill_color=aes_color, fill_opacity=opacity, color=aes_color,stoke_width=0.1))

    b = Polygon(*H1,fill_color=aes_color, fill_opacity=opacity, color=aes_color,stoke_width=0.1)
    h = Polygon(*H2,fill_color=aes_color, fill_opacity=opacity, color=aes_color,stoke_width=0.1)
    s = VGroup(*S)
    poly3D = VGroup(*[b,h,s])
    return poly3D



class DefLattice(Scene):
    def construct(self):
        plane = ScreenGrid()
        self.add(plane)

        v_1 = InputVectors()
        v_2 = InputVectors()
        v_3 = v_1 + v_2
        center = np.array([0, 0, 0])

        self.play(FadeIn(Vector(v_1, color = GREEN)))
        self.play(FadeIn(Vector(v_3, color = RED)))
      
        for i in range(-20, 20):
            for j in range(-20, 20):
                center2 = center + (i * v_1) + (j * v_3)
                suma0 = center2 + v_1
                suma1 = center2 + v_3
                suma2 = center2 + v_1 + v_3
                self.add(plane, Dot(suma0))
                self.add(plane, Dot(suma1))
                self.add(plane, Dot(center2))
                self.add(plane, Dot(suma2))
       
        DomFund =   [center,   #P1
                    v_1,    #P2
                    v_1 + v_3, 
                    v_3#P4
                    ]

        DrawDomFund = Polygon3D(DomFund)
        self.play(ShowCreation(DrawDomFund))


        self.wait(5)

