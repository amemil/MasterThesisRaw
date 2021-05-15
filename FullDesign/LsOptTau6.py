#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 20:02:02 2021

@author: emilam
"""
import sys, os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import UtilitiesMaster as ut

s1init = np.load('s1init_6.npy')
s2init = np.load('s2init_6.npy')
Winit = np.load('Winit_6.npy')

design = ut.ExperimentDesign(freqs_init=np.array([20,50,100,200]),maxtime=60,trialsize=5\
                 ,Ap=0.005, tau=0.02, genstd=0.0001,b1=-3.1, b2=-3.1, w0=1.0,binsize = 1/500.0,reals = 15,longinit = 60\
                     ,s1init = s1init,s2init = s2init,Winit = Winit)
means,entrs,optms,mutinfs,W,posts = design.onlineDesign_wh_tau(nofreq =False,constant = False, random = False, optimised = True)

np.save('WHestmimatesTau_6',means)
np.save('WHentropiesTau_6',entrs)
np.save('WHoptfrqsTau_6',optms)
np.save('WHmutinfsTau_6',mutinfs)
np.save('WHwTau_6',W)
np.save('WHpostsTau_6',posts)