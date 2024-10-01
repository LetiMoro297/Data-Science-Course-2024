# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:16:42 2024

@author: Letiz
"""
import numpy as np
import numpy.random 
import math
import matplotlib.pyplot as plt
from pyomo.environ import *
import time
import random
from single_linkage import *


n=15

Nx = 2*n
centro_X = [0, -1]
VarX = 0.4
Xs = numpy.random.normal(centro_X, [VarX*2, VarX], size = (Nx, 2))

Ny = 2*n
centro_Y = [2, 2]
VarY = 0.4
Ys = numpy.random.normal(centro_Y, [VarY, VarY], size = (Ny, 2))

Ys = np.array(Ys)

Nz = 2*n
centro_Z = [-2, 4]
VarZ = 0.4
Zs = numpy.random.normal(centro_Z, [VarZ, VarZ*2], size = (Nz, 2))

Zs = np.array(Zs)

# =============================================================================
# =============================================================================
plt.scatter(Xs[:,0], Xs[:,1], color = 'blue')
plt.scatter(Ys[:,0], Ys[:,1], color = 'blue')
plt.scatter(Zs[:,0], Zs[:,1], color = 'blue')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# =============================================================================
# =============================================================================

k = 3

Ls = [tuple(i) for i in Xs.tolist()] + [tuple(i) for i in Ys.tolist()] + [tuple(i) for i in Zs.tolist()]
Clusters = single_linkage(Ls, k)

plt.figure()
Colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']
for j in range(k):
    for i in Clusters[j]:
        plt.scatter(i[0], i[1], c = Colors[2*j+2])

    
plt.xlabel('x')
plt.ylabel('y')
plt.show()
