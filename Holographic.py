import matplotlib.pyplot as plt
import numpy as np
import function
from numba import jit
@jit

def run_Holographic(col, raw):
	wavelength = 0.78e-6
	f = 5e-6
	k = 2 * np.pi / wavelength
	n = 2
	r0 = 1.2e-6
	inter = 1.2e-6

	x = np.linspace(-5e-6, 5e-6, col)
	y = np.linspace(-5e-6, 5e-6, raw)

	[xv,yv]=np.meshgrid(x,y)
	r = np.zeros((raw,col))
	theta = np.zeros((raw,col))
	Tn = np.zeros((raw,col))

	r = np.sqrt(xv**2+yv**2)
	for i in range(0,raw):
		for j in range(0,col):
			theta[i][j] = np.arctan2(yv[i][j],xv[i][j])
			if yv[i][j]<0:
				theta[i][j] += 2*np.pi

	# n阶的相位板
	Tn = function.fun1(raw, col, theta, Tn, n)
	# 薄透镜
	#Tn = function.fun2(raw, col, theta, r, Tn, k, f)
    # 薄透镜+n阶的相位板
	#Tn = function.fun3(raw, col, theta, r, Tn, n, k, f)
	# n阶的相位板+贝塞尔
	#Tn = function.fun4(raw, col, theta, r, Tn, n, r0)

	# np.savetxt("r.dat", r, fmt='%.18e', delimiter=' ', newline='\n')
	# np.savetxt("theta.dat", theta, fmt='%.18e', delimiter=' ', newline='\n')
	# np.savetxt("Tn.dat", Tn, fmt='%.18e', delimiter=' ', newline='\n')

	plt.axis("equal")
	plt.imshow(Tn, cmap=plt.cm.gray) #灰度
	plt.colorbar() 
	plt.savefig("test.png")
	plt.show()

run_Holographic(col=20, raw=20)