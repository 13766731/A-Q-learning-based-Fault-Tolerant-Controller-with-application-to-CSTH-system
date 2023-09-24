# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 08:48:43 2021

@author: a.h
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 00:31:51 2020

@author: a.h
"""



def CSTH_model(u) :
    import numpy as np
    from scipy import signal
    import matplotlib.pyplot as plt
    from scipy.integrate import odeint
    Kp = 16.66666
    tau = 1.05409255
    zeta = 2.608879069
    theta = 0
    def model3(x,t):
        y = x[0]
        dydt = x[1]
        dy2dt2 = (-2.0*zeta*tau*dydt - y + Kp*u)/tau**2
        return [dydt,dy2dt2]
    t3 = np.linspace(0,50,100)
    x3 = odeint(model3,[0,0],t3)
    y3 = x3[:,0]
    return  (y3[99])
    
import numpy as np
step = np.zeros((300)) 
step[20:300] = 1
from scipy import signal
aa = CSTH_model(1+1)



   
 
# y_out_CSTH= np.zeros(300)  
# loop_circle =0 
# fault = 5
 
# while loop_circle <100:
    
#                 y_out_CSTH[loop_circle] = CSTH_model(1) + fault
#                 # error_mse_pid[loop_circle] = np.sqrt((15 - y_out_pid[loop_circle])**2)
#                 fault += 0.01
#                 loop_circle += 1
                
    
    
    
    
    
    
    