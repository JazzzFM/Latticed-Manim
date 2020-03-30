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



def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords

class ConstLattice(Scene):
    def construct(self):
        m = []
        n = []

        for i in range(2):
            i = float( input("Ingrese los escalares del primer vector, entrada ["+str(i+1)+"] : "))
            m.append(i)
        print("")

        for j in range(2):
            j = float( input("Ingrese los escalares del segundo vector, entrada ["+str(j+1)+"] : "))
            n.append(j)
        
        n.append(0) 
        m.append(0)

        v_1 = np.array(m)
        v_2 = np.array(n)
        
        screen_grid = ScreenGrid()
        self.add(screen_grid)
        
        self.play(FadeIn(Vector(v_1, color = BLUE)))
        self.play(FadeIn(Vector(v_2, color = GREEN)))

        vectors1 = {}
        vectors2 = {}
        
        #coords = get_coords_from_csv("../custom_graphs/data")
        #dots = self.get_dots_from_coords(coords)
        #self.add(dots)



        for i in range(-3, 3):
            vectors1[i] = i * v_1
            vectors2[i] = i * v_2
            self.play( FadeIn( Vector(vectors1[i], color = BLUE, stroke = 0.09), run_time = 0.125) )
            self.play( ReplacementTransform(Vector(vectors1[i]), Dot(vectors1[i])), run_time = 0.125 )
            self.play( FadeIn(Vector(vectors2[i], color = GREEN, stroke = 0.09), run_time = 0.125) )
            #self.play( ReplacementTransform(Vector(vectors2[i]),  Dot(vectors2[i])), run_time = 0.125 )

        vector_sum = {}

        for j in reversed(range(-3, 3)):
            for i in reversed(range(-3, 3)):
                vector_sum[(i,j)] = (i * v_1) + (j * v_2)
                self.play(FadeIn(Vector(vector_sum[(i,j)], color = ORANGE, stroke = 0.09), run_time = 0.125))
                #self.play(ReplacementTransform(Vector(vector_sum[(i,j)]), Dot(vector_sum[(i,j)])), run_time = 0.125)

# NO he logrado hacer que los arreglos comentados funcionen en Dot.

        self.wait(5)


