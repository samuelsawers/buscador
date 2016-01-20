
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

	def get_url(self, etiquetas):
		links=[]
#		for index in range(len(etiquetas)):
		soup = BeautifulSoup(etiquetas, 'lxml')
		newtag = soup.img
		print "data=", newtag['data-normal']

d = Download('http://www.slideshare.net/gloriaortizh/pop-up-books-9941995?qid=024b0da4-45e4-4b7e-9711-3c808c510ad5&v=qf1&b=&from_search=1')
#imgs=['<img alt="POSTITULO DE GRABADO    ESPACIO CURRICULAR: SEMINARIOALUMNA: GLORIA LUCIA ORTIZ HOYOS                      ESCUELA DE ARTE..." class="slide_image" data-full="http://image.slidesharecdn.com/popupbooks-111029161802-phpapp02/95/pop-up-books-1-1024.jpg?cb=1319905157" data-normal="http://image.slidesharecdn.com/popupbooks-111029161802-phpapp02/95/pop-up-books-1-728.jpg?cb=1319905157" data-small="http://image.slidesharecdn.com/popupbooks-111029161802-phpapp02/85/pop-up-books-1-320.jpg?cb=1319905157" src="http://image.slidesharecdn.com/popupbooks-111029161802-phpapp02/95/pop-up-books-1-728.jpg?cb=1319905157"/>', '<img alt="\u2022 Con esta breve presentaci\xf3n deseo lograr un acercamiento al maravilloso  tema de los libros desplegables, transitar por ..." class="slide_image" data-full="http://image.slidesharecdn.com/popupbooks-111029161802-phpapp02/95/pop-up-books-2-1024.jpg?cb=1319905157" data-normal="http://image.slidesharecdn.com/popupbooks-111029161802-phpapp02/95/pop-up-books-2-728.jpg?cb=1319905157" data-small="http://image.slidesharecdn.com/popupbooks-111029161802-phpapp02/85/pop-up-books-2-320.jpg?cb=1319905157" src=""/>']
imgs = d.get_tags('img', 'class', 'slide_image')
print imgs[0]
print len(imgs[0])
d.get_url(imgs)
