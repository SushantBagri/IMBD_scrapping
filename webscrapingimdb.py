from task1 import scrap_top_movies
# from task2 import group_by_year
from task3 import movies_by_decade
from task4 import scrap_movies_details
from task5 import get_movie_list_details
from task5 import analyse_movie_director
from task5 import analyse_movie_language
from pprint import pprint
print('\t\t\tWELCOME TO WEBSCRAPING OF IMDB')
while 1:
	print('\t\tfor scrap top 250 movie names   PRESS 1')
	print('\t\tfor scrap top 250 movies names by group year   PRESS 2')
	print('\t\tfor scrap top 250 movies by decade   PRESS 3')
	print('\t\tfor scrap movie details   PRESS 4')
	print('\t\tfor movie list details   PRESS 5')
	print('\t\tfor analyse movie director   PRESS 6')
	print('\t\tfor analyse movie language   PRESS 7')
	print('\t\tfor exit     PRESS 0')
	a=int(input('\t\tchoose any option  '))
	if a==1:
		pprint(scrap_top_movies())
	elif a==2:
		def group_by_year(movies):
			year=[]
			movies_by_year=[]
			for i in movies:
				year.append(i['year'])
			year=sorted(list(dict.fromkeys(year)))
			for k in year:
				b={k:''}
				a=[]
				for i in movies:
					if k==i['year']:
						a.append(i)
				b[k]=a
				movies_by_year.append(b)
			return movies_by_year
		movies=scrap_top_movies()
		pprint(group_by_year(movies))
	elif a==3:
		movies=scrap_top_movies()
		pprint(movies_by_decade(movies))
	elif a==4:
		movies=scrap_top_movies()
		pprint(movies)
		b=int(input('   enter the no. movie   '))
		url=movies[b-1]['url']
		pprint(scrap_movies_details(url))
	elif a==5:
		movies_list=scrap_top_movies()
		pprint(get_movie_list_details(movies_list))
	elif a==6:
		movies_list=scrap_top_movies()
		movies=get_movie_list_details(movies_list)
		pprint(analyse_movie_director(movies))
	elif a==7:
		movies_list=scrap_top_movies()
		movies=get_movie_list_details(movies_list)
		pprint(analyse_movie_language(movies))

	elif a==0:
		break
	else:
		print('\t\t\tyou choose wrong option')




