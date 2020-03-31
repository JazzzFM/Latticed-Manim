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
                    label = Text(f"{coord_point}", font="Arial", stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)


#######################################################################################################################
#   Here we have the Reduction Algorithms in a Lattice

# matrix multiplication
def mat_mult(a, b):
    m = len(a)
    n = len(b[0])
    p = len(a[0])
    res = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            coeff = 0
            for k in range(p):
                coeff += a[i][k] * b[k][j]
            res[i][j] = coeff
    return res


# scalar product
def scalar_product(a, b):
    m = len(a)
    res = Fraction(0)
    for i in range(m):
        res += a[i] * b[i]
    return res


# display matrix
def print_mat(n):
    maxlen = 0
    for row in n:
        for f in row:
            if len(str(f)) > maxlen:
                maxlen = len(str(f))
    for row in n:
        row_str = ""
        for f in row:
            difflen = maxlen - len(str(f))
            sep = " "
            for i in range(difflen):
                sep = sep + " "
            row_str = row_str + sep + str(f)
        print(row_str)


# display vector
def print_vector(v):
    row_str = " ".join("%s" % i for i in v)
    print(row_str)


# get vector j in the matrix n
def get_vector(n, j):
    return [n[i][j] for i in range(len(n))]


# vector substraction
def vector_add(a, b):
    return [a[i] + b[i] for i in range(len(a))]


# vector substraction
def vector_sub(a, b):
    return [a[i] - b[i] for i in range(len(a))]


# vector multiplication with a constant
def vector_mult_const(v, k):
    return [v[i] * k for i in range(len(v))]


# set the k-th column of matrix n to the vector v
def set_matrix_vector(n, k, v):
    row = len(n)
    for i in range(row):
        n[i][k] = v[i]


# norml2 : square of the L2-norm of the vector x
def norml2(a):
    return scalar_product(a, a)


def create_matrix_from_knapsack(knap, the_sum):
    n = len(knap)
    result = [[Fraction(0) for j in range(n + 1)] for i in range(n + 1)]

    # identity matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                result[i][j] = Fraction(1)

    i = i + 1
    for k in range(n):
        result[i][k] = Fraction(knap[k])

    result[i][k + 1] = -Fraction(the_sum)
    return result


def roundp(num):
    if (num > 0):
        return int(num + Fraction(1, 2))
    else:
        return int(num - Fraction(1, 2))


def create_matrix(n):
    row = len(n)
    col = len(n[0])
    res = [[Fraction(n[i][j]) for j in range(col)] for i in range(row)]
    return res


# [ 0, 2, -1, ... , 0, 1 ] + [1, -2, 2, ..., 0, -1] = [ 1, 0, 1, ..., 0, 0]

def heuristic_u_plus_v(n):
    row = len(n)
    col = len(n[0])
    # negative vectors
    minus_1_tab = []
    # positive vectors
    plus_1_tab = []

    # this vector finishes with -1
    minus_1_vect = [0 for i in range(row)]
    # this vector finishes with 1
    plus_1_vect = [0 for i in range(row)]

    for i in range(col):
        if n[row - 1][i] == 1:
            for j in range(row):
                plus_1_vect[j] = int(n[j][i])

            if plus_1_vect not in plus_1_tab:
                plus_1_tab.append(plus_1_vect)

        elif n[row - 1][i] == -1:
            for j in range(row):
                minus_1_vect[j] = int(n[j][i])

            if minus_1_vect not in minus_1_tab:
                minus_1_tab.append(minus_1_vect)
    return vector_add(minus_1_vect, plus_1_vect)[:-1]


# retrieve the best vector for knapsack

def best_vect_knapsack(n):
    row = len(n)
    col = len(n[0])

    best_vect = [0 for i in range(row)]
    solution = [0 for i in range(row - 1)]

    for i in range(col):
        if n[row - 1][i] == 0:
            take_it = 1

            for j in range(row):
                if n[j][i] != Fraction(1):
                    if n[j][i] != Fraction(0):
                        take_it = 0

            if take_it:
                for j in range(row):
                    if n[j][i] == 1:
                        best_vect[j] = 1
                    elif n[j][i] == 0:
                        best_vect[j] = 0
                break;

    apply_heuristic = True
    for i in range(row):
        if best_vect[i] != 0:
            apply_heuristic = False

    if apply_heuristic:
        print("No existe solución directa, aplica la heuristica gaussiana")
        solution = heuristic_u_plus_v(n)
        for i in range(len(solution)):
            if solution[i] != 1:
                if solution[i] != 0:
                    # apply complement
                    print("No se encontró solución en la heuristica gaussiana")
                    return [0] * row
    else:
        for i in range(row - 1):
            solution[i] = best_vect[i]
    return solution


