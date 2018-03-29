import numpy as np
from numba import jit
@jit

def fun1(raw, col, theta, Tn, n):
	# n阶的相位板
	Tn = n*theta
	Tn = too(raw,col,Tn)
	return Tn

def fun2(raw, col, theta, r, Tn, k, f):
	# 薄透镜
	Tn = k*(r**2)/2/f
	Tn = too(raw,col,Tn)
	return Tn

def fun3(raw, col, theta, r, Tn, n, k, f):
	# 薄透镜+n阶的相位板
	Tn = n*theta + k*(r**2)/2/f
	Tn = too(raw,col,Tn)
	return Tn

def fun4(raw, col, theta, r, Tn, n, r0):
	# n阶的相位板+贝塞尔
	Tn = n * theta - 2*np.pi*r/r0
	Tn = too(raw,col,Tn)
	return Tn

def too(raw,col,Tn):
	for i in range(0,raw):
		for j in range(0,col):
			while Tn[i][j]<0:
				Tn[i][j] += 2*np.pi
			while Tn[i][j]>2*np.pi:
				Tn[i][j] -= 2*np.pi
	return Tn