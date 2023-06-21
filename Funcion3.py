import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1, 5 ,300)
def h(t):
    return (t*np.exp(-2*t)) 
plt.plot(t, h(t), 'o:k', markersize=10)
plt.title('$F(t)=t*exp^-2t$')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
a = plt.gca()
#a.set_axis_bgcolor('k')
plt.grid(True)
plt.show()