# gram schmidt algorithm

def gram_schmidt(g, m, mu, B):
    col = len(g[0])

    for i in range(col):
        # bi* = bi
        b_i = get_vector(g, i)
        b_i_star = b_i
        set_matrix_vector(m, i, b_i_star)

        for j in range(i):
            # u[i][j] = (bi, bj*)/Bj
            b_j_star = get_vector(m, j)
            b_i = get_vector(g, i)
            B[j] = norml2(b_j_star)
            mu[i][j] = Fraction(scalar_product(b_i, b_j_star), B[j])
            # bi* = bi* - u[i][j]* bj*
            b_i_star = vector_sub(b_i_star, vector_mult_const(b_j_star, mu[i][j]))
            set_matrix_vector(m, i, b_i_star)

        b_i_star = get_vector(m, i)
        # B[i] = (bi*, bi*)
        B[i] = scalar_product(b_i_star, b_i_star)


# reduce

def reduce(g, mu, k, l):
    row = len(g)

    if math.fabs(mu[k][l]) > Fraction(1, 2):
        r = roundp(mu[k][l])
        b_k = get_vector(g, k)
        b_l = get_vector(g, l)
        # bk = bk - r*bl
        set_matrix_vector(g, k, vector_sub(b_k, vector_mult_const(b_l, r)))

        for j in range(l):
            # u[k][j] = u[k][j] - r*u[l][j]
            mu[k][j] = mu[k][j] - r * mu[l][j]

        # u[k][l] = u[k][l] - r
        mu[k][l] = mu[k][l] - r


# lll_reduction from LLL book
def lll_reduction(n, lc=Fraction(3, 4)):
    row = len(n)
    col = len(n[0])

    m = [[Fraction(0) for j in range(col)] for i in range(row)]
    mu = [[Fraction(0) for j in range(col)] for i in range(col)]
    g = [[n[i][j] for j in range(col)] for i in range(row)]
    B = [Fraction(0) for j in range(col)]

    gram_schmidt(g, m, mu, B)

    # k = 2
    k = 1

    while 1:

        # 1 - perform (*) for l = k - 1
        reduce(g, mu, k, k - 1)

        # lovasz condition
        if B[k] < (lc - mu[k][k - 1] * mu[k][k - 1]) * B[k - 1]:
            # 2
            # u = u[k][k-1]
            u = mu[k][k - 1]

            # B = Bk + u^2*Bk-1
            big_B = B[k] + (u * u) * B[k - 1]

            # mu[k][k-1] = u * B[k-1] / B
            mu[k][k - 1] = u * Fraction(B[k - 1], big_B)

            # Bk = Bk-1 * Bk / B
            B[k] = Fraction(B[k - 1] * B[k], big_B)

            # Bk-1 = B
            B[k - 1] = big_B

            # exchange bk and bk-1
            b_k = get_vector(g, k)
            b_k_minus_1 = get_vector(g, k - 1)
            set_matrix_vector(g, k, b_k_minus_1)
            set_matrix_vector(g, k - 1, b_k)

            # for j = 0 .. k-2
            for j in range(k - 1):
                save = mu[k - 1][j]
                mu[k - 1][j] = mu[k][j]
                mu[k][j] = save

            for i in range(k + 1, col):
                save = mu[i][k - 1]
                mu[i][k - 1] = mu[k][k - 1] * mu[i][k - 1] + mu[i][k] - u * mu[i][k] * mu[k][k - 1]
                mu[i][k] = save - u * mu[i][k]

            # if k > 2
            if k > 1:
                k = k - 1

        else:
            for l in range(k - 2, -1, -1):
                reduce(g, mu, k, l)

            if k == col - 1:
                return g

            k = k + 1


# definition from the LLL book

