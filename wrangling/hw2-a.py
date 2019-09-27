"""
CS 620
HW2-a
@author:  Gavindya Jayawardena (UIN-01130618)
"""


"""Given two list of numbers that are already sorted, 
 return a single merged list in sorted order.
"""
def merge(sortedListA, sortedListB):
    #Complete this part 
    return sortedList

"""Given a list of numbers in random order, return the summary statistics 
that includes the max, min, mean, population standard deviation, median,
75 percentile, and 25 percentile.
"""    
def summaryStatistics(listOfNums):
    #Complete this part. 
    # You can decide to return the following statistics either in a sequence 
    # type (i.e., list, tuple), or a key-value pair (i.e., dictionary)
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
    #complete this part
    return newList