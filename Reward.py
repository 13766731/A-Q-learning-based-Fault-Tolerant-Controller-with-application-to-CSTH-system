# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:26:54 2020

@author: a.h
"""

def Reward(state_now):
    if state_now <= 4:
        R=1
    if state_now >4:
        R=-1
    if (state_now >5):  #or  (state_now < -4):
        print('We are in Danger area')
        R=-100
    return R


# def Reward(state_now):
#     if state_now <= 8:
#         R=-6
#     if state_now <= 7:
#         R=-5
#     if state_now <= 6:
#         R=-4
#     if state_now <= 5:
#         R=-3
#     if state_now <= 4:
#         R=-2
#     if state_now <= 3:
#         R=-1
#     if state_now <= 2:
#         R= 10
#     if state_now <= 1:
#         R=100
#     if (state_now >= 9):  #or  (state_now < -4):
#         print('We are in Danger area')
#         R=-100
#     return R

