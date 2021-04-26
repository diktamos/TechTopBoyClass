import matplotlib.pyplot as plt
import numpy as np

#plt.close(1)

x=np.linspace(-4,4,25)
y=np.square(x)
z=np.square(y)
plt.axis([0,5,0,16])
plt.plot(x,y,'b-^',linewidth=3, markersize=7,label='Y')
plt.plot(x,z,'r--o',linewidth=3, markersize=7,label='Z')
plt.xlabel('My X Values')
plt.ylabel('My Y Values')
plt.legend(loc='lower center')
plt.title('My First Graph')
plt.grid(True)
plt.show()
#plt.close('all')