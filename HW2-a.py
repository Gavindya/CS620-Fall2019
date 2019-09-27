"""
CS 620
HW2-a
@author: Gavindya Jayawardena (UIN-01130618)
"""
import pandas as pd
from collections import deque

"""Given two list of numbers that are already sorted, 
 return a single merged list in sorted order.
"""
def merge(sortedListA, sortedListB):
    list_merged = deque()
    list_A = deque(sortedListA)
    list_B = deque(sortedListB)

    while list_A and list_B:
        a = list_A[0]
        b = list_B[0]
        if a > b:
            # print('a > b', a, b)
            list_merged.append(list_B.popleft())
            # print('list_merged', list_merged)
        elif a == b:
            # print('a == b', a, b)
            list_merged.append(list_A.popleft())
            list_merged.append(list_B.popleft())
            # print('list_merged', list_merged)
        else:
            # print('a < b', a, b)
            list_merged.append(list_A.popleft())
            # print('list_merged', list_merged)
    sortedList =  list_merged + list_A + list_B

    return list(sortedList)
test_list1 = [-1, 5,5, 9, 11]
test_list2 = [-3, 4, 5, 8, 100]
merged_lst = merge(test_list1,test_list2)
print(merged_lst)

"""Given a list of numbers in random order, return the summary statistics 
that includes the max, min, mean, population standard deviation, median,
75 percentile, and 25 percentile.
"""
def summaryStatistics(listOfNums):

    seriesOfNums = pd.Series(listOfNums)

    maxVal = seriesOfNums.max()
    minVal = seriesOfNums.min()
    meanVal = seriesOfNums.mean()
    stdev = seriesOfNums.std()
    median = seriesOfNums.median()
    perc75 = seriesOfNums.quantile(q=0.75)
    perc25 = seriesOfNums.quantile(q=0.25)

    return {'max': maxVal,
            'min': minVal,
            'mean': meanVal,
            'stdev': stdev,
            'median': median,
            'perc75': perc75,
            'perc25': perc25}

# test_list = [0, 10, 20, 20, 40, 50]
# stats = summaryStatistics(test_list)
# print(stats)

"""Given a list of real numbers in any range, scale them to be 
between 0 and 1 (inclusive). For each number x in the list, the new number 
is computed with the formula ((x - min)/(max - min)) where max is the 
maximum value of the original list and min is the minimum value of the list. 
"""

def scaleToDigits(listOfNums):
    seriesOfNums = pd.Series(listOfNums)

    max =  seriesOfNums.max()
    min =  seriesOfNums.min()
    diff = max - min
    return (seriesOfNums -min)/diff

# trnsformed = scaleToDigits(test_list)
# print(trnsformed)