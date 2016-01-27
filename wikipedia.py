import requests
from fpdf import FPDF
from PIL import Image
from searchfile import Download

class Wikipedia:
	page = ''
	search = ''
	def __init__(self):
		pass

	def get_file(self, search, limite, page):
		bb = True
		self.page = page
		self.search = search
		while bb == True:
			url = 'https://en.wikipedia.org/w/index.php?limit='+limite+'&offset='+self.page+'&search='+((self.search).replace(' ', '+'))
			print url
			d = Download(url)
			chapters = d.get_tags('ul', 'class', 'mw-search-results')
			title = d.get_tags_file(str(chapters[0]),'div', 'class', 'mw-search-result-heading')
			desc = d.get_tags_file(str(chapters[0]),'div', 'class', 'searchresult')
			index = 0
			link = []
			for index in range(len(title)):
				link.append(d.get_url_wikipedia(title[index], 'a', 'href'))
				text_title = d.get_tags_text(str(title[index]))
				text_desc = d.get_tags_text(str(desc[index]))
				print link
				print '\033[94m[',(index+1), '] ', text_title, '\033[0m\n', text_desc,'\n'
			option=raw_input("ingrese el numero de una busqueda\npresione n para ir a la pagina siguiente\npresione p para ir a la pagina anterior\n")
			if(option == 'n'):
				self.page = str(int(float(self.page)) + int(float(limite)))
				print '\n\n'
			if(option == 'p' and int(float(self.page)) >= 0 ):
				self.page = str(int(float(self.page)) - int(float(limite)))
				print '\n\n'
			if(option.isdigit()):
				if(int(float(option)) > 0 and int(float(option)) <= (index+1)):
					a = 'https://en.wikipedia.org'+str(link[int(float(option))-1][0])
					v = Download(a)
					div = v.get_tags('div', 'id', 'bodyContent')
					text_page = v.get_tags_text(str(div[0]))
					print '\n',a,'\n','\033[97m'+text_page+'\033[0m\n'
					bb = False
			chapters = []
			chapters = []
			title = []
			desc = []
			text_title = []
			text_desc = []
			url = ''
#			print option
search = raw_input('ingrese su busqueda para wikipedia:\n')
limite = raw_input("cuantos resultados desea ver por pagina\n")
wikipedia = Wikipedia()
wikipedia.get_file(search, limite, '0')

'''
Colores Consola

Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'

'''
