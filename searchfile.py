
from urllib2 import Request
from urllib2 import urlopen
from bs4 import BeautifulSoup

class Download():
	url=''
	def __init__(self, url):
		self.url = url

	def get_html(self, url):
		try:
			req = Request(url)
			return urlopen(req).read()
		except Exception, e:
			return 'error'

	def get_tags(self, tag, attribute, value):
		html = self.get_html(self.url)
		if html != 'error':
			soup = BeautifulSoup(html,'html.parser')
			return soup.findAll(tag, attrs={attribute:value})
		else :
			return "error"

	def get_tags_html(self, html, tag, attribute, value):
		if html != 'error':
			soup = BeautifulSoup(html,'html.parser')
			return soup.findAll(tag, attrs={attribute:value})
		else :
			return "error"

	def get_urls(self, type_search, etiquetas, attribute):
		links=[]
		for index in range(len(etiquetas)):
			soup = BeautifulSoup(str(etiquetas[index]), 'lxml')
			if type_search == 'slideshare':
				newtag = soup.img
			if type_search == 'youtube':
				newtag = soup.a
			links.append(newtag[attribute])
		return links
