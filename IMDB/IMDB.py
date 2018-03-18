import pandas as pd

content = pd.read_csv('https://datasets.imdbws.com/title.basics.tsv.gz', sep='\t', header=0)


df = content[content['titleType'] == 'movie']
dfSeries = content[content['titleType'] == 'tvseries']

most_movies = df['startYear'].value_counts()
print(most_movies)
most_Series_ended = dfSeries['endYear'].value_counts()

print('##############################################################################################')
print('##############################################################################################')

print(most_Series_ended)
# 1. Which year was the most movies released?
#2017    18899 movies

# 2. Which year was most series ended?


# 3. Which genres has the longest runtime per movies?


# 4. Which genre covers the most movies?


# 5. What is the average runtime on adult films?
