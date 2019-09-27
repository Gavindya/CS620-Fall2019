"""
CS 620
HW2-b
@author: Gavindya Jayawardena (UIN-01130618)
"""
import pandas as pd
import glob
import gc
import os
import numpy as np

#part I
path = "./wrangling/yob-names/"
yobPath = 'yob-names.csv'
all_files = glob.glob(path + "*.txt")

cols = ['name','sex','frequency']
df = pd.DataFrame()

print(len(all_files))

for file in all_files:
    print(file)
    yob = pd.read_csv(file, names=cols, header=None)
    year = file.split('/')[-1].split('.')[0][3:]
    print(year)
    yob.insert(0,'year',year)
    print(yob.head())
    df = df.append(yob)


# print(df.head())
# print(df.tail())

print(len(df['year'].unique()))
# Part II
# a)	How many girls were born between 1990 and 2000?

# b)	What is the most popular boys name in year 1980?

#c)	How many female Benjamin’s are alive today (year 2019)?

# lifeExpectancy = pd.read_csv("cdc-life-expectancy.csv")


