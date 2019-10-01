"""
CS 620
HW2-a
@author: Gavindya Jayawardena (UIN-01130618)
"""
import pandas as pd
import numpy as np
from collections import deque

"""Given two list of numbers that are already sorted, 
 return a single merged list in sorted order.
"""
def merge(sortedListA, sortedListB):
    # Using numpy to concatanate two lists
    arr = np.concatenate((sortedListA, sortedListB))
    # Sort the concatenated array using merge sort
    arr.sort(kind='mergesort')
    return arr


"""Given a list of numbers in random order, return the summary statistics 
that includes the max, min, mean, population standard deviation, median,
75 percentile, and 25 percentile.
"""
def summaryStatistics(listOfNums):

    # create a numpy array
    arr = np.array(listOfNums)

    maxVal = np.max(arr)
    minVal = np.min(arr)
    meanVal = np.mean(arr)
    stdev = np.std(arr)
    median = np.median(arr)
    perc75 = np.quantile(arr, 0.75)
    perc25 = np.quantile(arr, 0.25)

    return {'max': maxVal,
            'min': minVal,
            'mean': meanVal,
            'stdev': stdev,
            'median': median,
            'perc75': perc75,
            'perc25': perc25}


"""Given a list of real numbers in any range, scale them to be 
between 0 and 1 (inclusive). For each number x in the list, the new number 
is computed with the formula ((x - min)/(max - min)) where max is the 
maximum value of the original list and min is the minimum value of the list. 
"""

def scaleToDigits(listOfNums):

    # create a numpy array
    arr = np.array(listOfNums)

    max = np.max(arr)
    min = np.min(arr)
    diff = max - min

    # Return Transformed array
    return (arr -min)/diff
