# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 00:16:49 2020

@author: a.h
"""

def Enter_state (error):
    if (error < -20) or (error > 20):
        state_now = 10
    if (error >= -20) and (error <= 20):
        state_now = 9
    if (error >= -15) and (error <= 15):
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
    return state_now