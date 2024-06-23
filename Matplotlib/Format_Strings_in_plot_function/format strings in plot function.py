import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,7)
y=[0,1,4,9,16,25,36]

plt.xlabel("number")
plt.ylabel("square")
plt.title("square of number")

#Arguments color, marker, markersize, linestyle, alpha
plt.plot(x,y, color='red', marker='*', markersize=5, linestyle='-',alpha=1)
plt.show()