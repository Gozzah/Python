import pandas as pd
import numpy as np

import webget as wg

url = 'https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv'
response = wg.download(url)

print(response +'downloadet')

dataFrame = pd.read_csv('complete.csv')

df = pd.DataFrame(dataFrame.groupby('club')['eur_value'].sum())
top_3_Valuable_Players = df.nlargest(3,'eur_value')
bottom_3_Valuable_Players = df.nsmallest(3,'eur_value')

#Top 3 Most valuable and useless shitplayers players
print('The three most valuable clubs are: \n', top_3_Valuable_Players)
print('The three most valuable clubs are: \n', bottom_3_Valuable_Players)



#question 2

#averageage =dataFrame.groupby('nationality', as_index=False)['age'].mean()
#print(averageage)
#question 2

most_frequent_nationality = dataFrame['nationality'].value_counts()
print(most_frequent_nationality)

#England is the most frequent nationality

# Question 4 (Frequency)
#// .mean is a numpy func. to count the average of array elements.

#averageage = dataFrame['age'].mean()
#print("The average players age is: ", averageage)

#averageweight = dataFrame['weight_kg'].mean()
#print("The average players weight in kg is: ", averageweight)

#averageheight = dataFrame['height_cm'].mean()
#print("The average players height in cm is: ", averageheight)

#Question 5
#// Average difference between value and wage for all listed players

#Value = dataFrame['eur_value'].mean()
#Wage = dataFrame['eur_wage'].mean()
#print("The average difference between value and wage between all players is: ", Value - Wage, "EUR")