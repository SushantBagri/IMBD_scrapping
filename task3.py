from task1 import scrap_top_movies
from pprint import pprint
def movies_by_decade(movies):
	year=[]
	for i in movies:
		if i['year'] not in year:
			year.append(i['year'])
	year=sorted(year)
	decades=[]
	for i in range((((year[0]//10))*10),((year[-1]//10)*10+10),10):
		decades.append(i)
	movies_decades=[]
	for i in range(len(decades)):
		b={decades[i]:''}
		a=[]
		for k in movies:
			if k['year']>=decades[i] and k['year']<(decades[i]+10):
				a.append(k)
		b[decades[i]]=a
		movies_decades.append(b)
	return movies_decades

