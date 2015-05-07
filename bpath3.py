import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)    # set the seed of the random number generator 

def bm(M=1):
	"""Generate an array of m discretizes Wiener paths"""
	T = 1.
	N = 500
	dt = T/N
	t = np.linspace(0, T, N+1)

	dW = np.sqrt(dt)*np.random.normal(size=(M,N))
	W = np.cumsum(dW,axis=1)
	W = np.hstack((np.zeros((M,1)),W))
	return t,W

def main():
	M = 10**4
	t,W = bm(M)
	
	U = np.exp( np.tile(t,[M,1]) + 0.5*W )
	print np.shape(U)
	Umean = np.mean(U, axis=0)
	averr = np.linalg.norm(Umean - np.exp(9*t/8), ord=np.inf)
	print "The sample error with M = %d is and %f" % (M,averr)

	plt.figure()
	plt.plot(t, Umean, 'b')
	plt.plot(t,U[0,:],'r',t,U[1,:],'r',t,U[2,:],'r',t,U[3,:],'r',t,U[4,:],'r')
	plt.show()

	return None

if __name__ == '__main__':
	main()

