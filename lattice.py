import Q
import math
import pygame
import random 
import MatrixQ
import Vector4D as v4
import Vector5D as v5
import tarugo4D as t4
import tarugo5D as t5
import os
#import latticeVid as L  #AQUI ESTOY LLAMANDO A MANIM
import tarugo3D as t
import cube as c
import Vector as v
import plane as p
from tkinter import*
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from PIL import ImageTk, Image


import subprocess
import shlex, subprocess
#import OpenGL_accelerate

root = Tk()
sizex = 800
sizey = 600
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

Row = 0
rowFrame0 = 0
rowframe2 = 0

##################
#                #
#   Background   #
#                #
##################

can = Canvas(root, width = sizex, height = sizey)
image = ImageTk.PhotoImage(Image.open("Lat.jpeg"))
#
can.create_image(0, 0, anchor = NW, image = image)
can.pack()

###########
#         #
#  Fames  #
#         #
###########

frame0 = LabelFrame(root, text = "Objective function: ", padx = 100, pady = 50)
#frame0.grid(row = Row, column = 0, columnspan = 6, padx = 10, pady = 10)
def data():
    for i in range(50):
       Label(frame,text=i).grid(row=i,column=0)
       Label(frame,text="my text"+str(i)).grid(row=i,column=1)
       Label(frame,text="..........").grid(row=i,column=2)

def data2():
    for i in range(50):
       Label(frame,text=i).grid(row=0,column=i)
       Label(frame,text="my text"+str(i)).grid(row=1,column=i)
       Label(frame,text="..........").grid(row=2,column=i)


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width = 600, height = 200)

def myfunction2(event):
    canvas2.configure(scrollregion=canvas2.bbox("all"),width=600,height=600)

#myframe=Frame(root, relief=GROOVE, width=50, height=100, bd=10)
#myframe.place(x=100,y=300)
#
#canvas=Canvas(myframe)
#frame=Frame(canvas)
#myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
#myscrollbar0=Scrollbar(myframe, orient="horizontal",command=canvas.xview)
#canvas.configure(yscrollcommand=myscrollbar.set)
#canvas.configure(xscrollcommand=myscrollbar0.set)
#canvas.create_image(0, 0, anchor = NW, image = image)
#myscrollbar.pack(side="right",fill="y")
#myscrollbar0.pack(side="bottom",fill="x")
#canvas.pack(side="left")
#canvas.create_window((0,0),window=frame,anchor='nw')
#frame.bind("<Configure>",myfunction)
##############################################################
#myframe2=Frame(root, relief=GROOVE, width=50, height=100, bd=20)
#myframe2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
#
#canvas2=Canvas(myframe2)
#frame2=Frame(canvas2)
#myscrollbar2=Scrollbar(myframe2, orient="horizontal",command=canvas2.xview)
#
#canvas2.configure(xscrollcommand=myscrollbar2.set)
#canvas2.create_image(0, 0, anchor = NW, image = image)
#myscrollbar2.pack(side="bottom",fill="x")
#canvas2.pack(side="left")
#canvas2.create_window((0,0),window=frame2,anchor='nw')
#frame2.bind("<Configure>",myfunction2)
#data2()
#data()
###########
#         #
# LABELS  #
#         #
###########
lb = Label(root, text = "Or try building with Manim:")
lb3 = Label(root, text = "Enter the base vectors for 3D lattice:")
func = Label(root, text = "vector1:")
func1 = Label(root, text = "vector2:")
func2 = Label(root, text = "vector3:")

lb31 = Label(root, text = "Enter the base vectors for 4D lattice:")
func01 = Label(root, text = "vector1:")
func11 = Label(root, text = "vector2:")
func21 = Label(root, text = "vector3:")
func31 = Label(root, text = "vector4:")

lb32 = Label(root, text = "Enter the base vectors for 5D lattice:")
func011 = Label(root, text = "vector1:")
func111 = Label(root, text = "vector2:")
func211 = Label(root, text = "vector3:")
func311 = Label(root, text = "vector4:")
func411 = Label(root, text = "vector5:")

lb3.place(relx = 0.2, rely = 0.04, anchor = CENTER)
lb31.place(relx = 0.2, rely = 0.25, anchor = CENTER)
lb32.place(relx = 0.2, rely = 0.55, anchor = CENTER)

