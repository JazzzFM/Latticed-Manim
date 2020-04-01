import Vector as v
from OpenGL.GL import *
from OpenGL.GLU import *

def F0(u, v):
	return u

def F1(u, v):
	return v

def F2(u, v, A, B, C, D):
	return (D/C) + (-(A/C) * u) + (-(B/C) * v)		

class plane():
	def __init__(self, A, B, C, D):
		self.A = A
		self.B = B
		self.C = C
		self.D = D

	def graph(self, n):
		for i in range(-n, n + 1):
			for j in range(-n, n+1):

				u0 = i + (0.0)
				v0 = j + (0.0)

				u1 = i + (1.0)
				v1 = j + (0.0)

				u2 = i + (1.0)
				v2 = j + (1.0)

				u3 = i + (0.0)
				v3 = j + (1.0)

				G = [
					v.Vector3D(F0(u0, v0), F1(u0, v0), F2(u0, v0, self.A, self.B, self.C, self.D)),
					v.Vector3D(F0(u1, v1), F1(u1, v1), F2(u1, v1, self.A, self.B, self.C, self.D)),
					v.Vector3D(F0(u2, v2), F1(u2, v2), F2(u2, v2, self.A, self.B, self.C, self.D)),
					v.Vector3D(F0(u3, v3), F1(u3, v3), F2(u3, v3, self.A, self.B, self.C, self.D))
				]

				#glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
				#glFrontFace(GL_CCW);
				#glEnable(GL_CULL_FACE)
				#glCullFace(GL_BACK)
				#glBegin(GL_POLYGON)
				##glNormal3d(normal0, normal1, normal2)
				#glColor3f(200, 255, 200)
				#glVertex3f(G[0].x, G[0].y, G[0].z)
				##glColor3f(255, 0, 0)
				#glVertex3f(G[1].x, G[1].y, G[1].z)
				##glColor3f(0, 0, 255)
				#glVertex3f(G[2].x, G[2].y, G[2].z)
				##glColor3f(255, 0, 0)
				#glVertex3f(G[3].x, G[3].y, G[3].z)
				#glEnd()
				#
				glLineWidth(3.0)
				glBegin(GL_LINES)
				glColor3f(0, 0, 0)
				glVertex3f(G[0].x, G[0].y, G[0].z)
				glVertex3f(G[1].x, G[1].y, G[1].z)
				glEnd()

				glBegin(GL_LINES)
				glColor3f(0, 0, 0)
				glVertex3f(G[1].x, G[1].y, G[1].z)
				glVertex3f(G[2].x, G[2].y, G[2].z)
				glEnd()			