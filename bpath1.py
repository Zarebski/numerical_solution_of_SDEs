import numpy as np 

def main():
	"""Brownian path simulation"""
	np.random.seed(100)		# set the seed of the random number generator
	T = 1. 					
	N = 500					
	dt = T/N 				

	dW = np.zeros(N) 		# preallocate arrays ...
	W = np.zeros(N)			# for efficiency

if __name__ == '__main__':
	main()
