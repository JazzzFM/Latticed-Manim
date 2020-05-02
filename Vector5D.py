import math
import Vector as v3d
import Vector4D as v4d
import MatrixR

class Vector5D():
	def __init__(self, x, y, z, w, t):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
		self.t = t

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w) + "," + str(self.t) + ")" 

	def __add__(self, b):
		return Vector5D(self.x + b.x, self.y + b.y, self.z + b.z, self.w + b.w, self.t + b.t)
	
	def __sub__(self, b):
		return Vector5D(self.x - b.x, self.y - b.y, self.z - b.z, self.w - b.w, self.t - b.t)

	def __mul__(self, b):
		return (self.x * b.x) + (self.y * b.y) + (self.z * b.z)  + (self.w * b.w)  + (self.t * b.t)

	#def __truediv__(self, b):
	#	return Vector5D(self.y * b.z - self.z * b.y,
	#		 		   -self.x * b.z + self.z * b.x,
	#		 		    self.x * b.y - self.y * b.x)

	def scale(self, a):
		return Vector5D(a * self.x, a * self.y, a * self.z, a * self.w, a * self.t)

	def abs(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2 + self.t**2)

	def unit(self):
		return self.scale(1/(self.abs()))

	def matMult(self, mat):
		v0 = Vector5D(mat.A[0][0], mat.A[1][0], mat.A[2][0], mat.A[3][0], mat.A[4][0])
		v1 = Vector5D(mat.A[0][1], mat.A[1][1], mat.A[2][1], mat.A[3][1], mat.A[4][1])
		v2 = Vector5D(mat.A[0][2], mat.A[1][2], mat.A[2][2], mat.A[3][2], mat.A[4][2])
		v3 = Vector5D(mat.A[0][3], mat.A[1][3], mat.A[2][3], mat.A[3][3], mat.A[4][3])
		v4 = Vector5D(mat.A[0][4], mat.A[1][4], mat.A[2][4], mat.A[3][4], mat.A[4][4])

		return v0.scale(self.x) + v1.scale(self.y) + v2.scale(self.z) + v3.scale(self.w) + v4.scale(self.t) 

	def proyVec(self, proy):
		p = self.scale(proy/(proy - self.t))
		return v4d.Vector4D(p.x, p.y, p.z, p.w)

	def inversion(self, r):

		if self.abs() < r:
			u = self.unit()
			const = (r*r)/self.abs()
			return u.scale(const)
		else:
			if abs(self.abs() - r) < 0.000000001:
				return self
			else:
				u = self.unit()
				const = (r*r)/self.abs()
				return u.scale(const)