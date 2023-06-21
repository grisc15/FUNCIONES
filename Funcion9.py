import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,100)
def f(x):
    return (np.power(np.cos(x),3))
plt.plot(x,f(x),'>:b', ms=10)
plt.title('$x=cos^{3}(t)$\n$y=sin^{3}(t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(x):
    return (np.sin(x)**3)
plt.plot(x,y(x),'<:k', ms =10)
plt.legend(['$f(x)$','$f(y)$'])
plt.grid(True)
plt.show()