def islll(n, lc=Fraction(3, 4)):
    row = len(n)
    col = len(n[0])

    m = [[Fraction(0) for j in range(col)] for i in range(row)]
    mu = [[Fraction(0) for j in range(col)] for i in range(col)]
    B = [Fraction(0) for j in range(col)]

    gram_schmidt(n, m, mu, B)

    for i in range(col):
        for j in range(i):
            if math.fabs(mu[i][j]) > Fraction(1, 2):
                return False

    for k in range(1, col):
        if B[k] < (lc - mu[k][k - 1] * mu[k][k - 1]) * B[k - 1]:
            return False
    return True


def Input2DVectors():
    m = []
    a_1 = float(input("Ingrese los escalares del vector base, entrada [" + str(1) + "] : "))
    m.append(a_1)
    a_2 = float(input("Ingrese los escalares del vector base, entrada [" + str(2) + "] : "))
    m.append(a_2)
    m.append(0)
    print("\n")
    return m


def Input3DVectors():
    m = []
    a_1 = float(input("Ingrese los escalares del vector base, entrada [" + str(1) + "] : "))
    m.append(a_1)
    a_2 = float(input("Ingrese los escalares del vector base, entrada [" + str(2) + "] : "))
    m.append(a_2)
    a_3 = float(input("Ingrese los escalares del vector base, entrada [" + str(3) + "] : "))
    m.append(a_3)
    print("\n")
    return m


def InputVectors():
    m = []
    a_1 = float(input("Ingrese los escalares del vector base, entrada [" + str(1) + "] : "))
    m.append(a_1)
    a_2 = float(input("Ingrese los escalares del vector base, entrada [" + str(2) + "] : "))
    m.append(a_2)
    m.append(0)
    print("\n")
    return np.array(m)


def InputVectors3D():
    m = []
    a_1 = float(input("Ingrese los escalares del vector base, entrada [" + str(1) + "] : "))
    m.append(a_1)
    a_2 = float(input("Ingrese los escalares del vector base, entrada [" + str(2) + "] : "))
    m.append(a_2)
    a_3 = float(input("Ingrese los escalares del vector base, entrada [" + str(3) + "] : "))
    m.append(a_3)
    print("\n")
    return np.array(m)


def InputVectors4D():
    m = []
    a_1 = float(input("Ingrese los escalares del vector base, entrada [" + str(1) + "] : "))
    m.append(a_1)
    a_2 = float(input("Ingrese los escalares del vector base, entrada [" + str(2) + "] : "))
    m.append(a_2)
    a_3 = float(input("Ingrese los escalares del vector base, entrada [" + str(3) + "] : "))
    m.append(a_3)
    a_4 = float(input("Ingrese los escalares del vector base, entrada [" + str(4) + "] : "))
    m.append(a_4)
    print("\n")
    return m


########################################################################################################################
# is already :D

class SpanLattice1D(Scene):
    def construct(self):
        screen_grid = ScreenGrid()
        self.add(screen_grid)
        v = InputVectors()

        self.play(FadeIn(Vector(v, color=BLUE)))
        vects = {}

        for i in range(-10, 10):
            vects[i] = i * v
            self.play(FadeIn(Vector(vects[i], color=BLUE, stroke=0.09), run_time=0.125))
            self.play(ReplacementTransform(Vector(vects[i]), Dot(vects[i])), run_time=0.125)

        self.wait(10)


#####################################################################################################################
# This is alreay! :D

class SpanLattice2D(Scene):
    def construct(self):
        grid = ScreenGrid()
        self.add(grid)

        v_1 = InputVectors()
        v_2 = InputVectors()

        self.play(FadeIn(Vector(v_1, color=BLUE)))
        self.play(FadeIn(Vector(v_2, color=GREEN)))
        vectors1 = {}
        vectors2 = {}

        for i in range(-5, 5):
            vectors1[i] = i * v_1
            vectors2[i] = i * v_2
            self.play(FadeIn(Vector(vectors1[i], color=BLUE, stroke=0.09), run_time=0.125))
            self.play(ReplacementTransform(Vector(vectors1[i]), Dot(vectors1[i])), run_time=0.125)
            self.play(FadeIn(Vector(vectors2[i], color=GREEN, stroke=0.09), run_time=0.125))
            self.play(ReplacementTransform(Vector(vectors2[i]), Dot(vectors2[i])), run_time=0.125)

        vector_sum = {}

        for j in reversed(range(-5, 5)):
            for i in reversed(range(-5, 5)):
                vector_sum[(i, j)] = (i * v_1) + (j * v_2)
                self.play(FadeIn(Vector(vector_sum[(i, j)], color=ORANGE, stroke=0.09), run_time=0.125))
                self.play(ReplacementTransform(Vector(vector_sum[(i, j)]), Dot(vector_sum[(i, j)])), run_time=0.125)

        self.wait(5)


