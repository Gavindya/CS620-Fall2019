"""
CS 620
HW2-b
@author: Gavindya Jayawardena (UIN-01130618)
"""
import pandas as pd
import glob

# create an empty dataframe
df = pd.DataFrame()

# part I
path = "./wrangling/yob-names/"
yobPath = 'yob-names.csv'
all_files = glob.glob(path + "*.txt")

# Define columns
cols = ['name','sex','frequency']

# Iterate through all the files in path folder
for file in all_files:
    # Read text file into a dataframe providing column names
    yob_df = pd.read_csv(file, names=cols, header=None)

    # Extract Year From file name
    year = file.split('/')[-1].split('.')[0][3:]

    # Insert Year as the first column of the dataframe
    yob_df.insert(0,'year',year)

    # append the dataframe to the global dataframe (df)
    df = df.append(yob_df)

df.sort_values('year',inplace=True)
# Write the dataframe df to yob-names.csv file
df.to_csv('yob-names.csv', index=False, encoding='utf-8')


# Part II

# Read back the generated yob-names.csv file if not running the program from beginning
if(len(df) == 0):
    df = pd.read_csv('yob-names.csv')


# a) What is the most popular boys name in year 1980?

# Filter dataframe df to get rows with year = 1980 and sex = Male
df_1 = df[(df['year']==1980) & (df['sex']=="M")]
# Get rows with the highest frequency from df_1
df_2 = df_1.loc[df_1['frequency'].idxmax()]
# Get names of the highest frequency boys
popular_boys_name = df_2['name']
print('most popular boys name in year 1980: ',popular_boys_name )


# b)	How many girls were born between 1990 and 2000?

# Filter dataframe df to get rows with year -> 1990 < year < 2000 and sex = Female
df_3 = df[(df['year']>1990) & (df['year']<2000) & (df['sex']=="F")]
# Get the sum of the frequencies as the count of the girls born between 1990 and 2000
girls_count = df_3['frequency'].sum()
print("girls born between 1990 and 2000 : ", girls_count)


#c)	How many female Benjamin’s are alive today (year 2019)?

# Read cdc-life-expectancy.csv to lifeExpectancy dataframe
lifeExpectancy = pd.read_csv("./wrangling/cdc-life-expectancy.csv")
# Calculate expected life ending year of females and add a new column (end_year_F) to the lifeExpectancy dataframe
lifeExpectancy['end_year_F'] = lifeExpectancy['year'] + lifeExpectancy['F']
# create yob list based on life ending year of females >= 2019
birth_years_list = list(lifeExpectancy[(lifeExpectancy['end_year_F'] >= 2019)]['year'])
# create a new dataframe df_4 by filtering the years (in yob list), sex (F) and name (Benjamin)
df_4 = df.query('year in @birth_years_list')
df_4 = df_4[(df_4['sex']=="F") & (df_4['name']=="Benjamin")]
# Get the sum of the frequencies in df_4 as the count of the Benjamin’s born between 1990 and 2000
benjamin_count = df_4['frequency'].sum()
print("Number of Benjamin’s alive today (year 2019) : ", benjamin_count)