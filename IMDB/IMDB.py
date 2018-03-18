import pandas as pd

df = content[content['titleType'] == 'movie']


most_movies = df['startYear'].value_counts()
print(most_movies)

#2. Which year was most series ended?


dfSeries = content[content['titleType'] == 'tvseries']
most_series = dfSeries['endYear'].value_counts()
print('the year where most series ended was: ', most_series)




#3. Which genres has the longest runtime per movies?





#4. Which genre covers the most movies?

titles = content[content['titleType'] == 'movie']
genre = titles['genres'].max()
print('genre with most movies is: ', genre)





#5. What is the average runtime on adult films?


genres = content[content['genres'] == 'adult']
average = genres['runtimeMinutes'].mean()

print('average runtime on adultfilms', average)