####################################################################################################################
# This is already

class DrawLattice2D(Scene):
    def construct(self):

        screen_grid = ScreenGrid()
        self.add(screen_grid)

        v_1 = InputVectors()
        v_2 = InputVectors()

        center = np.array([0, 0, 0])
        self.play(FadeIn(Vector(v_1, color=BLUE)))
        self.play(FadeIn(Vector(v_2, color=GREEN)))

        for i in range(-10, 10):
            for j in range(-10, 10):
                center2 = center + (i * v_1) + (j * v_2)
                suma0 = center2 + v_1
                suma1 = center2 + v_2
                suma2 = center2 + v_1 + v_2
                self.add(screen_grid, Dot(suma0))
                self.add(screen_grid, Dot(suma1))
                self.add(screen_grid, Dot(center2))
                self.add(screen_grid, Dot(suma2))

        self.wait(5)


######################################################################################################
# This is already! :D

def Polygon3D(listOfPoints, aes_color=BLUE, opacity=0.7):
    H1 = listOfPoints
    H2 = []
    for i in range(len(H1)):
        H2.append([H1[i][0], H1[i][1], H1[i][2]])

    S = []
    for i in range(len(H2) - 1):
        s1 = [(H2[i][0], H2[i][1], H2[i][2]),
              (H2[i + 1][0], H2[i + 1][1], H2[i + 1][2]),
              (H2[i + 1][0], H2[i + 1][1], H1[i + 1][2]),
              (H2[i][0], H2[i][1], H1[i][2])]
        S.append(Polygon(*s1, fill_color=aes_color, fill_opacity=opacity, color=aes_color, stoke_width=0.1))

    b = Polygon(*H1, fill_color=aes_color, fill_opacity=opacity, color=aes_color, stoke_width=0.1)
    h = Polygon(*H2, fill_color=aes_color, fill_opacity=opacity, color=aes_color, stoke_width=0.1)
    s = VGroup(*S)
    poly3D = VGroup(*[b, h, s])
    return poly3D


class DrawDomFundLattice2D(Scene):
    def construct(self):
        plane = ScreenGrid()
        self.add(plane)

        v_1 = InputVectors()
        v_2 = InputVectors()

        center = np.array([0, 0, 0])

        self.play(FadeIn(Vector(v_1, color=GREEN)))
        self.play(FadeIn(Vector(v_2, color=RED)))

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

        DomFund = [center,
                   v_1,
                   v_1 + v_2,
                   v_2
                   ]

        DrawDomFund = Polygon3D(DomFund)
        self.play(ShowCreation(DrawDomFund))

        self.wait(5)


###############################################################################################################################
# This is already! :D

class GaussLatticeReduction(Scene):
    def construct(self):

        screen_grid = ScreenGrid()
        self.add(screen_grid)

        u_1 = Input2DVectors()
        u_2 = Input2DVectors()
        v_1 = np.array(u_1)
        v_2 = np.array(u_2)

        center = np.array([0, 0, 0])
        self.play(FadeIn(Vector(v_1, color=BLUE)))
        self.play(FadeIn(Vector(v_2, color=GREEN)))

        for i in range(-20, 20):
            for j in range(-20, 20):
                center2 = center + (i * v_1) + (j * v_2)
                suma0 = center2 + v_1
                suma1 = center2 + v_2
                suma2 = center2 + v_1 + v_2
                self.add(screen_grid, Dot(suma0))
                self.add(screen_grid, Dot(suma1))
                self.add(screen_grid, Dot(center2))
                self.add(screen_grid, Dot(suma2))

        self.wait(3)

        mat2 = [[u_1[0], u_2[0]], [u_1[1], u_2[1]]]
        mat2 = create_matrix(mat2)
        mat2 = lll_reduction(mat2)

        w_1 = [float(mat2[0][0]), float(mat2[1][0])]
        w_2 = [float(mat2[0][1]), float(mat2[1][1])]
        w_1 = np.array(w_1)
        w_2 = np.array(w_2)

        self.play(Transform(Vector(v_1), Vector(w_1), run_time=0.5))

        self.wait(5)


############################################################################################################################################################################
#    This is already!  :D


