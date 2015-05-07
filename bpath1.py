import numpy as np 
import matplotlib.pyplot as plt

def bm():
    """Brownian path simulation"""
    np.random.seed(100)    # set the seed of the random number generator
    stopping_time = 1.
    N = 10
    dt = stopping_time/N 

    dW = np.sqrt(dt)*np.random.normal(size=N)
    W = np.cumsum(dW)
    W = np.hstack(([0],W))
    
    T = np.linspace(0,stopping_time,N+1)
    
    return T,W

def main():
    T,W = bm()
    
    plt.figure()
    plt.plot(T,W)
    plt.show()

if __name__ == '__main__':
	main()
