
import numpy as np

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