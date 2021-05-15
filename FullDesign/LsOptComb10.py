#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 17:48:34 2021

@author: emilam
"""
import sys, os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import UtilitiesMaster as ut

s1init = np.load('s1init_10.npy')
s2init = np.load('s2init_10.npy')
Winit = np.load('Winit_10.npy')

design = ut.ExperimentDesign(freqs_init=np.array([20,50,100,200]),maxtime=60,trialsize=5\
                 ,Ap=0.005, tau=0.02, genstd=0.0001,b1=-3.1, b2=-3.1, w0=1.0,binsize = 1/500.0,reals = 15,longinit = 60\
                     ,s1init = s1init,s2init = s2init,Winit = Winit)
means,entrs,optms,mutinfs,W,posts = design.onlineDesign_wh_comb(nofreq =False,constant = False, random = False, optimised = True)

np.save('WHestmimatesComb_10',means)
np.save('WHentropiesComb_10',entrs)
np.save('WHoptfrqsComb_10',optms)
np.save('WHmutinfsComb_10',mutinfs)
np.save('WHwComb_10',W)
np.save('WHpostsComb_10',posts)