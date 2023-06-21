import math
import matplotlib.pyplot as plt
import numpy as np
def circle(radio,a,b):
    theta = np.linspace(0,2*np.pi,100)
    r = np.sqrt(radio)
    x1 = r*np.cos(theta)+a
    x2 = r*np.sin(theta)+b
    return(x1,x2)
def elipsis():
    u=0.     #x-position of the center
    v=-2    #y-position of the center
    a=2.     #radius on the x-axis
    b=1    #radius on the y-axis
    t = np.linspace(0, 2*np.pi, 100)
    plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
    plt.grid(color='k',linestyle='--')
    plt.fill(u+a*np.cos(t) , v+b*np.sin(t),'k')
    plt.show()
x,y = circle(15,0,0)
x1,y1 = circle(1,1.25,1)
x2,y2 = circle(1,-1.25,1)
plt.plot(x,y)
plt.plot(x1,y1)
plt.plot(x2,y2)
elipsis()
plt.show()