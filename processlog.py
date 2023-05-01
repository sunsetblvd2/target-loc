import sys
import os
import pdb
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('classic')

process_list_file=os.getcwd()+'\\queue\\'+sys.argv[1]

to_process=[]
with open(process_list_file,'r') as file_r:
    for line in file_r:
        to_process.append(line.rstrip())

for log_name in to_process:

    log_path=os.getcwd()+'\\logs\\'
    log=log_path+log_name+'.txt'

    mc_results_list=[]
    with open(log,'r') as log_r:
        for line in log_r:
            if '*** Emitter_set' in line:
                temp=line.split(':')
                temp=temp[1].replace('[','')
                temp=temp.replace(']','')
                temp=temp.split(',')
    
                theta=[]
                for i in range(0,len(temp)-1):
    
                    theta.append(float(temp[i]))
    
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
    
    x_t=theta[1]
    y_t=theta[2]
    
    mse_x_sum=0
    mse_y_sum=0
    
    for i in range(0,point_estimates.shape[0]):
    
        mse_x_sum+= ( abs ( point_estimates[i,0] - x_t ) ) ** 2
        mse_y_sum+= ( abs ( point_estimates[i,1] - y_t ) ) ** 2
    
    rmse_x = np.sqrt( ( 1 / point_estimates.shape[0]) * mse_x_sum )
    rmse_y = np.sqrt( ( 1 / point_estimates.shape[0]) * mse_y_sum )
    
    with open(log,'a+') as log_w:
        log_w.write('\n'+'%_RMSE_X:: '+str(rmse_x))
        log_w.write('\n'+'%_RMSE_Y:: '+str(rmse_y))


def plot():

    fig,ax=plt.subplots()
    
    ax.scatter(point_estimates[:,0],point_estimates[:,1],marker='x',color='k',s=25,label='Estimate')
    
    ax.set_title('MLE Monte Carlo (N=100)')
    ax.set_xlabel('x-coordinate (m)')
    ax.set_ylabel('y-coordinate (m)')
    
    plt.legend()
    plt.tight_layout()
    plt.show()

