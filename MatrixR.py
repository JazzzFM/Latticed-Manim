class MatrixR:
	def __init__(self, rows, columns):
		self.m = rows
		self.n =columns
		self.A = [[0 for y in range(self.n)] for x in range(self.m)]

	def add(self, i, j, q):
		self.A[i][j] *= 0
		self.A[i][j] += q

	def __add__(self, B):
		if (self.m != B.m) or (self.n != B.n):
			print("\n\nDimension Error\n\n\n")
			return
		else:
			C = MatrixR(self.m, self.n)
			for i in range(0, self.m):
				for j in range(0, self.n):
					C.A[i][j] = self.A[i][j] + B.A[i][j]
		return C

	def __sub__(self, B):
		if (self.m != B.m) or (self.n != B.n):
			print("\n\nDimension Error\n\n\n")
			return
		else:
			C = MatrixR(self.m, self.n)
			for i in range(0, self.m):
				for j in range(0, self.n):
					C.A[i][j] = self.A[i][j] - B.A[i][j]
		return C

	def __mul__(self, B):
		if self.n != B.m:
			print("\n\nDimension Error\n")
			return
		else:
			C = MatrixR(self.m, B.n)
			for i in range(0, C.m):
				for j in range(0, C.n):
					for k in range(0, self.n):
						C.A[i][j] += (self.A[i][k] * B.A[k][j])
		return C
