import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,4*np.pi,200)
def f4(x):
    return (x*np.exp(-3*x))
plt.plot(x,f4(x),'*:c',ms=10)
plt.title('$f(x)=xe^{-3x}$\n$g(x)=1-3xe^{-3x}$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def g(x):
    return (1-(3*x*np.exp(-3*x)))
plt.plot(x,g(x),'*:m', ms=10)
plt.legend(['f(x)','g(x)'])
plt.grid(True)
plt.show()