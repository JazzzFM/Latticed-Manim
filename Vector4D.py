import math
import Vector as v3d
import MatrixR

class Vector4D():
	def __init__(self, x, y, z, w):
		self.x = x
		self.y = y
		self.z = z
		self.w = w

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + "," + str(self.w) + ")" 

	def __add__(self, b):
		return Vector4D(self.x + b.x, self.y + b.y, self.z + b.z, self.w + b.w)
	
	def __sub__(self, b):
		return Vector4D(self.x - b.x, self.y - b.y, self.z - b.z, self.w - b.w)

	def __mul__(self, b):
		return (self.x * b.x) + (self.y * b.y) + (self.z * b.z)  + (self.w * b.w)

	#def __truediv__(self, b):
	#	return Vector4D(self.y * b.z - self.z * b.y,
	#		 		   -self.x * b.z + self.z * b.x,
	#		 		    self.x * b.y - self.y * b.x)

	def scale(self, a):
		return Vector4D(a * self.x, a * self.y, a * self.z, a * self.w)

	def abs(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

	def unit(self):
		return self.scale(1/(self.abs()))

	def matMult(self, mat):
		v0 = Vector4D(mat.A[0][0], mat.A[1][0], mat.A[2][0], mat.A[3][0])
		v1 = Vector4D(mat.A[0][1], mat.A[1][1], mat.A[2][1], mat.A[3][1])
		v2 = Vector4D(mat.A[0][2], mat.A[1][2], mat.A[2][2], mat.A[3][2])
		v3 = Vector4D(mat.A[0][3], mat.A[1][3], mat.A[2][3], mat.A[3][3])

		return v0.scale(self.x) + v1.scale(self.y) + v2.scale(self.z) + v3.scale(self.w) 

	def proyVec(self, proy):
		p = self.scale(proy/(proy - self.w))
		return v3d.Vector3D(p.x, p.y, p.z)

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