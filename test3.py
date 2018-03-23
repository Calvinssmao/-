import matplotlib.pyplot as plt
import numpy as np

Tn = np.genfromtxt("Tn.dat",delimiter=' ',skip_header=0)

plt.axis("equal")
plt.imshow(Tn, cmap=plt.cm.gray) #灰度
plt.colorbar() 
plt.savefig("test.png")
plt.show()