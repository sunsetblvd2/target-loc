import numpy as np
import pdb
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import grid

class Isotropic:

    def __init__(self,theta,n):

        self.P_0=theta[0]
        self.x_t=theta[1]
        self.y_t=theta[2]
        self.n=n

    def amplitude(self,x_i,y_i):

        def distance(x_i,y_i):

            return np.sqrt((x_i-self.x_t)**2+(y_i-self.y_t)**2)

        d=distance(x_i,y_i)

        if d < 1:

            d=1

        return self.P_0 / d**self.n

    def heatmap(self,domain_size):
        
        heatmapGrid=grid.Grid(domain_size,2)
        cells=heatmapGrid.coordinates(heatmapGrid.domain_xo)

        a=np.zeros((heatmapGrid.domain_xo.size,heatmapGrid.domain_xo.size))

        for i in range(0,heatmapGrid.domain_xo.size):

            x_range=heatmapGrid.X_xo[i]
            y_range=heatmapGrid.Y_xo[i]

            for j in range(0,heatmapGrid.domain_xo.size):

                x=x_range[j]
                y=y_range[j]
                a[i,j]=self.amplitude(x,y)

        self.fig,self.ax=plt.subplots(figsize=(7,6),constrained_layout=True,squeeze=False)
        norm=mpl.colors.LogNorm()
        cmp=mpl.colormaps['plasma']
        eMin=np.amin(heatmapGrid.domain)
        eMax=np.amax(heatmapGrid.domain)
        pos=self.ax[0,0].imshow(a,extent=[eMin,eMax,eMin,eMax],cmap=cmp,norm=norm, \
                           interpolation='bilinear',origin='lower')
        plt.colorbar(pos,label='Power')
        #plt.show()
