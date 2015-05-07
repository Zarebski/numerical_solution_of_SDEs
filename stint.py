import numpy as np 

np.random.seed(200)    # set the seed of the random number generator 

def main():
	T = 1.
	N = 10**5
	dt = T/N
	dW = np.sqrt(dt)*np.random.normal(size=N)
	W = np.cumsum(dW)
	W = np.hstack(([0],W))
	
	ito = np.sum( W[0:-1]*dW)						# approx ito integral
 	itoerr = np.abs( ito - 0.5*( W[-1]**2 - T ) ) 	# truncation error

	print "Error with N = %d is %f" % (N, itoerr)
	


if __name__ == '__main__':
	main()