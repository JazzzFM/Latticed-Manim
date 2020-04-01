class Rational:
	def __init__(self, numerador, denominador):
		self.num = numerador
		self.den = denominador
		d = mcd(self.num, self.den)
		self.den /= d
		self.num /= d

		self.num = int(self.num)
		self.den = int(self.den)

		if self.den < 0:
			self.den = -self.den
			self.num = -self.num


	def __str__(self):
		if self.num == self.den:
			return "1"
		else:	
			if self.num == 0:
				return "0"
			else:
				if self.den == 1:
					return str(self.num)
				else:
					return str(self.num) + "/" + str(self.den)	

	def __add__(self, q):
		return Rational((self.num * q.den) + (self.den * q.num), self.den * q.den)
		
	def __sub__(self, q):
		return Rational((self.num * q.den) - (self.den * q.num), self.den * q.den)

	def __mul__(self, q):
		return Rational(self.num * q.num, self.den * q.den)
		
	def __truediv__(self, q):
		return Rational(self.num * q.den, self.den * q.num)

	def __pow__(self, n):
		aux = Rational(1, 1)
		for i in range (0, n):
			aux *= self
		return aux		

	def __iadd__(self, q):
		return Rational((self.num * q.den) + (self.den * q.num), self.den * q.den)
			
	def __isub__(self, q):
		return Rational((self.num * q.den) - (self.den * q.num), self.den * q.den)
	
	def __imul__(self, q):
		return Rational(self.num * q.num, self.den * q.den)
	
	def __idiv__(self, q):
		return Rational(self.num * q.den, self.den * q.num)

	def __neg__(self):
		return Rational(-self.num, self.den)

	def __invert__(self):
		return Rational(self.den, self.num)

	def __ipow__(self, n):
		aux = Rational(1, 1)
		for i in range (0, n):
			aux *= self
		return aux		

	def __eq__(self, q):
		if self.num == q.num and self.den == q.den:
			return True
		else: 
			return False

	def __ne__(self, q):
		if self.num == q.num and self.den == q.den:
			return False
		else: 
			return True

	def __lt__(self, q):
		if (self.num/self.den) < (q.num/q.den):
			return True
		else:
			return False

	def __gt__(self, q):
		if (self.num/self.den) > (q.num/q.den):
			return True
		else:
			return False			 						
	
	def __le__(self, q):
		if (self.num/self.den) <= (q.num/q.den):
			return True
		else:
			return False

	def __ge__(self, q):
		if (self.num/self.den) >= (q.num/q.den):
			return True
		else:
			return False

	def digitCounter(self):

		if self > Rational(0, 1):
			if self != Rational(1, 1):
				if self.den == 1:
					return intCount(self.num)
				else:
					return intCount(self.num) + 1 + intCount(self.den)
			else: 
				return 1
		else:
			if self == Rational(0, 1):
				return 1
			else:
				if self == Rational(-1, 1) or self == Rational(1,-1):
					return 2
				else: 
					if self.den == 1:
						return intCount(self.num) + 1
					else:
						return intCount(self.num) + 2 + intCount(self.den)
	#	if self < Rational(0, 1):
	#		return intCount(self.num) + 2 + intCount(self.den)
	#	else:
	#		return intCount(self.num) + 1 + intCount(self.den) 		


def mcd(m, n):

	if m < 0:
		m = -m
	if n < 0:
		n = -n
	if n == m:
		return m

	r = m%n	

	while r != 0:
		m = n
		n = r
		r = m%n

	return n

def intCount(n):
	count = 0
	if n == 0:
		return 1
	else:
		if n < 0:
			n *= -1
		while n != 0:
			count = count + 1
			n = n//10
	return count