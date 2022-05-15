import numpy as np
import matplotlib.pyplot as plt
x = []
x = np.random.random_integers(1,15,size=(5))
y = np.random.random_integers(1,15,size=(5))
print (x)

print (y)
plt.scatter(x,y)
plt.show()