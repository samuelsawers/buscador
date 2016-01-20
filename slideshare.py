import urllib2
import urllib
from fpdf import FPDF
from PIL import Image
#funcion de descarga de la pagina web
def gethtml(url):
	try:
		req = urllib2.Request(url)
		return urllib2.urlopen(req).read()
	except Exception, e:
		print e
		return ''
#link de prueba
#url = 'http://www.slideshare.net/gloriaortizh/pop-up-books-9941995?qid=024b0da4-45e4-4b7e-9711-3c808c510ad5&v=qf1&b=&from_search=1'
url=raw_input('ingrese url de sildeshare:\n')
html=gethtml(url)
cad=html.split('<div class="slide_container">')[1]
sections = cad.split('section')
images=[]
i = 1
j = 0
for x in sections:
	i+=1
	if i % 2 == 1:
		aux = x.split('"')[13]
		if aux.find('slideshare') > -1:
			images.append(aux.split('?')[0])
			print images[j]
			j += 1

pdf = FPDF('P', 'pt', 'Letter')
print  "\ndownload ", len(images), " images\n"

filepath_index = 0
for url in images:
	filepath = urllib.urlretrieve(url)[filepath_index]
	img = Image.open(filepath)
	size = img.size
	pdf.add_page(format = size)
	pdf.image(aux, x=0, y=0)
pdf.output('test.pdf', 'F')
