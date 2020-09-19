#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:50:57 2020

@author: Marina Rosell i Pau Lozano
"""
#%%

import sklearn
import numpy as np
from sklearn.datasets import make_swiss_roll #carrega bd per poder ser tractades per svm
X,t = sklearn.datasets.make_swiss_roll(1000)

#%%

y=np.empty(1000)
for i in range(1000):
    if t[i]>=sum(t)/1000:
        y[i]=1
    else:
        y[i]=-1

#%%

A = np.concatenate((X,y.reshape(1000,1)), axis=1)
print(A[0:20,:])

#%%
np.savetxt('swiss_roll.dat',A,fmt='%10.5f')

#%% Visualització de la funció Swiss-Roll
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[:,0], X[:,1], X[:,2], c=y)
plt.tight_layout()
#%%%
print(X[1])
