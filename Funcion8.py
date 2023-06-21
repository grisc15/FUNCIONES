import matplotlib.pyplot as plt
import numpy as np

t= np.linspace(0,2*np.pi,100)
def x(t):
    return ((1+np.sin(t))*(np.cos(t)))
plt.plot(t,x(t),'^:c', ms=10)
plt.title('$x(t)=$(1+sin(t))*cos(t)\n$y(t)=(1+2sin(t))*(sin(t))$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(t):
    return (1+(2*np.sin(t))*(np.sin(t)))
plt.plot(t,y(t),'*:m', ms =10)
plt.legend(['$x(t)$','$y(t)$'])
plt.grid(True)
plt.show()