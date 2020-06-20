from task1 import scrap_top_movies
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
import os
import time
import random 
import time

# # def movies_url(movies):
# # 	url=[]
# # 	for i in movies:
# # 		url.append(i['url'])
# # 	return url
# ###################################################################################################################################################

def scrap_movies_details(url):
	file_name=''
	for i in url[27:]:
		if i!='/':
			file_name+=i
		else:
			break
	file_name+='.json'
	if os.path.exists(file_name):
		file=open(file_name,'r')
		text=file.read()
		file.close()
		return text
	infor_movie={'name':'','director':'','Country':'','Language':'','runtime':'','poster_url':'','bio':'','genre':''}
	data=requests.get(url)
	n=random.randint(1,3)
	time.sleep(n)
	file_data=BeautifulSoup(data.text,'html.parser')
	name_details=file_data.find('div',class_='title_wrapper').h1.get_text().strip()
	name=''
	for i in name_details:
		if i!='(':
			name+=i
		else:
			break
	infor_movie['name']=name.strip()
	main_div=file_data.find('div',class_='plot_summary')
	infor_movie['bio']=main_div.find('div',class_='summary_text').get_text().strip()
	director=main_div.find('div',class_='credit_summary_item')
	a=director.find_all('a')
	for text in a:
		infor_movie['director']=[i.get_text() for i in a]
	subtext=file_data.find('div',class_='subtext')
	movie_runtime=subtext.find('time').get_text().strip()
	if 'min' in movie_runtime:
		runtime_minutes=int(movie_runtime[3:].strip('min'))
		infor_movie['runtime']=int(movie_runtime[0])*60+runtime_minutes
	else:
		infor_movie['runtime']=int(movie_runtime[0])*60
	genre=subtext.find_all('a')
	genre.pop()
	infor_movie['genre']=[i.get_text() for i in genre]
	extra_infor=file_data.find('div',attrs={'class':'article','id':'titleDetails'})
	all_div=extra_infor.find_all('div')
	for div in all_div:
		h4=div.find_all('h4')
		for text in h4:
			if 'Language:' in text:
				a=div.find_all('a')
				infor_movie['Language']=[i.get_text() for i in 	a]
			elif 'Country:' in text:
				a=div.find_all('a')
				infor_movie['Country']=''.join([k.get_text() for k in a])
	infor_movie['poster_url']='www.imdb.com'+file_data.find('div',class_='poster').a['href']
	data_for_file=json.dumps(infor_movie)
	open_file=open(file_name,'w')
	open_file.write(data_for_file)
	open_file.close()
	file=open(file_name,'r')
	text=file.read()
	file.close()
	return text



