from math import *

def euclidean_algorithm(x, y, verbose=True):
	if x < y:
		return euclidean_algorithm(y, x, verbose)
	print()
	while y != 0:
		if verbose: print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
		(x, y) = (y, x % y)
	
	if verbose: print('gcd = %s' % x) 
	return x

euclidean_algorithm(56343, 2072)
euclidean_algorithm(31363, 3761)