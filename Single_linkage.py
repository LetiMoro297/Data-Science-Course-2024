# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:38:06 2024

@author: Letiz
"""
import numpy as np
import numpy.random 
import numpy.linalg
import math
import matplotlib.pyplot as plt
from pyomo.environ import *
import time
import random

def single_linkage(Xs, k):
    random.shuffle(Xs)
    n = len(Xs)
    Classes = {}
    ListClasses = [[(i)] for i in Xs]
    
    for (ind, point) in enumerate(Xs):
        Classes[point] = ind
    dist_matrix = [[np.linalg.norm(np.array(x)-np.array(y)) for y in Xs] for x in Xs]
    dist_matrix = np.array(dist_matrix)
    M = dist_matrix.max()+1
    
    for i in range(n):
        dist_matrix[i, i] += M
    
    
    while n>k:
        (i, j) = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)
        [I, J] = sorted((i, j))
        
        point_i = tuple(Xs[I])
        point_j = tuple(Xs[J])
        I = Classes[point_i]
        J = Classes[point_j]
        if I == J:
            dist_matrix[i, j] = M
            dist_matrix[j, i] = M
        else:
            ListClasses[I] = ListClasses[I] + ListClasses[J]
            ListClasses[J] = []
            
            for point in ListClasses[I]:
                Classes[point] = I
            
            dist_matrix[i, j] = M
            dist_matrix[j, i] = M
            n -= 1
        
    clusters = []
    for Ls in ListClasses:
        if not(Ls == []):
            clusters = clusters + [Ls]
    
        
    return clusters
