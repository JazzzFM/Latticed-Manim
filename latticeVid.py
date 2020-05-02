from manimlib.imports import *
import numpy as np
from tkinter import*



class Example(ThreeDScene):
    

    def construct(self):

        def torus(center):
            c = 0.1
            trr = ParametricSurface(
                lambda u, v : np.array([
                     (c * np.sin(TAU * v) * np.cos(TAU*u)) + center[0],
                     (c * np.sin(TAU * v) * np.sin(TAU*u)) + center[1],
                     (c * np.cos(TAU * v)) + center[2]
                 ]),
                resolution=(3, 3)).fade(0.5) #Resolution of the surfaces
            self.play(Write(trr), run_time = 0.1)
        #end of def

        def gaussian_lattice_reduction(v1, v2):
            while True:
                m_v1 = np.linalg.norm(v1)
                m_v2 = np.linalg.norm(v2)

            if m_v2 < m_v1:
                aux = v1
                v1 = v2
                v2 = aux

            m_v1 = np.linalg.norm(v1)
            m = np.dot(v1, v2) / (m_v1 ** 2)

            if m == 0:
                return v1, v2

            v2 = v2 - (m * v1)
            torus(v2)



        def facet(vertex0, vertex1, vertex2, vertex3):
            square = Polygon(np.array([vertex0[0], vertex0[1], vertex0[2]]), np.array([vertex1[0], vertex1[1], vertex1[2]]), np.array([vertex2[0], vertex2[1], vertex2[2]]), np.array([vertex3[0], vertex3[1], vertex3[2]]))
            self.play(Write(square), run_time = 0.2)
        #end of facet

        def tarugo3D(center, base0, base1, base2):
            v_0 = ((center + base0) + base1) + base2
            v_1 = (center + base1) + base2
            v_2 = center + base2
            v_3 = (center + base0) + base2

            v_4 = (center + base0) + base1
            v_5 = center + base1
            v_6 = center
            v_7 = center + base0

            torus(v_0)
            torus(v_1)
            torus(v_2)
            torus(v_3)
            torus(v_4)
            torus(v_5)
            torus(v_6)
            torus(v_7)

            #end of tarugo3D

        def projectedToRest(proy, v):
            return np.array([(proy/(proy-v[3])) * v[0], (proy/(proy-v[3])) * v[1], (proy/(proy-v[3])) * v[2]])

        def tarugo4D(center, base0, base1, base2, base3, angle):
            proyLAT = 5
            #angle = 0

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
            
            RotZW = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, np.cos(angle),-np.sin(angle)], [0, 0, np.sin(angle), np.cos(angle)]])

            for i in range(0, 16):
                v[i] = np.matmul(RotZW, v[i])

            v1 = np.array([projectedToRest(proyLAT, v[0]), projectedToRest(proyLAT, v[1]), projectedToRest(proyLAT, v[2]), projectedToRest(proyLAT, v[3]), projectedToRest(proyLAT, v[4]), projectedToRest(proyLAT, v[5]), projectedToRest(proyLAT, v[6]), projectedToRest(proyLAT, v[7]), projectedToRest(proyLAT, v[8]), projectedToRest(proyLAT, v[9]), projectedToRest(proyLAT, v[10]), projectedToRest(proyLAT, v[11]), projectedToRest(proyLAT, v[12]), projectedToRest(proyLAT, v[13]), projectedToRest(proyLAT, v[14]), projectedToRest(proyLAT, v[15])])

            for i in range(0, 15):
                torus(v1[i])
            
            #end of tarugo3D

        def dominioFundamental4D(center, base0, base1, base2, base3, angle):
            proyLAT = 50
            #angle = 0

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
            
            RotZW = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, np.cos(angle),-np.sin(angle)], [0, 0, np.sin(angle), np.cos(angle)]])

            for i in range(0, 16):
                v[i] = np.matmul(RotZW, v[i])

            v1 = np.array([projectedToRest(proyLAT, v[0]), projectedToRest(proyLAT, v[1]), projectedToRest(proyLAT, v[2]), projectedToRest(proyLAT, v[3]), projectedToRest(proyLAT, v[4]), projectedToRest(proyLAT, v[5]), projectedToRest(proyLAT, v[6]), projectedToRest(proyLAT, v[7]), projectedToRest(proyLAT, v[8]), projectedToRest(proyLAT, v[9]), projectedToRest(proyLAT, v[10]), projectedToRest(proyLAT, v[11]), projectedToRest(proyLAT, v[12]), projectedToRest(proyLAT, v[13]), projectedToRest(proyLAT, v[14]), projectedToRest(proyLAT, v[15])])
            
            facet(v1[6], v1[7], v1[4], v1[5])
            facet(v1[6], v1[7], v1[3], v1[2])
            facet(v1[6], v1[5], v1[1], v1[2])
            facet(v1[0], v1[1], v1[2], v1[3])
            facet(v1[0], v1[1], v1[5], v1[4])
            facet(v1[0], v1[3], v1[7], v1[4])

            facet(v1[11], v1[3], v1[7], v1[15])
            facet(v1[15], v1[7], v1[4], v1[12])
            facet(v1[11], v1[3], v1[0], v1[8])
            facet(v1[8], v1[0], v1[4], v1[12])
            
            
            facet(v1[10], v1[2], v1[1], v1[9])
            facet(v1[10], v1[2], v1[3], v1[11])
            facet(v1[9], v1[1], v1[0], v1[8])
            facet(v1[9], v1[1], v1[5], v1[13])

            facet(v1[10], v1[2], v1[6], v1[14])
            facet(v1[14], v1[6], v1[7], v1[15])

            facet(v1[14], v1[6], v1[5], v1[13])
            facet(v1[13], v1[5], v1[4], v1[12])

            

            #end of tarugo3D        

        def dominioFundamental3D(center, base0, base1, base2):
            v_0 = ((center + base0) + base1) + base2
            v_1 = (center + base1) + base2
            v_2 = center + base2
            v_3 = (center + base0) + base2

            v_4 = (center + base0) + base1
            v_5 = center + base1
            v_6 = center
            v_7 = center + base0

            facet(v_6, v_7, v_4, v_5)
            facet(v_6, v_7, v_3, v_2)
            facet(v_6, v_5, v_1, v_2)
            facet(v_0, v_1, v_2, v_3)
            facet(v_0, v_1, v_5, v_4)
            facet(v_0, v_3, v_7, v_4)
        #end of DominioFundamental        

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70 * DEGREES,theta=-45*DEGREES)
        self.add(axes)

        center = np.array([0.0, 0.0, 0.0])
        Base0  = np.array([1.0, 0.0, 0.0])
        Base1  = np.array([1.0, 0.5, 0.5])
        Base2  = np.array([0.0, 0.0, 1.0])

        Center = np.array([0.0, 0.0, 0.0, 0.0])
        base0  = np.array([2.0, 0.0, 0.5, 0.0])
        base1  = np.array([0.0, 2.0, 0.0, 0.0])
        base2  = np.array([0.5, 0.0, 2.0, 0.5])
        base3  = np.array([0.0, 0.5, 0.0, 1.0])
        
        Base01 = np.array([6.2351, 1.2145, 0])
        Base11 = np.array([1.7445, 3.2414, 0])        
        dominioFundamental3D(center, Base0, Base1, Base2)

        #torus(center)
    #    for i in range(-2, 2):
    #        for j in range(-2, 2):
    #           for k in range(-2, 2):
    #                if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1) or (i%2 ==-1 and j%2 ==-1) or (i%2 ==-1 and j%2 == 1) or (i%2 == 1 and j%2 ==-1):
    #                    if (i%2 == 0 and k%2 == 0) or (i%2 == 1 and k%2 == 1) or (i%2 ==-1 and k%2 ==-1) or (i%2 ==-1 and k%2 == 1) or (i%2 == 1 and k%2 ==-1):
    #                        if (k%2 == 0 and j%2 == 0) or (k%2 == 1 and j%2 == 1) or (k%2 ==-1 and j%2 ==-1) or (k%2 ==-1 and j%2 == 1) or (k%2 == 1 and j%2 ==-1):
    #                            tarugo3D(center + (i * Base0) + (j * Base1) + (k * Base2), Base0, Base1, Base2)

    #    for i in range(-2, 3):
    #        for j in range(-2, 3):
    #           for k in range(-2, 3):
    #                if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1) or (i%2 ==-1 and j%2 ==-1) or (i%2 ==-1 and j%2 == 1) or (i%2 == 1 and j%2 ==-1):
    #                    if (i%2 == 0 and k%2 == 0) or (i%2 == 1 and k%2 == 1) or (i%2 ==-1 and k%2 ==-1) or (i%2 ==-1 and k%2 == 1) or (i%2 == 1 and k%2 ==-1):
    #                        if (k%2 == 0 and j%2 == 0) or (k%2 == 1 and j%2 == 1) or (k%2 ==-1 and j%2 ==-1) or (k%2 ==-1 and j%2 == 1) or (k%2 == 1 and j%2 ==-1):
    #                            dominioFundamental4D(Center + (i * base0) + (j * base1) + (k * base2), base0, base1, base2, base3, 3.1415*0.25)


                    
        #dominioFundamental4D(Center + (i * base0) + (j * base1) + (k * base2), base0, base1, base2, base3, 3.1415*0.0)
        self.wait(3)
    #    root = Tk()
    #    root.title("Lattice")
    #    label = Label(root, text = "Lets build Lattices")
    #    label.grid(row = 0, column = 0, columnspan = 3, padx = 100, pady=100)
    #    b = Button(root, text = "Build Lattice in 4D", command = lambda: dominioFundamental4D(Center, base0, base1, base2, base3, 3.1415*0.25))
    #    b.grid(row = 1, column = 1)
    #    button_quit = Button(root, text = "See Lattice", command = root.quit)
    #    button_quit.grid(row = 2, column = 1)
#
    #    root.mainloop()

    #    for i in range(0, 1):
    #        for j in range(0, 1):
    #            for k in range(0, 1):
    #                tarugo4D(Center + (i * base0) + (j * base1) + (k * base2), base0, base1, base2, base3, 3.1415*0.25)
            
     #   gaussian_lattice_reduction(Base01, Base11)

        





