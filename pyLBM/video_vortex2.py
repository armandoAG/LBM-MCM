from vortex_2 import *
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pylbm

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

#for i in my_range(0, .5, .1):
 #   sol.one_time_step()

#prueba agregar elipse
"""def __init__(self, parent):
    self.ax = parent
def ellipse(self, pos, radius, color, angle=0.):
        return self.ax.add_patch(Ellipse(xy = pos, width = 2*radius[0], height = 2*radius[1], angle=angle*180/np.pi, fill=True, color=color))"""


ims = []

fig = plt.figure()
#ax.ellipse([.3/dx, .5*(ymin+ymax)/dx], [rayon/dx, rayon/dx], 'r')

#para comprobar que entre el while y los for hay la misma cantidad de while iterados
while1 = []
count1_1 = 0

count1 = 0 #iteraciones del while
count2 = 0 #iteraciones del for
for i in my_range(0, 300, 1):
    print 'sol.t = %f' %sol.t, 'i = %f' %i
    #for j in my_range(0, 0.1, 0.1):
    while sol.t < i:
        count1 += 1
        sol.one_time_step()
        print 'iteration --> %d'%i, '| sol.t = %f'%sol.t
        count1_1 += 1
        if sol.t >= i:
            while1.append([count1_1])
            count1_1 = 0
    im = plt.imshow(vorticity(sol).transpose(), cmap = 'cubehelix')
    ims.append([im])
    plt.title('Von Karman vortex street at t = %d' %(sol.t))
    count2 += 1
    #plt.title('Von Karman vortex street at %d' %(sol.t))

'''while sol.t < Tf:
    sol.one_time_step()
im = plt.imshow(vorticity(sol).transpose(), cmap = 'cubehelix')
ims.append([im])
plt.title('Von Karman vortex street at t = %d' %(sol.t))
'''


#print count1
#print count2
#print while1
print sol._F[0]
print sol._Fold[0]
"""viewer = pylbm.viewer.matplotlibViewer
fig = viewer.Fig()
ax = fig[0]
#im = ax.image(vorticity(sol).transpose(), cmap='cubehelix',  clim = [-3., 0])
ax.ellipse([.3/dx, .5*(ymin+ymax)/dx], [rayon/dx, rayon/dx], 'r')
ax.title = 'Von Karman vortex street at t = {0:f}'.format(sol.t)
plt.pause(.9)
def update(iframe):
    for i in range(50):
        sol.one_time_step()
    im.set_data(vorticity(sol).transpose())
    ax.title = 'Von Karman vortex street at t = {0:f}'.format(sol.t)
"""
# run the simulation
#fig.animate(update)
#fig.show()

ani = animation.ArtistAnimation(fig, ims, interval=1, repeat=False)

plt.show()
