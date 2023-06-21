import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,-24,250)
def h(t):
    return (np.sin(2*t)*np.exp(-0.1*t))
plt.plot(t,h(t),'o:r', ms = 10)
plt.title('$h(t)=sin(2t)*e^{-0.1t}$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.show()
