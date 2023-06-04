import sys
import os
import numpy as np
import pdb

intensity=np.arange(0,520,20)
intensity[0]=1

queue_file=sys.argv[1].replace('.txt','')

## monte carlo trials
## emitter intensity
## x_t, emitter x-coordinate
## y_t, emitter y-coordinate
## n, attenuation
## domain size
## network size
## samples per period
## algo.
## visual

for P_0 in intensity:

    os.system('python mc_driver.py '+queue_file+'_mle'+' 1 '+str(P_0)+' 0 0 2 60 6 1 mle 0')
    os.system('python mc_driver.py '+queue_file+'_snap'+' 1 '+str(P_0)+' 0 0 2 60 6 1 snap 0')

