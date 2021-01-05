#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 21:16:26 2021

@author: emilam
"""
import numpy as np              
import matplotlib.pyplot as plt 
from tqdm import tqdm
from scipy.stats import gamma
from numba import njit
@njit

#print('Datasize')

#Affect of the datasize (longer time scale), 2 noise levels -> check for bigger time domains
#Decorrelation of A and Tau with bigger datasets (not learning rule shape if more data)

