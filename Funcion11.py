import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,2*np.pi,100)
def f(t):
    return (np.sin(3*t))
plt.plot(t,f(t),'<:y', ms=10)
plt.title('$x=sin(3t)$\n$y=sin(4t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(t):
    return (np.sin(4*t))
plt.plot(t,y(t),'>:r', ms =10)
plt.legend(['$f(x)$','$f(y)$'])
plt.grid(True)
plt.show()