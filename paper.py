# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 09:41:16 2021

@author: a.h
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:23:12 2020

@author: S. Ali Hosseini
"""




######################################### IMPORTS ##################################################

import numpy as np
from CSTH_model import CSTH_model
import random
from PID_controller import PID_controller
import  matplotlib.pyplot as plt
from State import State
from Reward import Reward
from Policy import Policy
from Enter_state import Enter_state
from Q_Learning_Algorithm import Q_Learning_Algorithm
from CSTR_plant import CSTR_plant


################################################# PARAMETERS ##################################

# actions=list(range(-3,4)) 
# state=list(range(0,11))
# y_out = np.zeros(300)
# m = np.zeros(2000)
# error_mse= np.zeros(300)
# loop_circle=0
# error = 0
# fault = 1#random.randint(-5,5)
# a=0
# yy =0
# mean_duble=np.zeros(100)
# ii =0
# cc= 0
# ################################################### MAIN LOOP #######################################

# for k in range(200):
#     while loop_circle < 300:
#         if loop_circle == 0:
#             y_out[loop_circle] = CSTH_model(8)
#             error_mse[loop_circle] = (125 - y_out[loop_circle])**2

#         else:
#             if loop_circle <= 10:
#                 control_action = PID_controller(CSTH_model,y_out[loop_circle])
#                 y_out[loop_circle] = CSTH_model(control_action)
#                 error_mse[loop_circle] = (125 - y_out[loop_circle])**2
                
#             if loop_circle > 10 and a==0:
#                 if abs(error)<= 0.2 and a==0 : 
#                     control_action = PID_controller(CSTR_plant,y_out[loop_circle])
#                     y_out[loop_circle] = CSTR_plant(control_action)+fault
#                     error_mse[loop_circle] = (125 - y_out[loop_circle])**2
                 

#                 else:
                    
#                     print('ya abolfazlllllleeeeee')
#                     state = Enter_state(error)      
#                     print('state',state)  
#                     (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Q_Learning_Algorithm (fault,state,State,Reward,Policy,CSTH_model,loop_circle,y_out,error_mse)
#                     # a=1
#                     # (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Duble_Q_Learning(fault,state,State,Reward,Policy,CSTR_plant,loop_circle,y_out,error_mse)
#                     print(y_out)
#                     print('looooooppppp',loop_circle)
#                     a=1
               
               
 
#             if loop_circle > 10 and a==1:
#                 y_out[loop_circle] = CSTH_model(A) + fault
#                 error_mse[loop_circle] = (125 - y_out[loop_circle])**2

#         error =   125 - y_out[loop_circle]
#         loop_circle += 1
   
#         print(loop_circle)
#         #print(loop_circle)


############################### new ################################

y_out = np.zeros(300)
m = np.zeros(2000)
error_mse= np.zeros(300)
loop_circle=0
error = 0
fault = 4 #random.randint(-5,5)
fault_actuator = 0.1
a=0
yy =0
mean_duble=np.zeros(200)
ii =0
loop_circle = 0
actions11=list(range(-6,6)) 
state11=list(range(0,16))
Q = np.zeros((np.size(state11),np.size(actions11)))
# Q=np.random.rand(np.size(state11),np.size(actions11))
initial_inpute = 1
set_point = 15
loop_Q_Learning = 0
system_performance = np.zeros(300)

# CSTH_model = CSTR_plant

while loop_circle < 100:
    if loop_circle == 0:
            y_out[loop_circle] = CSTH_model(initial_inpute+fault_actuator)+fault
            error_mse[loop_circle] = np.sqrt((set_point - y_out[loop_circle])**2)
            error =   set_point - y_out[loop_circle]
            state = Enter_state(error)
    else:

        
        alpha=1#float(input('Enter alpha:   '))
        gama=1# float(input('Enter gama:   '))
        epsilon = 0
        # Q=np.random.rand(np.size(state11),np.size(actions11))
        # Q[0,:]=0
        # Q = np.zeros((np.size(state11),np.size(actions11)))
        A = Policy(Q,state,epsilon)
        S_perim,a = State(A,initial_inpute,fault,CSTH_model,fault_actuator)
        R = Reward(S_perim)
        Q[state,A+5] = Q[state,A+5] + alpha * (R + gama * max(Q[S_perim,:])-Q[state,A+5])
        state = S_perim
        y_out[loop_circle] = a
        error_mse[loop_circle] = np.sqrt((set_point - y_out[loop_circle])**2)
        # system_performance[loop_circle] = CSTH_model(initial_inpute)+fault

        # (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Q_Learning_Algorithm (fault,state,State,Reward,Policy,CSTH_model,loop_circle,y_out,error_mse)
        
    loop_circle += 1
    fault += 0.01


###################################### PID controller ############


y_out_pid = np.zeros(300)
error_mse_pid= np.zeros(300)
loop_circle=0
error = 0
a=0
yy =0
ii =0
initial_inpute = 1
set_point = 15
fault = 4
while loop_circle <100:
    
                control_action = PID_controller(CSTH_model,y_out_pid[loop_circle])+ fault_actuator
                y_out_pid[loop_circle] = CSTH_model(control_action) + fault
                error_mse_pid[loop_circle] = np.sqrt((15 - y_out_pid[loop_circle])**2)
                fault += 0.01
                loop_circle += 1
                

                


print(sum(abs(error_mse)))
print(sum(abs(error_mse_pid)))








       