class DrawLatticeIn3D(ThreeDScene):
    center = np.array([0, 0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        axes = ThreeDAxes()
        self.set_camera_orientation(phi=60 * DEGREES, theta=-40 * DEGREES)
        self.add(axes)

    def torus(self, center):
        c = 0.08
        trr = ParametricSurface(
            lambda u, v: np.array([
                (c * np.sin(TAU * v) * np.cos(TAU * u)) + center[0],
                (c * np.sin(TAU * v) * np.sin(TAU * u)) + center[1],
                (c * np.cos(TAU * v)) + center[2]
            ]),
            resolution=(3, 3)).fade(0.5)  # Resolution of the surfaces
        self.play(Write(trr), run_time=0.08)

    def moveVectors(self, v1, v2):
        for i in range(-5, 5):
            for j in range(-5, 5):
                center2 = self.center + (i * v1) + (j * v2)
                suma0 = center2 + v1
                suma1 = center2 + v2
                self.torus(suma0)
                self.torus(suma1)
                self.torus(center2)
                self.torus(suma1)

        self.wait(15)

    def tarugo3D(self, center, base0, base1, base2):
        self.torus(((center + base0) + base1) + base2)
        self.torus((center + base1) + base2)
        self.torus(center + base2)
        self.torus((center + base0) + base2)
        self.torus((center + base0) + base1)
        self.torus(center + base1)
        self.torus(center)
        self.torus(center + base0)

    def facet(self, vertex0, vertex1, vertex2, vertex3):
        square = Polygon(np.array([vertex0[0], vertex0[1], vertex0[2]]),
                         np.array([vertex1[0], vertex1[1], vertex1[2]]),
                         np.array([vertex2[0], vertex2[1], vertex2[2]]),
                         np.array([vertex3[0], vertex3[1], vertex3[2]]))
        self.play(Write(square), run_time=0.2)


class DrawLattice1Din3D(DrawLatticeIn3D):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        v = InputVectors3D()
        self.play(FadeIn(Line(ORIGIN, v, color=BLUE)))

        self.torus(v)
        vects = {}

        for i in range(-15, 15):
            vects[i] = i * v
            self.torus(vects[i])

        self.wait(20)


class DrawLattice2Din3D(DrawLatticeIn3D):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        v_1 = InputVectors3D()
        v_2 = InputVectors3D()

        self.play(FadeIn(Line(self.center, v_1, color=RED)))
        self.torus(v_1)
        self.play(FadeIn(Line(self.center, v_2, color=GREEN)))
        self.torus(v_2)

        self.moveVectors(v_1, v_2)


class DrawLatticeDomFund2Din3D(DrawLatticeIn3D):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        v_1 = InputVectors3D()
        v_2 = InputVectors3D()

        self.play(FadeIn(Line(self.center, v_1, color=RED)))
        self.torus(v_1)
        self.play(FadeIn(Line(self.center, v_2, color=GREEN)))
        self.torus(v_2)

        DomFund = [self.center,
                   v_1,
                   v_1 + v_2,
                   v_2
                   ]

        DrawDomFund = Polygon3D(DomFund)
        self.play(ShowCreation(DrawDomFund))

        self.moveVectors(v_1, v_2)


class DrawLattice3D(DrawLatticeIn3D):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        base0 = InputVectors3D()
        base1 = InputVectors3D()
        base2 = InputVectors3D()

        self.play(FadeIn(Line(self.center, base0, color=RED)))
        self.torus(base0)
        self.play(FadeIn(Line(self.center, base1, color=GREEN)))
        self.torus(base1)
        self.play(FadeIn(Line(self.center, base2, color=ORANGE)))
        self.torus(base2)
        self.wait(1)

        # torus(center)
        for i in range(-2, 2):
            for j in range(-2, 2):
                for k in range(-2, 2):
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1) or (i % 2 == -1 and j % 2 == -1) or (
                            i % 2 == -1 and j % 2 == 1) or (i % 2 == 1 and j % 2 == -1):
                        if (i % 2 == 0 and k % 2 == 0) or (i % 2 == 1 and k % 2 == 1) or (
                                i % 2 == -1 and k % 2 == -1) or (i % 2 == -1 and k % 2 == 1) or (
                                i % 2 == 1 and k % 2 == -1):
                            if (k % 2 == 0 and j % 2 == 0) or (k % 2 == 1 and j % 2 == 1) or (
                                    k % 2 == -1 and j % 2 == -1) or (k % 2 == -1 and j % 2 == 1) or (
                                    k % 2 == 1 and j % 2 == -1):
                                self.tarugo3D(self.center + (i * base0) + (j * base1) + (k * base2), base0, base1,
                                              base2)

        self.wait(20)


########################################################################################################################################################################
# This is already! :D

class DrawDomFund3D(DrawLatticeIn3D):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def dominioFundamental3D(center, base0, base1, base2):
            v_0 = ((center + base0) + base1) + base2
            v_1 = (center + base1) + base2
            v_2 = center + base2
            v_3 = (center + base0) + base2
            v_4 = (center + base0) + base1
            v_5 = center + base1
            v_6 = center
            v_7 = center + base0

            self.facet(v_6, v_7, v_4, v_5)
            cara0 = [v_6, v_7, v_4, v_5]
            self.add(Polygon3D(cara0))

            self.facet(v_6, v_7, v_3, v_2)
            cara1 = [v_6, v_7, v_3, v_2]
            self.add(Polygon3D(cara1))

            self.facet(v_6, v_5, v_1, v_2)
            cara2 = [v_6, v_5, v_1, v_2]
            self.add(Polygon3D(cara2))

            self.facet(v_0, v_1, v_2, v_3)
            cara3 = [v_0, v_1, v_2, v_3]
            self.add(Polygon3D(cara3))

            self.facet(v_0, v_1, v_5, v_4)
            cara4 = [v_0, v_1, v_5, v_4]
            self.add(Polygon3D(cara4))

            self.facet(v_0, v_3, v_7, v_4)
            cara5 = [v_0, v_3, v_7, v_4]
            self.add(Polygon3D(cara5))

        # end of DominioFundamental

        base0 = InputVectors3D()
        base1 = InputVectors3D()
        base2 = InputVectors3D()

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        axes = ThreeDAxes()
        self.set_camera_orientation(phi=60 * DEGREES, theta=-40 * DEGREES)
        self.add(axes)

        center = np.array([0.0, 0.0, 0.0])
        self.play(FadeIn(Line(center, base0, color=RED)))
        self.torus(base0)
        self.play(FadeIn(Line(center, base1, color=GREEN)))
        self.torus(base1)
        self.play(FadeIn(Line(center, base2, color=ORANGE)))
        self.torus(base2)
        self.wait(1)

        dominioFundamental3D(center, base0, base1, base2)

        # torus(center)
        for i in range(-2, 2):
            for j in range(-2, 2):
                for k in range(-2, 2):
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1) or (i % 2 == -1 and j % 2 == -1) or (
                            i % 2 == -1 and j % 2 == 1) or (i % 2 == 1 and j % 2 == -1):
                        if (i % 2 == 0 and k % 2 == 0) or (i % 2 == 1 and k % 2 == 1) or (
                                i % 2 == -1 and k % 2 == -1) or (i % 2 == -1 and k % 2 == 1) or (
                                i % 2 == 1 and k % 2 == -1):
                            if (k % 2 == 0 and j % 2 == 0) or (k % 2 == 1 and j % 2 == 1) or (
                                    k % 2 == -1 and j % 2 == -1) or (k % 2 == -1 and j % 2 == 1) or (
                                    k % 2 == 1 and j % 2 == -1):
                                self.tarugo3D(self.center + (i * base0) + (j * base1) + (k * base2), base0, base1, base2)

        self.wait(10)


