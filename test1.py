import matplotlib.pyplot as plt
import numpy as np

gap=4000

x = np.linspace(-20, 20, gap)
y = np.linspace(-20, 20, gap)
[xv,yv]=np.meshgrid(x,y)
r = np.zeros((gap,gap))
theta = np.zeros((gap,gap))

for i in range(0,gap):
	for j in range(0,gap):
		r[i][j] = np.sqrt(xv[i][j]**2+yv[i][j]**2)
		theta[i][j] = np.arctan2(yv[i][j],xv[i][j])
		if yv[i][j]<0:
			theta[i][j] +=2*np.pi

np.savetxt("r.dat", r, fmt='%.18e', delimiter=' ', newline='\n')
np.savetxt("theta.dat", theta, fmt='%.18e', delimiter=' ', newline='\n')
