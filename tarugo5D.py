import Vector as v
import Vector4D as v4
import Vector5D as v5
import MatrixR as mat
import math
import cube as c
from OpenGL.GL import *
from OpenGL.GLU import *

class tarugo5D(object):
	"""docstring for tarugo5D"""
	def __init__(self, center, base0, base1, base2, base3, base4, T):
		self.center = center
		self.base0 = base0
		self.base1 = base1
		self.base2 = base2
		self.base3 = base3
		self.base4 = base4
		self.T = T

	def setCube(self):
		pass

	def drawTarugo(self, angle, proy):
		v0 = ((self.center + self.base0) + self.base1) + self.base2
		v1 = (self.center + self.base1) + self.base2
		v2 = self.center + self.base2
		v3 = (self.center + self.base0) + self.base2

		v4 = (self.center + self.base0) + self.base1
		v5 = self.center + self.base1
		v6 = self.center
		v7 = self.center + self.base0

		v8 = (((self.center + self.base0) + self.base1) + self.base2) + self.base3
		v9 = ((self.center + self.base1) + self.base2) + self.base3
		v10 = (self.center + self.base2) + self.base3
		v11 = ((self.center + self.base0) + self.base2) + self.base3

		v12 = ((self.center + self.base0) + self.base1) + self.base3
		v13 = (self.center + self.base1) + self.base3
		v14 = self.center + self.base3
		v15 = (self.center + self.base0) + self.base3

		v16 = (((self.center + self.base0) + self.base1) + self.base2) + self.base4
		v17 = ((self.center + self.base1) + self.base2) + self.base4
		v18 = (self.center + self.base2) + self.base4
		v19 = ((self.center + self.base0) + self.base2) + self.base4

		v20 = ((self.center + self.base0) + self.base1) + self.base4
		v21 = (self.center + self.base1) + self.base4
		v22 = self.center + self.base4
		v23 = (self.center + self.base0) + self.base4

		v24 = ((((self.center + self.base0) + self.base1) + self.base2) + self.base3) + self.base4
		v25 = (((self.center + self.base1) + self.base2) + self.base3) + self.base4
		v26 = ((self.center + self.base2) + self.base3) + self.base4
		v27 = (((self.center + self.base0) + self.base2) + self.base3) + self.base4

		v28 = (((self.center + self.base0) + self.base1) + self.base3) + self.base4
		v29 = ((self.center + self.base1) + self.base3) + self.base4
		v30 = (self.center + self.base3) + self.base4
		v31 = ((self.center + self.base0) + self.base3) + self.base4

		v = [ v0,  v1,  v2,  v3,
			  v4,  v5,  v6,  v7,
			  v8,  v9, v10, v11,
			 v12, v13, v14, v15,
			 v16, v17, v18, v19,
			 v20, v21, v22, v23,
			 v24, v25, v26, v27,
			 v28, v29, v30, v31]


		RotZW = mat.MatrixR(5, 5)
		RotZW.add(0, 0, 1) 
		RotZW.add(1, 0, 0) 
		RotZW.add(2, 0, 0) 
		RotZW.add(3, 0, 0)
		RotZW.add(4, 0, 0)

		RotZW.add(0, 1, 0) 
		RotZW.add(1, 1, 1) 
		RotZW.add(2, 1, 0) 
		RotZW.add(3, 1, 0)
		RotZW.add(4, 1, 0)

		RotZW.add(0, 2, 0) 
		RotZW.add(1, 2, 0) 
		RotZW.add(2, 2, 1) 
		RotZW.add(3, 2, 0)
		RotZW.add(4, 2, 0)

		RotZW.add(0, 3, 0) 
		RotZW.add(1, 3, 0)
		RotZW.add(2, 3, 0) 
		RotZW.add(3, 3, math.cos(angle)) 
		RotZW.add(4, 3, math.sin(angle))

		RotZW.add(0, 4, 0) 
		RotZW.add(1, 4, 0)
		RotZW.add(2, 4, 0) 
		RotZW.add(3, 4,-math.sin(angle)) 
		RotZW.add(4, 4, math.cos(angle))

		for i in range(0, 32): 
			v[i] = v[i].matMult(RotZW)

		v1 = [v[y].proyVec(proy) for y in range(32)]

		v2 = [v1[y].proyVec(proy) for y in range(32)]

	#	for i in range(0, 16):
	#		C = c.cube(v1[i], 0.2)
	#		C.drawCubo()

		if self.T == True:
			
			quad(v2[0], v2[1], v2[2], v2[3])
			quad(v2[7], v2[6], v2[5], v2[4])
			quad(v2[0], v2[3], v2[7], v2[4])
			quad(v2[1], v2[5], v2[6], v2[2])
			quad(v2[2], v2[6], v2[7], v2[3])
			quad(v2[1], v2[0], v2[4], v2[5])
		else:

			line(v2[0], v2[1], 2)
			line(v2[1], v2[2], 2)
			line(v2[2], v2[3], 2)
			line(v2[3], v2[0], 2)
			line(v2[4], v2[5], 2)
			line(v2[5], v2[6], 2)
			line(v2[6], v2[7], 2)
			line(v2[7], v2[4], 2)
			line(v2[0], v2[4], 2)
			line(v2[1], v2[5], 2)
			line(v2[2], v2[6], 2)
			line(v2[3], v2[7], 2)

			line(v2[8], v2[9], 2)
			line(v2[9], v2[10], 2)
			line(v2[10], v2[11], 2)
			line(v2[11], v2[8], 2)

			line(v2[12], v2[13], 2)
			line(v2[13], v2[14], 2)
			line(v2[14], v2[15], 2)
			line(v2[15], v2[12], 2)

			line(v2[0], v2[8], 2)
			line(v2[1], v2[9], 2)
			line(v2[2], v2[10], 2)
			line(v2[3], v2[11], 2)

			line(v2[4], v2[12], 2)
			line(v2[5], v2[13], 2)
			line(v2[6], v2[14], 2)
			line(v2[7], v2[15], 2)

			line(v2[8], v2[12], 2)
			line(v2[9], v2[13], 2)
			line(v2[10], v2[14], 2)
			line(v2[11], v2[15], 2)
			

def quad(v0, v1, v2, v3):
	n = (v2/v0)
	glColorMaterial(GL_FRONT_AND_BACK, GL_EMISSION)
	glEnable(GL_COLOR_MATERIAL)
	glFrontFace(GL_CCW);
	glEnable(GL_CULL_FACE)
	glCullFace(GL_BACK)
	glBegin(GL_POLYGON)
	glNormal3d(n.x, n.y, n.z)
	glColor3f(0, 0, 255)
	glVertex3f(v0.x, v0.y, v0.z)
	glVertex3f(v1.x, v1.y, v1.z)
	glColor3f(255, 0, 0)
	glVertex3f(v2.x, v2.y, v2.z)
	glVertex3f(v3.x, v3.y, v3.z)
	glEnd()

def line(v0, v1, W):
	glLineWidth(W)
	glBegin(GL_LINES)
	glColor3f(0, 0, 0)
	glVertex3f(v0.x, v0.y, v0.z)
	glVertex3f(v1.x, v1.y, v1.z)
	glEnd()


