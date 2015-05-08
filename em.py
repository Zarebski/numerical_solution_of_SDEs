"""Euler-Maruyama method on linear SDE

SDE is dX = drift*X dt + diffusion*X dW,   X(0) = Xzero
where drift = 2, diffusion = 1 and Xzero = 1

Discretized Wiener path over [0,1] has dt = 2**(-8)
Euler-Maruyama uses timestep R*dt
"""

import numpy as np 
import matplotlib.pyplot as plt
import time

np.random.seed(100)

def main():
	drift = 2			# define the parameters...
	diffusion = 1 		# of the problem
	Xzero = 1

	T = 1. 				# generate a discretized...
	N = 2**11			# Wiener path
	dt = T/N
	dW = np.sqrt(dt)*np.random.normal(size=N)
	W = np.cumsum(dW)
	W = np.hstack(([0],W))
	t = np.linspace(0, T, N+1)

	# generate the true solution on the d-Wiener path
	Xtrue = Xzero*np.exp( (drift - 0.5*(diffusion**2))*t + diffusion*W )

	R = 2**4
	Dt = R*dt
	L = N/R 
	Xem = np.zeros(L)
	Xtemp = Xzero
	for j in range(1,L+1): 
		Winc = np.sum( dW[(R*(j-1)+1):(R*j)] )
		Xtemp = Xtemp + Dt*drift*Xtemp + diffusion*Xtemp*Winc
		Xem[j-1] = Xtemp
	Xem = np.hstack(([Xzero,Xem]))
	t2 = np.linspace(0, T, L+1)

	# produce a pretty plot of the two "solutions"
	plt.figure()
	plt.plot(t, Xtrue, 'm', label='True solution')
	plt.plot(t2, Xem, 'r', label='Euler-Maruyama')
	plt.legend(loc='upper left', shadow=False, fontsize='large')
	plt.title('Euler-Maruyama approximation to Black-Scholes',\
		fontsize='x-large')
	plt.xlabel('$t$', fontsize='large')
	plt.ylabel('$X(t)$', fontsize='large')
	plt.show()

	return None

if __name__ == '__main__':
	main()
