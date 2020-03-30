from manimlib.imports import *

class DrawPolygon(ThreeDScene):
    def construct(self):
        
        def Polygon3D(listOfPoints, aes_color = BLUE, opacity = 0.8):
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

        caras = {}
        caras[0]=   [(0,0,0),   #P1
                    (0,1,0),    #P2
                    (1,1,0),    #P3
                    (1,0,0),    #P4
                    ]
        caras[1] = [(0,0,1),   #P1
                    (0,1,1),    #P2
                    (1,1,1),    #P3
                    (1,0,1),    #P4
                    ]
    
        caras[2] = [(0,0,0),   #P1
                    (0,0,1),    #P2
                    (1,0,1),    #P3
                    (1,0,0),    #P4
                    ]    
        
        caras[3] = [(0,1,0),   #P1
                    (0,1,1),    #P2
                    (1,1,1),    #P3
                    (1,1,0),    #P4
                    ]
        
        caras[4] = [(1,0,0),    #P2
                    (1,0,1),    #P3
                    (1,1,1),
                    (1,1,0),
                    ]
        caras[5] = [(0,0,0),    #P2
                    (0,0,1),    #P3
                    (0,1,1),
                    (0,1,0),
                    ]
            
        
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=70 * DEGREES,theta=-45*DEGREES)
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)

        self.play(Write(Polygon3D(caras[0])))
        self.play(Write(Polygon3D(caras[1])))
        self.play(Write(Polygon3D(caras[2])))
        self.play(Write(Polygon3D(caras[3])))
        self.play(Write(Polygon3D(caras[4])))
        self.play(Write(Polygon3D(caras[5])))

        #self.add((Polygon3D(caras[5])))

        self.wait(15)

