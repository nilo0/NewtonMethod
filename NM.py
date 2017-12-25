
print('Please enter coeff tuple: ')
coeff = tuple(float(x.strip()) for x in raw_input().split(','))
x0 = float(input('Please enter x0: '))
E = float(input('Please enter e: '))


def Poly(A, x):
	return sum([ai * x**i for (i, ai) in enumerate(A)])

def dPoly(A, x):
	return sum([ai * i * x**(i-1) for (i, ai) in enumerate(A) if i != 0])

def newton(A, x, e):
	if Poly(A, x) <= e:
		print "x: ", x, "f(x) = ", Poly(A, x)
		return

	newton(A, x - (Poly(A, x) / dPoly(A, x)), e)


newton(coeff, x0, E)
