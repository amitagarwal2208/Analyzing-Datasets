import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


df = pd.read_csv("/Volumes/part3/MovieDataset/movie_metadata.csv")

data = df.values

print(df.head(n=10))

print(df.columns)

titles = list(df.get("movie_title"))
print(type(titles))

freq_titles = {}

for t in titles:

	l = len(t)

	try:
		freq_titles[l]+=1
	except:
		freq_titles[l]=1


X = freq_titles.keys()
Y = freq_titles.values()

plt.scatter(X,Y)
plt.xlabel("Length of Movie titles")
plt.ylabel("Frequency of movies with a particular title length")
plt.show()