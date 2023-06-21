import matplotlib.pyplot as plt
import numpy as np

a=np.arange(0,2*np.pi,0.015)
r=-250*np.sin(5*a)*np.cos(4*a)
v=a+np.sin(r/100)
x= 320+r*np.cos(v)
y= -240-r*np.sin(v)

plt.plot(x,y,c='k')
plt.title('ejercicio 6')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.axis('off')
plt.show()