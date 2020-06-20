from task1 import scrap_top_movies
from task4 import scrap_movies_details
from pprint import pprint
import time
import random
import json

def get_movie_list_details(movies_list):
	url=[]
	movies_details=[]
	
	for i in movies_list:
		url.append(i['url'])
	for i in url:
		movies_details.append(json.loads(scrap_movies_details(i)))
		
	return movies_details



# ##########################################################################################################
def analyse_movie_language(movies):
	a=[]
	for i in movies:
		for k in i['Language']:
			a.append(k)
	a=dict.fromkeys(a)
	for i in a:
		count=0
		for k in movies:
			for r in k['Language']:
				if r==i:
					count+=1
		a[i]=count


	return a

# ###################################################################################################################

def analyse_movie_director(movies):
	a=[]
	for i in movies:
		for k in i['director']:
			a.append(k)
	a=dict.fromkeys(a)
	del a['1 more credit']
	for i in a:
		count=0
		for k in movies:
			for r in k['director']:
				if r==i:
					count+=1
		a[i]=count


	return a



# def analyse_languages_and_directors(movies):
# 	a=[]
# 	for i in movies:
# 		for k in i['director']:
# 			a.append(k)
# 	a=dict.fromkeys(a)
# 	for i in a:
# 		b=[]
# 		for r in movies:
# 			if r['director']==i:
# 				b.append(r['Languages'])
		