###########
#         #
# Main Z  #
#         #
###########

def inputZ():
    global numVar
    global Z
    global Z1
    global Z2

    global dim4_0
    global dim4_1
    global dim4_2
    global dim4_3

    global dim5_0
    global dim5_1
    global dim5_2
    global dim5_3
    global dim5_4

    numVar = 3
    Z = [Entry(root, width = 5, borderwidth = 5) for x in range(numVar)]
    Z1 = [Entry(root, width = 5, borderwidth = 5) for x in range(numVar)]
    Z2 = [Entry(root, width = 5, borderwidth = 5) for x in range(numVar)]

    dim4_0 = [Entry(root, width = 5, borderwidth = 5) for x in range(4)]
    dim4_1 = [Entry(root, width = 5, borderwidth = 5) for x in range(4)]
    dim4_2 = [Entry(root, width = 5, borderwidth = 5) for x in range(4)]
    dim4_3 = [Entry(root, width = 5, borderwidth = 5) for x in range(4)]

    dim5_0 = [Entry(root, width = 5, borderwidth = 5) for x in range(5)]
    dim5_1 = [Entry(root, width = 5, borderwidth = 5) for x in range(5)]
    dim5_2 = [Entry(root, width = 5, borderwidth = 5) for x in range(5)]
    dim5_3 = [Entry(root, width = 5, borderwidth = 5) for x in range(5)]
    dim5_4 = [Entry(root, width = 5, borderwidth = 5) for x in range(5)]

    func.place(relx = 0.2, rely = 0.08, anchor = CENTER)
    func1.place(relx = 0.2, rely = 0.125, anchor = CENTER)
    func2.place(relx = 0.2, rely = 0.1725, anchor = CENTER)
    for i in range(0, numVar):
        Z[i].place(relx = 0.07*i + 0.3, rely = 0.08, anchor = CENTER)
        Z1[i].place(relx = 0.07*i + 0.3, rely = 0.125, anchor = CENTER)
        Z2[i].place(relx = 0.07*i + 0.3, rely = 0.1725, anchor = CENTER)

    func01.place(relx = 0.2, rely = 0.3, anchor = CENTER)
    func11.place(relx = 0.2, rely = 0.345, anchor = CENTER)
    func21.place(relx = 0.2, rely = 0.39, anchor = CENTER)
    func31.place(relx = 0.2, rely = 0.435, anchor = CENTER)
    for i in range(0, 4):
        dim4_0[i].place(relx = 0.07*i + 0.3, rely = 0.3, anchor = CENTER)
        dim4_1[i].place(relx = 0.07*i + 0.3, rely = 0.345, anchor = CENTER)
        dim4_2[i].place(relx = 0.07*i + 0.3, rely = 0.39, anchor = CENTER)
        dim4_3[i].place(relx = 0.07*i + 0.3, rely = 0.435, anchor = CENTER)

    func011.place(relx = 0.2, rely = 0.6, anchor = CENTER)
    func111.place(relx = 0.2, rely = 0.6 + 1*0.045, anchor = CENTER)
    func211.place(relx = 0.2, rely = 0.6 + 2*0.045, anchor = CENTER)
    func311.place(relx = 0.2, rely = 0.6 + 3*0.045, anchor = CENTER)
    func411.place(relx = 0.2, rely = 0.6 + 4*0.045, anchor = CENTER)

    for i in range(0, 5):
        dim5_0[i].place(relx = 0.07*i + 0.3, rely = 0.6, anchor = CENTER)
        dim5_1[i].place(relx = 0.07*i + 0.3, rely = 0.6 + 1*0.045, anchor = CENTER)
        dim5_2[i].place(relx = 0.07*i + 0.3, rely = 0.6 + 2*0.045, anchor = CENTER)
        dim5_3[i].place(relx = 0.07*i + 0.3, rely = 0.6 + 3*0.045, anchor = CENTER)
        dim5_4[i].place(relx = 0.07*i + 0.3, rely = 0.6 + 4*0.045, anchor = CENTER)


inputZ()
#############
#           #
# Functions #
#           #
#############

