"""
CS 620
HW2-b
@author: 
"""
import pandas as pd
import glob
import gc
import os
import numpy as np


#part I
path = r'yob-names' # use your path
yobPath = 'yob-names.csv'
all_files = glob.glob(yobPath + "/*.txt")

# Part II
# a)	How many girls were born between 1990 and 2000?

# b)	What is the most popular boys name in year 1980?

#c)	How many female Benjamin’s are alive today (year 2019)? 

lifeExpectancy = pd.read_csv("cdc-life-expectancy.csv")