###################################################################################################################################################################
#   This is already! :D

class LLLReduceLattice(DrawLatticeIn3D):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        v_1 = Input3DVectors()
        v_2 = Input3DVectors()
        v_3 = Input3DVectors()

        Base0 = np.array(v_1)
        Base1 = np.array(v_2)
        Base2 = np.array(v_3)

        self.play(FadeIn(Line(self.center, Base0, color=RED)))
        self.torus(Base0)
        self.play(FadeIn(Line(self.center, Base1, color=GREEN)))
        self.torus(Base1)
        self.play(FadeIn(Line(self.center, Base2, color=ORANGE)))
        self.torus(Base2)
        self.wait(1)

        # torus(center)
        for i in range(-2, 2):
            for j in range(-2, 2):
                for k in range(-2, 2):
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1) or (i % 2 == -1 and j % 2 == -1) or (
                            i % 2 == -1 and j % 2 == 1) or (i % 2 == 1 and j % 2 == -1):
                        if (i % 2 == 0 and k % 2 == 0) or (i % 2 == 1 and k % 2 == 1) or (
                                i % 2 == -1 and k % 2 == -1) or (i % 2 == -1 and k % 2 == 1) or (
                                i % 2 == 1 and k % 2 == -1):
                            if (k % 2 == 0 and j % 2 == 0) or (k % 2 == 1 and j % 2 == 1) or (
                                    k % 2 == -1 and j % 2 == -1) or (k % 2 == -1 and j % 2 == 1) or (
                                    k % 2 == 1 and j % 2 == -1):
                                self.tarugo3D(self.center + (i * Base0) + (j * Base1) + (k * Base2), Base0, Base1,
                                              Base2)

        mat1 = [[v_1[0], v_2[0], v_3[0]], [v_1[1], v_2[1], v_3[1]], [v_1[2], v_2[2], v_3[2]]]
        mat1 = create_matrix(mat1)
        mat1 = lll_reduction(mat1)

        u_1 = [float(mat1[0][0]), float(mat1[1][0]), float(mat1[2][0])]
        u_2 = [float(mat1[0][1]), float(mat1[1][1]), float(mat1[2][1])]
        u_3 = [float(mat1[0][2]), float(mat1[1][2]), float(mat1[2][2])]

        u_1 = np.array(u_1)
        u_2 = np.array(u_2)
        u_3 = np.array(u_3)

        self.play(
            ReplacementTransform(Line(self.center, Base0, color=RED), Line(self.center, u_1, color=RED), run_time=0.5))
        self.play(FadeOut())
        self.play(ReplacementTransform(Line(self.center, Base1, color=GREEN), Line(self.center, u_2, color=GREEN),
                                       run_time=0.5))
        self.play(
            ReplacementTransform(Line(self.center, Base0, color=ORANGE), Line(self.center, u_3, color=ORANGE),
                                 run_time=0.5))

        self.wait(20)


