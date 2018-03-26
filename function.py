import numpy as np
from numba import jit
@jit

def fun1(raw, col, theta, Tn, n):
	# n阶的相位板
	for i in range(0,raw):
		for j in range(0,col):
			Tn[i][j] = n*theta[i][j]
			while Tn[i][j]<0:
				Tn[i][j] += 2*np.pi
			while Tn[i][j]>2*np.pi:
				Tn[i][j] -= 2*np.pi
	return Tn

def fun2(raw, col, theta, r, Tn, k, f):
	# 薄透镜
	for i in range(0,raw):
		for j in range(0,col):
			Tn[i][j] = k*(r[i][j]**2)/2/f
			while Tn[i][j]<0:
				Tn[i][j] += 2*np.pi
			while Tn[i][j]>2*np.pi:
				Tn[i][j] -= 2*np.pi
	return Tn

def fun3(raw, col, theta, r, Tn, n, k, f):
	# 薄透镜+n阶的相位板
	for i in range(0,raw):
		for j in range(0,col):
			Tn[i][j] = n*theta[i][j] + k*(r[i][j]**2)/2/f
			while Tn[i][j]<0:
				Tn[i][j] += 2*np.pi
			while Tn[i][j]>2*np.pi:
				Tn[i][j] -= 2*np.pi
	return Tn

def fun4(raw, col, theta, r, Tn, n, r0):
	# n阶的相位板+贝塞尔
	for i in range(0,raw):
		for j in range(0,col):
			Tn[i][j] = n*theta[i][j] - 2*np.pi*r[i][j]/r0
			while Tn[i][j]<0:
				Tn[i][j] += 2*np.pi
			while Tn[i][j]>2*np.pi:
				Tn[i][j] -= 2*np.pi
	return Tn