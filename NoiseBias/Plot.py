#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:29:05 2021

@author: emilam
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import rv_histogram as hist

Datasets1 = np.load('ApInferenceData1to4Opposite.npy')
Datasets2 = np.load('ApInferenceData5to8Opposite.npy')
Datasets3 = np.load('ApInferenceData9to12Opposite.npy')
Datasets4 = np.load('ApInferenceData13to16Opposite.npy')
Datasets5 = np.load('ApInferenceData17to20Opposite.npy')

Datasets = [Datasets1,Datasets2,Datasets3,Datasets4,Datasets5]


plt.rcParams['axes.titlesize'] = 22
maps1 = np.load("Maps0.0001.npy")
maps2 = np.load("Maps0.0005.npy")
maps3 = np.load("Maps0.001.npy")
maps4 = np.load("Maps0.003.npy")
maps5 = np.load("Maps0.005.npy")
### CALCULATED WITH R
maps = [maps1,maps2,maps3,maps4,maps5]

means = []
medians = []
varrs = []
count = 0
for i in range(5):
    for j in range(4):
        means_temp = []
        varrs_temp = []
        maps_temp =[]
        medians_temp =[]
        count += 1
        for k in range(5):
            means_temp.append(np.mean(Datasets[i][j][k][300:][0]))
            medians_temp.append(np.median(Datasets[i][j][k][300:][0]))
            varrs_temp.append(np.var(Datasets[i][j][k][300:][0]))
        medians.append(medians_temp) 
        varrs.append(varrs_temp)
        means.append(means_temp)

meansvar = np.sqrt(np.asarray(means).var(0))     
means = np.asarray(means).mean(0)

mediansvar = np.sqrt(np.asarray(medians).var(0))
medians = np.asarray(medians).mean(0)

mapsvar = np.sqrt(np.asarray(maps).var(1))
maps = np.asarray(maps).mean(1)

varrs = np.asarray(varrs).mean(0)
varrs = np.sqrt(varrs)

x = [0.0001,0.0005,0.001,0.003,0.005]
ticksss = ['0.0001','0.0005','0.001','0.003','0.005']

plt.figure()
plt.title('High generative noise')
plt.xlabel('$\sigma$')
plt.ylabel('$A_+$ estimation')
plt.ylim([0.0018,0.0075])
#plt.xlim([0,6])
plt.xticks(x,labels = ticksss)
plt.yticks([0.003,0.005,0.007],labels=['0.003','0.005','0.007'])
for i in range(5):
    if i == 1:
        plt.errorbar(x[i], means[i], yerr = meansvar[i],c=[0.4,0.3,0.9],marker = 'o',ecolor=[0.4,0.3,0.9])
        #plt.errorbar(x[i], means[i], yerr = varrs[i],marker = 'o',label='Std of samples',barsabove=(True))
    else:
        plt.errorbar(x[i], means[i], yerr = meansvar[i],c=[0.4,0.3,0.9],marker = 'o',ecolor=[0.4,0.3,0.9])#,label='Std of means')
        #plt.errorbar(x[i], means[i], yerr = varrs[i],marker = 'o')#,label='Std of samples')
plt.axhline(0.005,color='r',linestyle='--',label='True Value')
#plt.legend()
plt.xscale('log')
#plt.minorticks_off()
plt.show()
'''
plt.figure()
plt.title('Mean of MAPs - 20 datasets')
plt.xlabel('Noise')
plt.ylabel('Ap estimation')
#plt.ylim([0.004,0.007])
plt.xlim([0,6])
plt.xticks(x,labels = ticksss)
for i in range(5):
    if i == 1:
        plt.errorbar(x[i], maps[i], yerr = mapsvar[i],c=[0.4,0.3,0.9],marker = 'o',ecolor=[0.4,0.3,0.9])
    else:
        plt.errorbar(x[i], maps[i], yerr = mapsvar[i],c=[0.4,0.3,0.9],marker = 'o',ecolor=[0.4,0.3,0.9])
plt.axhline(0.005,color='r',linestyle='--',label='True Value')
plt.legend()
plt.show()

plt.figure()
plt.title('Mean of posterior medians - 20 datasets')
plt.xlabel('Noise')
plt.ylabel('Ap estimation')
#plt.ylim([0.004,0.007])
plt.xlim([0,6])
plt.xticks(x,labels = ticksss)
for i in range(5):
    if i == 1:
        plt.errorbar(x[i], medians[i], yerr = mediansvar[i],c=[0.4,0.3,0.9],marker = 'o',ecolor=[0.4,0.3,0.9])
    else:
        plt.errorbar(x[i], medians[i],c=[0.4,0.3,0.9], yerr = mediansvar[i],marker = 'o',ecolor=[0.4,0.3,0.9])
plt.axhline(0.005,color='r',linestyle='--',label='True Value')
plt.legend()
plt.show()

'''
Datasets1 = np.load('ApInferenceData1to4.npy')
Datasets2 = np.load('ApInferenceData5to8.npy')
Datasets3 = np.load('ApInferenceData9to12.npy')
Datasets4 = np.load('ApInferenceData13to16.npy')
Datasets5 = np.load('ApInferenceData17to20.npy')

Datasets = [Datasets1,Datasets2,Datasets3,Datasets4,Datasets5]


means = []
medians = []
varrs = []
count = 0
for i in range(5):
    for j in range(4):
        means_temp = []
        varrs_temp = []
        maps_temp =[]
        medians_temp =[]
        count += 1
        for k in range(5):
            means_temp.append(np.mean(Datasets[i][j][k][300:]))
            medians_temp.append(np.median(Datasets[i][j][k][300:]))
            varrs_temp.append(np.var(Datasets[i][j][k][300:]))
        medians.append(medians_temp) 
        varrs.append(varrs_temp)
        means.append(means_temp)

meansvar2 = np.sqrt(np.asarray(means).var(0))     
means = np.asarray(means).mean(0)

varrs = np.asarray(varrs).mean(0)
varrs = np.sqrt(varrs)

x = [0.0001,0.0005,0.001,0.003,0.005]
ticksss = ['0.0001','0.0005','0.001','0.003','0.005']

plt.figure()
plt.title('Low generative noise')
plt.xlabel('$\sigma$')
plt.ylabel('$A_+$ estimation')
plt.ylim([0.0018,0.0075])
#plt.xlim([0,6])
plt.xticks(x,labels = ticksss)
plt.yticks([0.003,0.005,0.007],labels=['0.003','0.005','0.007'])
for i in range(5):
    if i == 1:
        plt.errorbar(x[i], means[i], yerr = meansvar2[i],c=[0.4,0.3,0.9],marker = 'o',ecolor=[0.4,0.3,0.9])
        #plt.errorbar(x[i], means[i], yerr = varrs[i],marker = 'o',label='Std of samples',barsabove=(True))
    else:
        plt.errorbar(x[i], means[i], yerr = meansvar2[i],c=[0.4,0.3,0.9],marker = 'o',ecolor=[0.4,0.3,0.9])#,label='Std of means')
        #plt.errorbar(x[i], means[i], yerr = varrs[i],marker = 'o')#,label='Std of samples')
plt.axhline(0.005,color='r',linestyle='--',label='True Value')
#plt.legend()
plt.xscale('log')
#plt.minorticks_off()
plt.show()