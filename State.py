"""
Created on Mon Sep 28 11:21:50 2020

@author: a.h
"""
def State(inpute,initial_inpute,fault,model,fault_actuator):
    inpute = inpute/10
    inpute = inpute + initial_inpute
    a = model(inpute+fault_actuator) + fault
    error = abs((15-a))
    if (error < -20) or (error > 20):
        state_now = 15
    if (error >= -20) and (error <= 20):
        state_now = 14
    if (error >= -19) and (error <= 19):
        state_now = 13
    if (error >= -18) and (error <= 18):
        state_now = 12
    if (error >= -17) and (error <= 17):
        state_now = 11
    if (error >= -16) and (error <= 16):
        state_now = 10
    if (error >= -15) and (error <= 15):
        state_now = 9
    if (error >= -13) and (error <= 13):
        state_now = 8
    if (error >= -10) and (error <= 10):
        state_now = 7
    if (error >= -5) and (error <= 5):
        state_now = 6
    if (error >= -3) and (error <= 3):
        state_now = 5
    if (error >= -2) and (error <= 2):
        state_now = 4
    if (error >= -1) and (error <= 1):
        state_now = 3
    if (error >= -0.5) and (error <= 0.5):
        state_now = 2
    if (error >= -0.3) and (error <= 0.3):
        state_now = 1
    if error == 0:
        state_now = 0
    return state_now,a

# def State(inpute,initial_inpute,fault,model,fault_actuator):
   
#     inpute = inpute/15
#     inpute = inpute + initial_inpute
#     a = model(inpute+fault_actuator) + fault
#     error = (12-a)
#     if (error < -5) or (error > 5):
#         state_now = 10
#     if (error >= -5) and (error <= 5):
#         state_now = 9
#     if (error >= -4) and (error <= 4):
#         state_now = 8
#     if (error >= -3) and (error <= 3):
#         state_now = 7
#     if (error >= -2) and (error <= 2):
#         state_now = 6
#     if (error >= -1) and (error <= 1):
#         state_now = 5
#     if (error >= -0.08) and (error <= 0.08):
#         state_now = 4
#     if (error >= -0.04) and (error <= 0.04):
#         state_now = 3
#     if (error >= -0.02) and (error <= 0.02):
#         state_now = 2
#     if (error >= -0.01) and (error <= 0.01):
#         state_now = 1
#     if error == 0:
#         state_now = 0
#     return state_now


























