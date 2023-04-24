import sys
import os
import pdb
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('classic')

log_name=sys.argv[1]
log_path=os.getcwd()+'\\logs\\'

log=log_path+log_name+'.txt'


mc_results_list=[]
with open(log,'r') as log_r:
    for line in log_r:
        if '%_ESTIMATE' in line:
            mc_results_list.append(line.rstrip()
                           .replace('%_ESTIMATE:: ','')
                           .replace('(','')
                           .replace(')','')
                           .replace(' ','')
                           .split(','))

point_estimates=np.zeros((len(mc_results_list),2))
for index,point in enumerate(mc_results_list):
    point_estimates[index,0]=point[0]
    point_estimates[index,1]=point[1]


fig,ax=plt.subplots()

ax.scatter(point_estimates[:,0],point_estimates[:,1],marker='x',color='k',s=25,label='Estimate')
ax.scatter(15,20,marker='*',color='r',s=100,label='Emitter')

ax.set_title('MLE Monte Carlo (N=100)')
ax.set_xlabel('x-coordinate (m)')
ax.set_ylabel('y-coordinate (m)')

ax.set_xlim(-10,45)
ax.set_ylim(-10,45)

plt.legend()
plt.tight_layout()
plt.show()
