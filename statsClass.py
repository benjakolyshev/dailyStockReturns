#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:13:19 2019

@author: satan
"""

import math

def expectation(arr):

    exp = (sum(arr)/len(arr))
    return exp

def variance(arr):
    exp = expectation(arr)
    var = (sum((xi - exp)**2 for xi in arr))/len(arr)
    vol = math.sqrt(var)
    return var

# This splits our array's arrays
def stringSplitter(arr):
    i = 1
    tempArr = []
    while (i < len(arr)):
        #print(arr)
        # We create a completely temporary array to hold our values so 
        # we can split them into up into the values we really want to see
        newTemp = arr[i].split(',')
        i = i + 1
        # This gives us the difference between the open and close
        # otherwise known as the daily return        
        tempArr.append((float(newTemp[4]) - float(newTemp[1]))/float(newTemp[1]))
    
    return(tempArr)
    
def covariance(arr1, arr2):
    exp1 = expectation(arr1)
    exp2 = expectation(arr2)
    i = 0
    cov = 0
    while i < len(arr1):
        cov = ((arr1[i] - exp1)*(arr2[i] - exp2)) + cov
        i = i + 1
    cov = cov / len(arr1)
    return(cov)