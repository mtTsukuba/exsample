# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
print(x)
y = relu(x)
print(y)


plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()
