import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

def scrap_top_movies():
	file_data=requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
	data=BeautifulSoup(file_data.text,'html.parser') 
	main_div=data.find('div',class_='lister')
	t_body=main_div.find('tbody',class_='lister-list')
	t_r=t_body.find_all('tr')
	ranks=[]
	movie_name=[]
	movie_ratings=[]
	movie_year=[]
	movie_url=[]
	for tr in t_r:
		position=tr.find('td',class_='titleColumn').get_text().strip()
		rank=''
		movie_name.append(tr.find('td',class_='titleColumn').a.get_text())
		movie_year.append(tr.find('td',class_='titleColumn').span.get_text())
		movie_ratings.append(tr.find('td',class_='ratingColumn').strong.get_text())
		link=tr.find('td',class_='titleColumn').a['href']
		movie_url.append('https://www.imdb.com'+link)
		for i in position:
			if '.' not in i:
				rank=rank+i
			else:
				break
		ranks.append(rank)
	details={'name':'','year':'','position':'','ratings':'','url':''}
	main_list=[]
	for i in range(0,len(ranks)):	
		details['name']=movie_name[i]
		details['position']	=int(ranks[i])
		details['year']=int(movie_year[i][1:5])
		details['url']=str(movie_url[i])
		details['ratings']=float(movie_ratings[i])
		main_list.append(details.copy())
	return main_list

# pprint(scrap_top_movies())
		
		

	


