# -*- coding: utf-8 -*-
"""
Cleaning data
"""
import pandas as pd

df=pd.read_csv("movie_dataset.csv")

df.dropna(inplace = True)
df = df.reset_index(drop=True)

df.drop_duplicates(inplace = True)

#print(df)

#########################################################################
#Q1

max_rating_index = df['Rating'].idxmax()

title = df.at[max_rating_index, 'Title']

print("Most rated:", title)

###############################################################################
#Q2

average_revenue = df['Revenue (Millions)'].mean()

print("Average revenue:", average_revenue)

############################################################################
#Q3

years_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

#print(years_2015_2017)

average_revenue_of_years_2015_2017 = years_2015_2017['Revenue (Millions)'].mean()

print("Average revenue from 2015 to 2017:", average_revenue_of_years_2015_2017)
################################################################################
#Q4
movies2016=df[df['Year']==2016]

number_movies2016=len(movies2016)
print("Number of movies in 2026",number_movies2016)
#################################################################################
#Q5

movies_nolan = df[df["Director"]=="Christopher Nolan"]
number_movies_by_nolan = len(movies_nolan)
print("Number of movies by Nolan:",number_movies_by_nolan)

##################################################################
#Q6
rating_8=df[df['Rating']>=8]
number_rating_8 = len(rating_8)
print("Number of movies with rating of at least 8:",number_rating_8)
##########################################################################3
#Q7
median_nolan=movies_nolan['Rating'].median()
print("The rating of movies by Nolan is:",median_nolan)
#########################################################
#Q8
year_highest_average = df.groupby('Year')['Rating'].mean().idxmax()
print("Year with the highest average rating:",year_highest_average)

#####################################################################
#Q9
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

percentage_increase = ((len(movies_2016) - len(movies_2006)) / len(movies_2006)) * 100
print("Percentage increase in the number of movies between 2006 and 2016:", percentage_increase)

##############################################################################################################3
#Q10
from collections import Counter

all_actors = df['Actors'].str.split(', ').sum()
most_common_actor = Counter(all_actors).most_common(1)[0][0]
print("Most common actor in all the movies:", most_common_actor)

####################################################################################
#Q11
unique_genres = df['Genre'].str.split(', ').explode().nunique()
print("Number of unique genres in the dataset:", unique_genres)
########################################################################
#Q12
correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)