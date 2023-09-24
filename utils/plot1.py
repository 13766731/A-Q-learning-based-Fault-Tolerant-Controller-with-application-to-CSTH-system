# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:31:33 2021

@author: a.h
"""

from numpy import loadtxt
import  matplotlib.pyplot as plt
import numpy as np


t=np.linspace(0,100,100)  


plt.figure(1)
plt.plot(t,scanrio_5_actuator_sensor_pid)
plt.plot(t,optima)
plt.plot(t,scanrio_5_actuator_sensor_rl,'*')
# plt.plot(t,scanrio_5_sensor_CSTH)
plt.xlabel('time')
plt.ylabel('Temperature (T)')
plt.legend(['Closed-loop with PID-controller','optimal output','Closed-loop with Q-Learning controller'])
plt.show()


# plt.figure(2)
# plt.plot(t,pid_alon)
# plt.plot(t,optimal_output,'.')
# plt.plot(t,pid_Q1,'--')
# plt.xlabel('time')
# plt.ylabel('Concentrations A (CA)')
# plt.legend(['Closed-loop with PID-Controller','optimal output','Closed-loop with CQLC'])
# plt.show()


# plt.figure(3)
# plt.plot(t,pid_Q2)
# plt.plot(t,pid_Q1,'--')
# plt.xlabel('time')
# plt.ylabel('Concentrations A (CA)')
# plt.legend(['Closed-loop with DQLC','Closed-loop with CQLC'])
# plt.show()