###############################################################################################################################################
# 

class DrawLattice4D(DrawLatticeIn3D):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def projectedToRest(proy, v):
            return np.array(
                [(proy / (proy - v[3])) * v[0], (proy / (proy - v[3])) * v[1], (proy / (proy - v[3])) * v[2]])

        def tarugo4D(center, base0, base1, base2, base3, angle):
            proyLAT = 15
            # angle = 0
            v_0 = ((center + base0) + base1) + base2
            v_1 = (center + base1) + base2
            v_2 = center + base2
            v_3 = (center + base0) + base2
            v_4 = (center + base0) + base1
            v_5 = center + base1
            v_6 = center
            v_7 = center + base0
            v_8 = (((center + base0) + base1) + base2) + base3
            v_9 = ((center + base1) + base2) + base3
            v_10 = (center + base2) + base3
            v_11 = ((center + base0) + base2) + base3
            v_12 = ((center + base0) + base1) + base3
            v_13 = (center + base1) + base3
            v_14 = center + base3
            v_15 = (center + base0) + base3

            v = np.array([v_0, v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11, v_12, v_13, v_14, v_15])

            RotZW = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, np.cos(angle), -np.sin(angle)],
                              [0, 0, np.sin(angle), np.cos(angle)]])

            for i in range(0, 16):
                v[i] = np.matmul(RotZW, v[i])

            v1 = np.array(
                [projectedToRest(proyLAT, v[0]), projectedToRest(proyLAT, v[1]), projectedToRest(proyLAT, v[2]),
                 projectedToRest(proyLAT, v[3]), projectedToRest(proyLAT, v[4]), projectedToRest(proyLAT, v[5]),
                 projectedToRest(proyLAT, v[6]), projectedToRest(proyLAT, v[7]), projectedToRest(proyLAT, v[8]),
                 projectedToRest(proyLAT, v[9]), projectedToRest(proyLAT, v[10]), projectedToRest(proyLAT, v[11]),
                 projectedToRest(proyLAT, v[12]), projectedToRest(proyLAT, v[13]), projectedToRest(proyLAT, v[14]),
                 projectedToRest(proyLAT, v[15])])

            for i in range(0, 15):
                self.torus(v1[i])

            # end of tarugo3D

        def dominioFundamental4D(center, base0, base1, base2, base3, angle):
            proyLAT = 15
            # angle = 0

            v_0 = ((center + base0) + base1) + base2
            v_1 = (center + base1) + base2
            v_2 = center + base2
            v_3 = (center + base0) + base2
            v_4 = (center + base0) + base1
            v_5 = center + base1
            v_6 = center
            v_7 = center + base0
            v_8 = (((center + base0) + base1) + base2) + base3
            v_9 = ((center + base1) + base2) + base3
            v_10 = (center + base2) + base3
            v_11 = ((center + base0) + base2) + base3
            v_12 = ((center + base0) + base1) + base3
            v_13 = (center + base1) + base3
            v_14 = center + base3
            v_15 = (center + base0) + base3
            v = np.array([v_0, v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11, v_12, v_13, v_14, v_15])
            RotZW = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, np.cos(angle), -np.sin(angle)],
                              [0, 0, np.sin(angle), np.cos(angle)]])

            for i in range(0, 16):
                v[i] = np.matmul(RotZW, v[i])

            v1 = np.array(
                [projectedToRest(proyLAT, v[0]), projectedToRest(proyLAT, v[1]), projectedToRest(proyLAT, v[2]),
                 projectedToRest(proyLAT, v[3]), projectedToRest(proyLAT, v[4]), projectedToRest(proyLAT, v[5]),
                 projectedToRest(proyLAT, v[6]), projectedToRest(proyLAT, v[7]), projectedToRest(proyLAT, v[8]),
                 projectedToRest(proyLAT, v[9]), projectedToRest(proyLAT, v[10]), projectedToRest(proyLAT, v[11]),
                 projectedToRest(proyLAT, v[12]), projectedToRest(proyLAT, v[13]), projectedToRest(proyLAT, v[14]),
                 projectedToRest(proyLAT, v[15])])

            self.facet(v1[6], v1[7], v1[4], v1[5])
            self.facet(v1[6], v1[7], v1[3], v1[2])
            self.facet(v1[6], v1[5], v1[1], v1[2])
            self.facet(v1[0], v1[1], v1[2], v1[3])
            self.facet(v1[0], v1[1], v1[5], v1[4])
            self.facet(v1[0], v1[3], v1[7], v1[4])
            self.facet(v1[11], v1[3], v1[7], v1[15])
            self.facet(v1[15], v1[7], v1[4], v1[12])
            self.facet(v1[11], v1[3], v1[0], v1[8])
            self.facet(v1[8], v1[0], v1[4], v1[12])
            self.facet(v1[10], v1[2], v1[1], v1[9])
            self.facet(v1[10], v1[2], v1[3], v1[11])
            self.facet(v1[9], v1[1], v1[0], v1[8])
            self.facet(v1[9], v1[1], v1[5], v1[13])
            self.facet(v1[10], v1[2], v1[6], v1[14])
            self.facet(v1[14], v1[6], v1[7], v1[15])
            self.facet(v1[14], v1[6], v1[5], v1[13])
            self.facet(v1[13], v1[5], v1[4], v1[12])

            # end of tarugo3D

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        v_1 = InputVectors4D()
        v_2 = InputVectors4D()
        v_3 = InputVectors4D()
        v_4 = InputVectors4D()

        Center = np.array([0.0, 0.0, 0.0, 0.0])
        base0 = np.array(v_1)
        base1 = np.array(v_2)
        base2 = np.array(v_3)
        base3 = np.array(v_4)

        for i in range(-3, 3):
            for j in range(-3, 3):
                for k in range(-3, 3):
                    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1) or (i % 2 == -1 and j % 2 == -1) or (
                            i % 2 == -1 and j % 2 == 1) or (i % 2 == 1 and j % 2 == -1):
                        if (i % 2 == 0 and k % 2 == 0) or (i % 2 == 1 and k % 2 == 1) or (
                                i % 2 == -1 and k % 2 == -1) or (i % 2 == -1 and k % 2 == 1) or (
                                i % 2 == 1 and k % 2 == -1):
                            if (k % 2 == 0 and j % 2 == 0) or (k % 2 == 1 and j % 2 == 1) or (
                                    k % 2 == -1 and j % 2 == -1) or (k % 2 == -1 and j % 2 == 1) or (
                                    k % 2 == 1 and j % 2 == -1):
                                dominioFundamental4D(Center + (i * base0) + (j * base1) + (k * base2), base0, base1,
                                                     base2, base3, 3.1415 * 0.25)

        self.wait(3)
