from fpdf import FPDF
from PIL import Image
import searchfile

<<<<<<< HEAD
class Slideshare:
	def __init__():
		self.arg = arg

	def get_file(self, url):
		url=raw_input('ingrese url de sildeshare:\n')
#		d = Download('http://www.slideshare.net/gloriaortizh/pop-up-books-9941995?qid=024b0da4-45e4-4b7e-9711-3c808c510ad5&v=qf1&b=&from_search=1')
		d = Download(url)
		print d.get_tag('div', 'class', 'slide_container')
/*
		pdf = FPDF('P', 'pt', 'Letter')
		print  "\ndownload ", len(images), " images\n"
		for pag in images:
			aux=urlretrieve(pag)[0]
			img=Image.open(aux)
			size=img.size
			pdf.add_page(format = size)
			pdf.image(aux, x=0, y=0)
		pdf.output('test.pdf', 'F')
		
=======
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
>>>>>>> 5282a7cc4269db6c5d0d63a6832a7826c4aebdf7
