import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)

plt.plot(x, y, label="sin Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Matplotlib Plot")
plt.legend()
plt.show()