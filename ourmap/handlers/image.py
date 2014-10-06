__author__ = 'andychou'

import logging

from base import Handler
import json
import urllib2
import sys
sys.path.append('../')
from flickr_keys import API_KEY, API_SECRETS,USER_ID
from google.appengine.api import urlfetch




class imageHandler(Handler):
	def get(self):
		#return self.write("hello")
		self.redirect("/")
		pass
	def post(self):
		result={}
		state = self.request.get('state')
		page_wanted = self.request.get('cur_page')
		if page_wanted=="":
			json_image_list = query_image_list(str(state))
		else:
			json_image_list = query_image_list(str(state),page_wanted)
		cur_page, pages = get_pages(json_image_list)
		url_dict = create_photo_html(json_image_list)
		result['url_dict'] = url_dict
		result['pages_count'] = pages
		result['page'] = cur_page
		json_data = json.dumps(result)
		return self.write(json_data)

#this function queries a API request and convert it to json format
def query_image_list(state, page='1'):
	url = photo_search_url(API_KEY, USER_ID, state, page)
	return get_json(url)

#thie function takes a json format of photo info
#then converts it to a list of URLs
def create_photo_html(json_image_list):
	url =""
	for i in json_image_list['photos']['photo']:
		farmid = i['farm']
		serverid = i['server']
		id = i['id']
		secret = i['secret']
		title = i['title']
		url += (create_a_html(str(farmid), str(serverid), str(id), str(secret), title))
	return url

#this function converts flickr photo info into URL format
def create_a_html(farmid, serverid, id, secret,title):
	small_pic ='https://farm'+farmid+'.staticflickr.com/'+serverid+'/'+id+'_'+secret+'_s.jpg'
	imgsrc = 'https://farm'+farmid+'.staticflickr.com/'+serverid+'/'+id+'_'+secret+'_b.jpg'

	a_link = '''<a href="%s" title="%s" data-gallery><img src="%s" alt="%s"></a>'''

	return str(a_link % (imgsrc, title, small_pic, title))

#returns how many pages given the Flickr json API response
def get_pages(json_data):
	pages = json_data['photos']['pages']
	cur_page = json_data['photos']['page']
	return (cur_page,pages)

def photo_search_url(api_key,user_id,tags,pages='1',format='json&nojsoncallback=1'):
	return 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key='+api_key+'&user_id='+user_id+'&tags='+tags+'&page='+pages+'&format='+format
	#return 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key='+api_key+'&user_id='+user_id+'&tags='+tags+'&format='+format

def get_json(url):
	response = urlfetch.fetch(url)
	json_data = json.loads(response.content)
	return json_data



