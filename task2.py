# from task1 import scrap_top_movies
# from pprint import pprint


# def group_by_year(movies):
# 	year=[]
# 	movies_by_year=[]
# 	for i in movies:
# 		year.append(i['year'])
# 	year=sorted(list(dict.fromkeys(year)))
# 	for k in year:
# 		b={k:''}
# 		a=[]
# 		for i in movies:
# 			if k==i['year']:
# 				a.append(i)
# 		b[k]=a
# 		movies_by_year.append(b)
# 	return movies_by_year

