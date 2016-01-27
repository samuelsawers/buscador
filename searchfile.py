
from urllib2 import Request
from urllib2 import urlopen
from bs4 import BeautifulSoup

class Download():
	url=''
	def __init__(self, url):
		self.url = url

	def get_html(self, url):
		try:
			hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding': 'none',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive'}
   			req = Request(url, headers=hdr)
			return urlopen(req).read()
		except Exception, e:
			return 'error'

	def get_html_file(self, filehtml):
		try:
			with open(filehtml, 'r') as f:
				read_data = f.read()
			f.closed
			return read_data
		except Exception, e:
			return 'error'

	def get_tags(self, tag, attribute, value):
		html = self.get_html(self.url)
		if html != 'error':
			soup = BeautifulSoup(html,'html.parser')
			return soup.findAll(tag, attrs={attribute:value})
		else :
			return "error"

	def get_tags_url(self, url, tag, attribute, value):
		html = self.get_html(url)
		if html != 'error':
			soup = BeautifulSoup(html,'html.parser')
			return soup.findAll(tag, attrs={attribute:value})
		else :
			return "error"

	def get_tags_file(self, html, tag, attribute, value):
		if html != 'error':
			soup = BeautifulSoup(html,'html.parser')
			return soup.findAll(tag, attrs={attribute:value})
		else :
			return "error"

	def get_tags_text(self, html):
		if html != 'error':
			soup = BeautifulSoup(html,'html.parser')
			return soup.get_text()
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
			if type_search == 'scribd':
				newtag = soup.img
			if type_search == 'slideshare':
				newtag = soup.img
			if type_search == 'youtube':
				newtag = soup.a
			links.append(newtag[attribute])
		return links

	def get_urls_tu_manga_online(self, html, tag, attribute):
		links=[]
		soup = BeautifulSoup(str(html), 'lxml')
		for index in soup.find_all(tag):
			links.append(index.get(attribute))
		return links

	def get_url_wikipedia(self, html, tag, attribute):
		links=[]
		soup = BeautifulSoup(str(html), 'lxml')
		for index in soup.find_all(tag):
			links.append(index.get(attribute))
		return links
