import matplotlib.pyplot as plt
import numpy as np

gap=4000
r0=5
n=-3

Tn = np.zeros((gap,gap))
r = np.genfromtxt("r.dat",delimiter=' ',skip_header=0)
theta = np.genfromtxt("theta.dat",delimiter=' ',skip_header=0)

for i in range(0,gap):
	for j in range(0,gap):
		Tn[i][j] = n*theta[i][j]-2*np.pi*r[i][j]/r0
		while Tn[i][j]<0:
			Tn[i][j] += 2*np.pi
		while Tn[i][j]>2*np.pi:
			Tn[i][j] -= 2*np.pi

np.savetxt("Tn.dat", Tn, fmt='%.18e', delimiter=' ', newline='\n')