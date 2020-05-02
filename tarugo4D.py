import Vector as v
import Vector4D as v4
import MatrixR as mat
import math
import cube as c
from OpenGL.GL import *
from OpenGL.GLU import *

class tarugo4D(object):
	"""docstring for tarugo4D"""
	def __init__(self, center, base0, base1, base2, base3, T):
		self.center = center
		self.base0 = base0
		self.base1 = base1
		self.base2 = base2
		self.base3 = base3
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

		v = [ v0,  v1,  v2,  v3,
			  v4,  v5,  v6,  v7,
			  v8,  v9, v10, v11,
			 v12, v13, v14, v15]


		RotZW = mat.MatrixR(4, 4)
		RotZW.add(0, 0, 1) 
		RotZW.add(1, 0, 0) 
		RotZW.add(2, 0, 0) 
		RotZW.add(3, 0, 0)

		RotZW.add(0, 1, 0) 
		RotZW.add(1, 1, 1) 
		RotZW.add(2, 1, 0) 
		RotZW.add(3, 1, 0)

		RotZW.add(0, 2, 0) 
		RotZW.add(1, 2, 0) 
		RotZW.add(2, 2, math.cos(angle)) 
		RotZW.add(3, 2, math.sin(angle))

		RotZW.add(0, 3, 0) 
		RotZW.add(1, 3, 0) 
		RotZW.add(2, 3,-math.sin(angle)) 
		RotZW.add(3, 3, math.cos(angle))

		for i in range(0, 16): 
			v[i] = v[i].matMult(RotZW)

		v1 = [v[y].proyVec(proy) for y in range(16)]

	#	for i in range(0, 16):
	#		C = c.cube(v1[i], 0.2)
	#		C.drawCubo()

		if self.T == True:
			
			quad(v1[0], v1[1], v1[2], v1[3])
			quad(v1[7], v1[6], v1[5], v1[4])
			quad(v1[0], v1[3], v1[7], v1[4])
			quad(v1[1], v1[5], v1[6], v1[2])
			quad(v1[2], v1[6], v1[7], v1[3])
			quad(v1[1], v1[0], v1[4], v1[5])
		else:

			line(v1[0], v1[1], 2)
			line(v1[1], v1[2], 2)
			line(v1[2], v1[3], 2)
			line(v1[3], v1[0], 2)
			line(v1[4], v1[5], 2)
			line(v1[5], v1[6], 2)
			line(v1[6], v1[7], 2)
			line(v1[7], v1[4], 2)
			line(v1[0], v1[4], 2)
			line(v1[1], v1[5], 2)
			line(v1[2], v1[6], 2)
			line(v1[3], v1[7], 2)

			line(v1[8], v1[9], 2)
			line(v1[9], v1[10], 2)
			line(v1[10], v1[11], 2)
			line(v1[11], v1[8], 2)

			line(v1[12], v1[13], 2)
			line(v1[13], v1[14], 2)
			line(v1[14], v1[15], 2)
			line(v1[15], v1[12], 2)

			line(v1[0], v1[8], 2)
			line(v1[1], v1[9], 2)
			line(v1[2], v1[10], 2)
			line(v1[3], v1[11], 2)

			line(v1[4], v1[12], 2)
			line(v1[5], v1[13], 2)
			line(v1[6], v1[14], 2)
			line(v1[7], v1[15], 2)

			line(v1[8], v1[12], 2)
			line(v1[9], v1[13], 2)
			line(v1[10], v1[14], 2)
			line(v1[11], v1[15], 2)
			

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


