import numpy as np
import math
import pandas as pd
from matplotlib import pyplot
%matplotlib inline


def rocketH (v,h,T, dt):
    ms = 50.0
    g = 9.81
    rho = 1.091
    r = 0.5
    A = math.pi*r**2
    ve = 325
    cd = 0.15
    mp0  = 100
    
    
    if T < 5 :
        mpf = 20
    else:
        mpf = 0
        
        
    if T<=5:
        mp = 100-T*20 
    else:
        mp = 0
    
    new_h = h+dt*v
    new_v =  v + dt*((-(ms + mp)*g + mpf*ve - 0.5*rho*v*abs(v)*A*cd)/(ms+mp))
    
    T = T+0.1

    return new_v, new_h,T
    

dt  = 0.1
f = np.array([[0,0,0]])
N = 0
T  = 0
value = (f[N][1])
while f[N][1]>=0:
    
    u = rocketH(f[N][0],f[N][1],T,dt)
    
    N +=1
    T=dt*N
    a = np.asarray([u])
    
    f=np.append(f,a,axis = 0)
    
    
Output = pd.DataFrame({'T':f[:,2],'V':f[:,0],'H':f[:,1]})

print(Output.to_string())