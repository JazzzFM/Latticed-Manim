import Vector as v
from OpenGL.GL import *
from OpenGL.GLU import *

class cube(object):
	"""docstring for cube"""
	def __init__(self, center, radius):
		self.center = center
		self.radius = radius

	def setCube(self):
		pass

	def drawCubo(self):
		CUBO = [
			v.Vector3D( self.radius + self.center.x, self.radius + self.center.y, self.radius + self.center.z),
			v.Vector3D(-self.radius + self.center.x, self.radius + self.center.y, self.radius + self.center.z),
			v.Vector3D(-self.radius + self.center.x,-self.radius + self.center.y, self.radius + self.center.z),
			v.Vector3D( self.radius + self.center.x,-self.radius + self.center.y, self.radius + self.center.z),
			v.Vector3D( self.radius + self.center.x, self.radius + self.center.y,-self.radius + self.center.z),
			v.Vector3D(-self.radius + self.center.x, self.radius + self.center.y,-self.radius + self.center.z),
			v.Vector3D(-self.radius + self.center.x,-self.radius + self.center.y,-self.radius + self.center.z),
			v.Vector3D( self.radius + self.center.x,-self.radius + self.center.y,-self.radius + self.center.z)
		]

		#for i in range(0, 8):
		#	CUBO[i] = CUBO[i].inversion(3)

		self.setCube()
		glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
		glFrontFace(GL_CCW);
		glEnable(GL_CULL_FACE)
		glCullFace(GL_BACK)
		glBegin(GL_POLYGON)
		#glNormal3d(normal0, normal1, normal2)
		glColor3f(0, 0, 255)
		glVertex3f(CUBO[0].x, CUBO[0].y, CUBO[0].z)
		glVertex3f(CUBO[1].x, CUBO[1].y, CUBO[1].z)
		glColor3f(255, 0, 0)
		glVertex3f(CUBO[2].x, CUBO[2].y, CUBO[2].z)
		glVertex3f(CUBO[3].x, CUBO[3].y, CUBO[3].z)
		glEnd()

		glFrontFace(GL_CCW);
		glEnable(GL_CULL_FACE)
		glCullFace(GL_BACK)
		glBegin(GL_POLYGON)
		#glNormal3d(normal0, normal1, normal2)
		glColor3f(0, 0, 255)
		glVertex3f(CUBO[7].x, CUBO[7].y, CUBO[7].z)
		glVertex3f(CUBO[6].x, CUBO[6].y, CUBO[6].z)
		glColor3f(255, 0, 0)
		glVertex3f(CUBO[5].x, CUBO[5].y, CUBO[5].z)
		glVertex3f(CUBO[4].x, CUBO[4].y, CUBO[4].z)
		glEnd()

		glFrontFace(GL_CCW);
		glEnable(GL_CULL_FACE)
		glCullFace(GL_BACK)
		glBegin(GL_POLYGON)
		#glNormal3d(normal0, normal1, normal2)
		glColor3f(0, 0, 255)
		glVertex3f(CUBO[0].x, CUBO[0].y, CUBO[0].z)
		glVertex3f(CUBO[3].x, CUBO[3].y, CUBO[3].z)
		glColor3f(255, 0, 0)
		glVertex3f(CUBO[7].x, CUBO[7].y, CUBO[7].z)
		glVertex3f(CUBO[4].x, CUBO[4].y, CUBO[4].z)
		glEnd()

		glFrontFace(GL_CCW);
		glEnable(GL_CULL_FACE)
		glCullFace(GL_BACK)
		glBegin(GL_POLYGON)
		#glNormal3d(normal0, normal1, normal2)
		glColor3f(0, 0, 255)
		glVertex3f(CUBO[1].x, CUBO[1].y, CUBO[1].z)
		glVertex3f(CUBO[5].x, CUBO[5].y, CUBO[5].z)
		glColor3f(255, 0, 0)
		glVertex3f(CUBO[6].x, CUBO[6].y, CUBO[6].z)
		glVertex3f(CUBO[2].x, CUBO[2].y, CUBO[2].z)
		glEnd()

		glFrontFace(GL_CCW);
		glEnable(GL_CULL_FACE)
		glCullFace(GL_BACK)
		glBegin(GL_POLYGON)
		#glNormal3d(normal0, normal1, normal2)
		glColor3f(0, 0, 255)
		glVertex3f(CUBO[2].x, CUBO[2].y, CUBO[2].z)
		glVertex3f(CUBO[6].x, CUBO[6].y, CUBO[6].z)
		glColor3f(255, 0, 0)
		glVertex3f(CUBO[7].x, CUBO[7].y, CUBO[7].z)
		glVertex3f(CUBO[3].x, CUBO[3].y, CUBO[3].z)
		glEnd()

		glFrontFace(GL_CCW);
		glEnable(GL_CULL_FACE)
		glCullFace(GL_BACK)
		glBegin(GL_POLYGON)
		#glNormal3d(normal0, normal1, normal2)
		glColor3f(0, 0, 255)
		glVertex3f(CUBO[1].x, CUBO[1].y, CUBO[1].z)
		glVertex3f(CUBO[0].x, CUBO[0].y, CUBO[0].z)
		glColor3f(255, 0, 0)
		glVertex3f(CUBO[4].x, CUBO[4].y, CUBO[4].z)
		glVertex3f(CUBO[5].x, CUBO[5].y, CUBO[5].z)
		glEnd()





#c = cube(v.Vector3D(0, 0, 0), 1)
#c.drawCube()