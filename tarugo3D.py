import Vector as v
from OpenGL.GL import *
from OpenGL.GLU import *

class tarugo3D(object):
	"""docstring for tarugo3D"""
	def __init__(self, center, base0, base1, base2, T):
		self.center = center
		self.base0 = base0
		self.base1 = base1
		self.base2 = base2
		self.T = T

	def setCube(self):
		pass

	def drawTarugo(self):
		v0 = ((self.center + self.base0) + self.base1) + self.base2
		v1 = (self.center + self.base1) + self.base2
		v2 = self.center + self.base2
		v3 = (self.center + self.base0) + self.base2

		v4 = (self.center + self.base0) + self.base1
		v5 = self.center + self.base1
		v6 = self.center
		v7 = self.center + self.base0

		#for i in range(0, 8):
		#	CUBO[i] = CUBO[i].inversion(3)


		if self.T == True:
			quad(v0, v1, v2, v3)
			quad(v7, v6, v5, v4)
			quad(v0, v3, v7, v4)
			quad(v1, v5, v6, v2)
			quad(v2, v6, v7, v3)
			quad(v1, v0, v4, v5)
		else:
			line(v0, v1, 2)
			line(v1, v2, 2)
			line(v2, v3, 2)
			line(v3, v0, 2)
			
			line(v4, v0, 2)
			line(v5, v1, 2)
			line(v6, v2, 2)
			line(v7, v3, 2)
			
			line(v4, v5, 2)
			line(v5, v6, 2)
			line(v6, v7, 2)
			line(v7, v4, 2)

def quad(v0, v1, v2, v3):
	n = (v2/v0)
	glColorMaterial(GL_FRONT, GL_EMISSION)
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