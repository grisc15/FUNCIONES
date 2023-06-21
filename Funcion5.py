import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,4*np.pi,200)
def s(x):
    return (np.cos(2*x)+np.sin(3*x))
plt.plot(x,s(x),'o:b', ms = 10)
plt.title('$s(x)=cos(2x)+sin(2x)$\n$v(x)=-2sin(2x)+3cos(3x)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def v(x):
    return (-2*np.sin(2*x)+3*np.cos(3*x))
plt.plot(x,v(x),'o:r', ms = 10)
plt.legend(['$s(x)$','$v(x)$'])
plt.show()