def split_get():
	first_rational = e0.get()
	rac = first_rational.split('/')
	p = int(rac[0])
	if len(rac) == 1:
		rac.append(1);
	q = rac[1]
	e0.delete(0, END)
	e2.delete(0, END)
	if q == 1:
		e2.insert(0, p)
	else:
		e2.insert(0, q)
		e2.insert(0, "/")
		e2.insert(0, p)

def string_split(STR):
	rac = STR.split('/')
	p = int(rac[0])
	if len(rac) == 1:
		rac.append(1);
	q = int(rac[1])
	return Q.Rational(p, q)

def add_Rational():
	rational = string_split(e0.get())
	global f_rac
	f_rac = rational
	e0.delete(0, END)

	rational2 = string_split(e1.get())
	global f_rac2
	f_rac2 = rational2
	e1.delete(0, END)

	result = f_rac + f_rac2
	e2.delete(0, END)
	if(result.den == 1):
		e2.insert(0, result.num)
	else:
		e2.insert(0, result.den)
		e2.insert(0, "/")
		e2.insert(0, result.num)

def get_Matrix():
	rational = [[Q.Rational(0,1) for x in range(n)] for y in range(n)]
	for i in range(0, m):
		for j in range(0, n):
			rational[i][j] = string_split(E[i][j].get())
			E[i][j].delete(0, END)

	for i in range(0, m):
		for j in range(0, n):
			I[i][j].delete(0, END)

	for i in range(0, m):
		for j in range(0, n):
			if(rational[i][j].den == 1):
				I[i][j].insert(0, rational[i][j].num)
			else:
				I[i][j].insert(0, rational[i][j].den)
				I[i][j].insert(0, "/")
				I[i][j].insert(0, rational[i][j].num)

clicked = StringVar()
clicked.set("<=")					

def dynamicIntput():
	global m
	global n
	m = int(CONS.get())
	n = int(VAR.get())
	global E
	global I
	global D
	global B
	E = [[Entry(frame, width = "10", borderwidth = 5) for x in range(n)] for y in range(m)]
	I = [[Entry(frame, width = "10", borderwidth = 5) for x in range(n)] for y in range(m)]
	D = [OptionMenu(frame, clicked, "<=", ">=", "=") for x in range(m)]
	B = [Entry(frame, width = "10", borderwidth = 5) for x in range(m)]
	for i in range(0, m):
		for j in range(0, n):
			E[i][j].grid(row = Row + 1 + i, column = j, padx = 20, pady = 10)
		D[i].grid(row = Row + 1 + i, column = n)
		B[i].grid(row = Row + 1 + i, column = n + 1)

	#for i in range(0, m):
	#	for j in range(0, n):
	#		I[i][j].grid(row = Row + i, column = j+4, padx = 20, pady = 10)


###########
#         #
# Buttons #
#         #
###########

button_1 = Button(root, text="+", padx = 40, pady = 20, command = add_Rational)
button_2 = Button(root, text="Gen Matrix", padx = 40, pady = 20, command = dynamicIntput)
button_3 = Button(root, text="Get Matrix", padx = 40, pady = 20, command = get_Matrix)
#button_4 = Button(frame2, text="Accept", command = inputZ)
#button_5 = Button(frame, text="Input Restrictions", command = dynamicIntput)

#button_4.grid(row = rowframe2 + 7, column = 0)
#button_5.grid(row = 0, column = 0, columnspan = 10)

#######################
#                     #
#       OpenGL        # 
#                     #
#######################


center = v.Vector3D(0, 0, 0)
Pos = v.Vector3D(1, 1, 1)
Sky = v.Vector3D(0, 0, 1)
LookAt = v.Vector3D(0, 0, 0)
PI = 3.1415926535897932384626
centers = [[[v.Vector3D(x, y, z) for y in range(-3, 4)] for x in range(-3, 4)] for z in range(-3, 4)]

