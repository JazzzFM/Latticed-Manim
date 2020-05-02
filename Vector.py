import math
import MatrixR

class Vector3D():
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")" 

	def __add__(self, w):
		return Vector3D(self.x + w.x, self.y + w.y, self.z + w.z)
	
	def __sub__(self, w):
		return Vector3D(self.x - w.x, self.y - w.y, self.z - w.z)

	def __mul__(self, w):
		return (self.x * w.x) + (self.y * w.y) + (self.z * w.z)

	def __truediv__(self, w):
		return Vector3D(self.y * w.z - self.z * w.y,
			 		   -self.x * w.z + self.z * w.x,
			 		    self.x * w.y - self.y * w.x)

	def scale(self, a):
		return Vector3D(a * self.x, a * self.y, a * self.z)

	def abs(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def unit(self):
		return self.scale(1/(self.abs()))

	def matMult(self, mat):
		v0 = Vector3D(mat.A[0][0], mat.A[1][0], mat.A[2][0])
		v1 = Vector3D(mat.A[0][1], mat.A[1][1], mat.A[2][1])
		v2 = Vector3D(mat.A[0][2], mat.A[1][2], mat.A[2][2])

		return v0.scale(self.x) + v1.scale(self.y) + v2.scale(self.z) 

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