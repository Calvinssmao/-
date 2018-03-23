import matplotlib.pyplot as plt
import numpy as np
from numba import jit
@jit

def run_Holographic(col, raw, r0, n):

	x = np.linspace(-col/200, col/200, col)
	y = np.linspace(-raw/200, raw/200, raw)
	[xv,yv]=np.meshgrid(x,y)
	r = np.zeros((raw,col))
	theta = np.zeros((raw,col))
	Tn = np.zeros((raw,col))

	for i in range(0,raw):
		for j in range(0,col):
			r[i][j] = np.sqrt(xv[i][j]**2+yv[i][j]**2)
			theta[i][j] = np.arctan2(yv[i][j],xv[i][j])
			if yv[i][j]<0:
				theta[i][j] +=2*np.pi

	for i in range(0,raw):
		for j in range(0,col):
			Tn[i][j] = n*theta[i][j]-2*np.pi*r[i][j]/r0
			while Tn[i][j]<0:
				Tn[i][j] += 2*np.pi
			while Tn[i][j]>2*np.pi:
				Tn[i][j] -= 2*np.pi

	# np.savetxt("r.dat", r, fmt='%.18e', delimiter=' ', newline='\n')
	# np.savetxt("theta.dat", theta, fmt='%.18e', delimiter=' ', newline='\n')
	# np.savetxt("Tn.dat", Tn, fmt='%.18e', delimiter=' ', newline='\n')

	plt.axis("equal")
	plt.imshow(Tn, cmap=plt.cm.gray) #灰度
	plt.colorbar() 
	plt.savefig("test.png")
	plt.show()

run_Holographic(col=4000,raw=4000, r0=5, n=2)