def axes():
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0, 0, 255)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 10)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 255, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 10, 0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(255, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(10, 0, 0)
    glEnd()
global vertical
vertical = Scale(root, from_= 0, to = 3.1415)
vertical.pack()

def draw3D():
    global theta

    global base0
    global base1
    global base2
    global base3

    center = v.Vector3D(0, 0, 0)
    
    Qx = string_split(Z[0].get())
    Qy = string_split(Z[1].get())
    Qz = string_split(Z[2].get())

    Qx1 = string_split(Z1[0].get())
    Qy1 = string_split(Z1[1].get())
    Qz1 = string_split(Z1[2].get())

    Qx2 = string_split(Z2[0].get())
    Qy2 = string_split(Z2[1].get())
    Qz2 = string_split(Z2[2].get())

    base0 = v.Vector3D(Qx.num/Qx.den, Qy.num/Qy.den, Qz.num/Qz.den)
    base1 = v.Vector3D(Qx1.num/Qx1.den, Qy1.num/Qy1.den, Qz1.num/Qz1.den)
    base2 = v.Vector3D(Qx2.num/Qx2.den, Qy2.num/Qy2.den, Qz2.num/Qz2.den)

    theta = 0.0
    pygame.init()
    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.001, 50.0)
    
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()
        
        glEnable(GL_DEPTH_TEST)
        glDepthMask(GL_TRUE)
        glDepthFunc(GL_LEQUAL)
        glDepthRange(0.0, 1.0)
        glEnable(GL_DEPTH_CLAMP)

        glEnable(GL_LIGHT0)
        fv4 = [0.3, 0.3, 0.3, 1.0]
        
        glShadeModel(GL_SMOOTH)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, fv4)
        glLightfv(GL_LIGHT0,GL_POSITION, fv4)
        glLightfv(GL_LIGHT0,GL_DIFFUSE, fv4)
        glEnable(GL_LIGHTING)
        glEnable(GL_MULTISAMPLE)  
        
        glRotatef(0, 30, 30, 30)
        glClearColor (0.5, 0.5, 0.5, 0.5)
        glClearDepth(1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        r = 25
        gluLookAt(r*math.sin(0.25*PI)*math.cos(theta), r*math.sin(0.25*PI)*math.sin(theta), r*math.cos(0.25*PI), LookAt.x, LookAt.y, LookAt.z, Sky.x, Sky.y, Sky.z)
        
        axes()
        for i in range(-3, 3):
            for j in range(-3, 3):
                for k in range(-3, 3):
                    if (i+j+k)%2 == 0:
                        tarugo = t.tarugo3D(((center + base0.scale(i)) + base1.scale(j)) + base2.scale(k), base0, base1, base2, True)
                        tarugo.drawTarugo()
                    else:
                        tarugo = t.tarugo3D(((center + base0.scale(i)) + base1.scale(j)) + base2.scale(k), base0, base1, base2, False)
                        tarugo.drawTarugo()

        
        pygame.display.flip()
        pygame.time.wait(10)
        theta += 0.01

button_Draw3D = Button(root, text="Graph 3D Lattice", command = draw3D)
button_Draw3D.place(relx = 0.07*5 + 0.3, rely = 0.1725, anchor = CENTER)


def draw4D():
    global theta

    global base4D_1
    global base4D_2
    global base4D_3
    global base4D_4

    Qx = string_split(dim4_0[0].get())
    Qy = string_split(dim4_0[1].get())
    Qz = string_split(dim4_0[2].get())
    Qw = string_split(dim4_0[3].get())

    Qx1 = string_split(dim4_1[0].get())
    Qy1 = string_split(dim4_1[1].get())
    Qz1 = string_split(dim4_1[2].get())
    Qw1 = string_split(dim4_1[3].get())

    Qx2 = string_split(dim4_2[0].get())
    Qy2 = string_split(dim4_2[1].get())
    Qz2 = string_split(dim4_2[2].get())
    Qw2 = string_split(dim4_2[3].get())

    Qx3 = string_split(dim4_3[0].get())
    Qy3 = string_split(dim4_3[1].get())
    Qz3 = string_split(dim4_3[2].get())
    Qw3 = string_split(dim4_3[3].get())

    base4D_1 = v4.Vector4D(Qx.num/Qx.den, Qy.num/Qy.den, Qz.num/Qz.den, Qw.num/Qw.den)
    base4D_2 = v4.Vector4D(Qx1.num/Qx1.den, Qy1.num/Qy1.den, Qz1.num/Qz1.den, Qw1.num/Qw1.den)
    base4D_3 = v4.Vector4D(Qx2.num/Qx2.den, Qy2.num/Qy2.den, Qz2.num/Qz2.den, Qw2.num/Qw2.den)
    base4D_4 = v4.Vector4D(Qx3.num/Qx3.den, Qy3.num/Qy3.den, Qz3.num/Qz3.den, Qw3.num/Qw3.den)


    center = v4.Vector4D(0, 0, 0, 0)
    base0 = v4.Vector4D(3, 0, 0, 0)
    base1 = v4.Vector4D(0, 3, 0, 0)
    base2 = v4.Vector4D(0, 0, 3, 0)
    base3 = v4.Vector4D(0, 0, 0, 3)

    theta = 0.0
    theta1 = 0.0
    pygame.init()
    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.001, 50.0)
    
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    theta += 0.1
            if event.type == pygame.MOUSEBUTTONDOWN:
                theta += 0.1

        
        glEnable(GL_DEPTH_TEST)
        glDepthMask(GL_TRUE)
        glDepthFunc(GL_LEQUAL)
        glDepthRange(0.0, 1.0)
        glEnable(GL_DEPTH_CLAMP)

        glEnable(GL_LIGHT0)
        fv4 = [0.3, 0.3, 0.3, 1.0]
        
        glShadeModel(GL_SMOOTH)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, fv4)
        glLightfv(GL_LIGHT0,GL_POSITION, fv4)
        glLightfv(GL_LIGHT0,GL_DIFFUSE, fv4)
        glEnable(GL_LIGHTING)
        glEnable(GL_MULTISAMPLE)  
        
        glRotatef(0, 30, 30, 30)
        glClearColor (0.5, 0.5, 0.5, 0.5)
        glClearDepth(1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        r = 25
        gluLookAt(r*math.sin(0.25*PI)*math.cos(theta1), r*math.sin(0.25*PI)*math.sin(theta1), r*math.cos(0.25*PI), LookAt.x, LookAt.y, LookAt.z, Sky.x, Sky.y, Sky.z)
        
        axes()

        for i in range(-2, 2):
            for j in range(-2, 2):
                for k in range(-2, 2):
                    if (i+j+k)%3 == 1:
                        tar4 = t4.tarugo4D(((center + base4D_1.scale(i)) + base4D_2.scale(j)) + base4D_3.scale(k), base4D_1, base4D_2, base4D_3, base4D_4, True)
                        tar4.drawTarugo(theta, 10)

        pygame.display.flip()
        pygame.time.wait(10)
        #theta += 0.01
        theta1 += 0.01

button_Draw = Button(root, text="Graph 4D Lattice", command = draw4D)
button_Draw.place(relx = 0.07*5 + 0.3, rely = 0.435, anchor = CENTER)


def draw5D():
    global theta

    global base5D_1
    global base5D_2
    global base5D_3
    global base5D_4
    global base5D_4

    Qx = string_split(dim5_0[0].get())
    Qy = string_split(dim5_0[1].get())
    Qz = string_split(dim5_0[2].get())
    Qw = string_split(dim5_0[3].get())
    Qt = string_split(dim5_0[4].get())

    Qx1 = string_split(dim5_1[0].get())
    Qy1 = string_split(dim5_1[1].get())
    Qz1 = string_split(dim5_1[2].get())
    Qw1 = string_split(dim5_1[3].get())
    Qt1 = string_split(dim5_1[4].get())

    Qx2 = string_split(dim5_2[0].get())
    Qy2 = string_split(dim5_2[1].get())
    Qz2 = string_split(dim5_2[2].get())
    Qw2 = string_split(dim5_2[3].get())
    Qt2 = string_split(dim5_2[4].get())

    Qx3 = string_split(dim5_3[0].get())
    Qy3 = string_split(dim5_3[1].get())
    Qz3 = string_split(dim5_3[2].get())
    Qw3 = string_split(dim5_3[3].get())
    Qt3 = string_split(dim5_3[4].get())

    Qx4 = string_split(dim5_4[0].get())
    Qy4 = string_split(dim5_4[1].get())
    Qz4 = string_split(dim5_4[2].get())
    Qw4 = string_split(dim5_4[3].get())
    Qt4 = string_split(dim5_4[4].get())

    base5D_1 = v5.Vector5D(Qx.num/Qx.den, Qy.num/Qy.den, Qz.num/Qz.den, Qw.num/Qw.den, Qt.num/Qt.den)
    base5D_2 = v5.Vector5D(Qx1.num/Qx1.den, Qy1.num/Qy1.den, Qz1.num/Qz1.den, Qw1.num/Qw1.den, Qt1.num/Qt1.den)
    base5D_3 = v5.Vector5D(Qx2.num/Qx2.den, Qy2.num/Qy2.den, Qz2.num/Qz2.den, Qw2.num/Qw2.den, Qt2.num/Qt2.den)
    base5D_4 = v5.Vector5D(Qx3.num/Qx3.den, Qy3.num/Qy3.den, Qz3.num/Qz3.den, Qw3.num/Qw3.den, Qt3.num/Qt3.den)
    base5D_5 = v5.Vector5D(Qx4.num/Qx4.den, Qy4.num/Qy4.den, Qz4.num/Qz4.den, Qw4.num/Qw4.den, Qt4.num/Qt4.den)

    center = v5.Vector5D(0, 0, 0, 0, 0)
    base0 = v5.Vector5D(3, 0, 0, 0, 0)
    base1 = v5.Vector5D(0, 3, 0, 0, 0)
    base2 = v5.Vector5D(0, 0, 3, 0, 0)
    base3 = v5.Vector5D(0, 0, 0, 3, 0)
    base4 = v5.Vector5D(0, 0, 0, 0, 3)

    theta = 0.0
    theta1 = 0.0
    pygame.init()
    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.001, 50.0)
    
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    theta += 0.1
            if event.type == pygame.MOUSEBUTTONDOWN:
                theta += 0.1

        
        glEnable(GL_DEPTH_TEST)
        glDepthMask(GL_TRUE)
        glDepthFunc(GL_LEQUAL)
        glDepthRange(0.0, 1.0)
        glEnable(GL_DEPTH_CLAMP)

        glEnable(GL_LIGHT0)
        fv4 = [0.3, 0.3, 0.3, 1.0]
        
        glShadeModel(GL_SMOOTH)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, fv4)
        glLightfv(GL_LIGHT0,GL_POSITION, fv4)
        glLightfv(GL_LIGHT0,GL_DIFFUSE, fv4)
        glEnable(GL_LIGHTING)
        glEnable(GL_MULTISAMPLE)  
        
        glRotatef(0, 30, 30, 30)
        glClearColor (0.5, 0.5, 0.5, 0.5)
        glClearDepth(1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        r = 25
        gluLookAt(r*math.sin(0.25*PI)*math.cos(theta1), r*math.sin(0.25*PI)*math.sin(theta1), r*math.cos(0.25*PI), LookAt.x, LookAt.y, LookAt.z, Sky.x, Sky.y, Sky.z)
        
        axes()

        for i in range(-2, 2):
            for j in range(-2, 2):
                for k in range(-2, 2):
                    if (i+j+k)%2 == 0:
                        tar5 = t5.tarugo5D(((center + base5D_1.scale(i)) + base5D_2.scale(j)) + base5D_3.scale(k), base5D_1, base5D_2, base5D_3, base5D_4, base5D_5, False)
                        tar6 = t5.tarugo5D(((center + base5D_1.scale(i)) + base5D_2.scale(j)) + base5D_3.scale(k), base5D_1, base5D_2, base5D_3, base5D_4, base5D_5, True)
                        tar5.drawTarugo(theta1*3, 10)
                        tar6.drawTarugo(theta1*3, 10)

        pygame.display.flip()
        pygame.time.wait(10)
        #theta += 0.01
        theta1 += 0.01

button_Draw5 = Button(root, text="Graph 5D Lattice", command = draw5D)
button_Draw5.place(relx = 0.07*6 + 0.3, rely = 0.6, anchor = CENTER)


########################
#                      #
#                      #
#     MANIM BUTTON     #
#                      #
#                      #
########################

def terminalAccess():
    os.system( 'python Main.py' )#'python -m manim latticeVid.py -pl')
lb.place(relx = 0.5, rely = 0.04, anchor = CENTER)
button_Draw = Button(root, text="MANIM", command = terminalAccess)
button_Draw.place(relx = 0.65, rely = 0.04, anchor = CENTER)

###################
#                 #
#   QUIT BUTTON   #
#                 #
################### 

button_quit = Button(root, text = "Exit", command = root.quit)
button_quit.place(relx = 0.5, rely =0.9, anchor = CENTER)


root.mainloop()
