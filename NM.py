# calculating the value of a given polynomial
def Poly(A, x):
	return sum([ai * x**i for (i, ai) in enumerate(A)])

# calculating the value of the differential of a given polynomial
def dPoly(A, x):
	return sum([ai * i * x**(i-1) for (i, ai) in enumerate(A) if i != 0])

# calculating the Newton Method for a given polynomial and a precission
def newton(A, x, e):
	if Poly(A, x) <= e:
		print "x: ", x, "f(x) = ", Poly(A, x)
		return

	newton(A, x - (Poly(A, x) / dPoly(A, x)), e)


# reading input from user
print('Please enter coeff tuple: ')
coeff = tuple(float(x.strip()) for x in raw_input().split(','))
x0 = float(input('Please enter x0: '))
E = float(input('Please enter e: '))

# calling newton fct with user's inputs
newton(coeff, x0, E)
