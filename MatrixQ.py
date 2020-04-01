import Q
import random 

class MatrixQ:
	
	def __init__(self, rows, columns):
		self.m = rows
		self.n =columns 
		self.A = [[Q.Rational(0, 1) for y in range(self.n)] for x in range(self.m)]

	def add(self, i, j, q):
		self.A[i][j] *= Q.Rational(0, 1)
		self.A[i][j] += q

	def __str__(self):
		k = 21
		S = ""
		for i in range(0, self.m):
			for j in range(0, self.n):
				S += str(self.A[i][j])
				l = self.A[i][j].digitCounter()	
				for r in range(0, k-l):
					S += " "
			S += "\n\n\n"
		return S

	def __add__(self, B):
		if (self.m != B.m) or (self.n != B.n):
			print("\n\nDimension Error\n\n\n")
			return
		else:
			C = MatrixQ(self.m, self.n)
			for i in range(0, self.m):
				for j in range(0, self.n):
					C.A[i][j] = self.A[i][j] + B.A[i][j]
		return C			

	def __sub__(self, B):
		if (self.m != B.m) or (self.n != B.n):
			print("\n\nDimension Error\n\n\n")
			return
		else:
			C = MatrixQ(self.m, self.n)
			for i in range(0, self.m):
				for j in range(0, self.n):
					C.A[i][j] = self.A[i][j] - B.A[i][j]
		return C

	def __mul__(self, B):
		if self.n != B.m:
			print("\n\nDimension Error\n")
			return
		else:
			C = MatrixQ(self.m, B.n)
			for i in range(0, C.m):
				for j in range(0, C.n):
					for k in range(0, self.n):
						C.A[i][j] += (self.A[i][k] * B.A[k][j])
		return C			




# Testing out code
#matGo = MatrixQ(3, 3)
#matGo1 = MatrixQ(3, 3)

#for i in range(0, matGo.m):
#	for j in range(0, matGo.n):
#		m1 = random.randint(-20, 20)
#		n1 = random.randint(-20, 20)
#		if n1 == 0:
#			matGo.add(i, j, Q.Rational(m1, 1))
#		else:
#			matGo.add(i, j, Q.Rational(m1, n1))


#for i in range(0, matGo1.m):
#	for j in range(0, matGo1.n):
#		m1 = random.randint(-20, 20)
#		n1 = random.randint(-20, 20)
#		if n1 == 0:
#			matGo1.add(i, j, Q.Rational(m1, 1))
#		else:
#			matGo1.add(i, j, Q.Rational(m1, n1))
#print("A = \n")
#print(matGo)
#print("\n\n")
#print("B = \n")
#print(matGo1)
#print("\n\nA+B = \n")
#print(matGo + matGo1)
#print("\n\nA-B = \n")
#print(matGo - matGo1)
#print("\n\nA*B = \n")
#print(matGo * matGo1)