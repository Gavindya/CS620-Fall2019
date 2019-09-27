import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# a= pd.Series([4, 7, -5, 3])
#
# print(a)
#
# print(list(a))
#
# print(a[[0,1,2]])
#
# print(7 in a.values)
# sdata = {'Texas': 10, 'Ohio': 20, 'Oregon': 15, 'Utah': 18} # Dictionary
# states = ['Texas', 'Ohio', 'Oregon', 'Iowa']
# obj4 = pd.Series(sdata)
# print(obj4)
# # Explicitly says the index ( w/o Utah. but with Iowa)
# obj5 = pd.Series(sdata, index=states)
# print(obj5)
# #Activity 4
# import random
#
# numlist = [random.randint(1,100) for x in range(10)]
# idx = range(1,11)
# RandomNumbers = pd.Series(numlist,idx)
# print(RandomNumbers)
# Squares = RandomNumbers**2
# print(Squares[-4:])
# print(list(Squares[Squares>500]))
## Dataframe
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],'year': [2000, 2001, 2002, 2001, 2002],'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame = pd.DataFrame(data)
# print(frame)
#
# states = ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada']
# yr = [2000, 2001, 2002, 2001, 2002]
# data2 = {'state':states,'year':yr}
# df = pd.DataFrame(data2)
# print([df.state,df.year])
# # Activity 5
# df = pd.read_csv("https://www.cs.odu.edu/~sampath/courses/f19/cs620/files/data/values.csv")
# print(df)
# print(df.factor_1.mean())
# print(df.factor_1.std())
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
# 'year': [2000, 2001, 2002, 2001, 2002],
# 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['A', 'B', 'C', 'D', 'E'])
# print(frame2)
#
# # loc(rows,columns) using labels
# print(frame2.loc['A':'B',['state','pop']])
#
# # iloc(rows,columns) using index of numerics
# print(frame2.iloc[:2,1:3])
# Activity 6
# data = np.random.randint(1,100, (3,5))
# print(data)
# df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=[1,2,3,4,5])
# print(df)
# df = df.T
# print(df)
# df[df<40] = 0
# print(df)
# # Activity 7
# import math
#
# def sqr_root(x):
#     return math.sqrt(x)
#
# frame = df.applymap(sqr_root)
# print(frame)
# # Activity 8
# def cleanBRFSSFrame(df):
#     df = df.drop(['sex'], axis=1)
# #     df = df.dropna()
#     return df
#
# def describe(df):
#     print(df['weight2'].count())
#     print(df['weight2'].mean())
#     print(df['weight2'].min())
#     print(df['weight2'].std())
#     print(df['weight2'].quantile())
#
# def age_calculations(df):
#     print(df['age'].median())
#     print(df['age'].mode())
#
# df = pd.read_csv("https://www.cs.odu.edu/~sampath/courses/f19/cs620/files/data/brfss.csv", index_col=0)
# df = cleanBRFSSFrame(df)
# print(df.describe())
# age_calculations(df)
#
# # df['weight2'].hist(bins=100)
# # plt.show()
#
# from pandas.plotting import scatter_matrix
# scatter_matrix(df[['weight2', 'wtyrago', 'htm3' ]])
#
# plt.show()
# data = {"height_inch":{'A':63, 'B':67, 'C':70},
#         "height_cm":{'A':160, 'B':170.2, 'C':177.8},
#         "weight":{'A':150, 'B':160, 'C':171}}
# df2 = pd.DataFrame(data)
# print(df2)
# #Activity 9
# df = pd.read_csv("https://www.cs.odu.edu/~sampath/courses/f19/cs620/files/data/brfss.csv", index_col=0)
# df = df.drop(['sex'], axis=1)
# df = df.dropna()
# print(df.head())
#
#
# def transform(series):
#     min = series.min()
#     max = series.max()
#     dif = max - min
#     return (series - min)/dif
#
# df = df.apply(lambda x: transform(x))
# print(df.head())
# df.boxplot()
# plt.show()
def zscore(series):
   return (series - series.mean(skipna=True)) / series.std(skipna=True);
d1 = pd.read_csv("https://www.cs.odu.edu/~sampath/courses/f19/cs620/files/data/brfss.csv")
d1 = d1.drop(['sex'],axis=1)
d2 = d1.apply(lambda x: zscore(x))
d2.boxplot()
plt.show()