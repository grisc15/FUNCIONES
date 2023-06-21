import matplotlib.pyplot as plt
import numpy as np

t= np.linspace(0,4*np.pi,100)
def f5(t):
    return (np.sin(3*t)*(np.cos(2*t)))
plt.plot(t,f5(t),'*:c', ms=10)
plt.title('$f(t)=sin(3t)*cos(2t)$\n$g(t)=(1/2)*cos(t))+(5/2)(cos(5t))$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def g2(t):
    return (0.5*np.cos(t)+(5/2)*np.cos(5*t))
plt.plot(t,g2(t),'o:m', ms =10)
plt.legend(['$f(t)$','$g(t)$'])
plt.grid(True)
plt.show()