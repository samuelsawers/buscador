from urllib import urlretrieve
from fpdf import FPDF
from PIL import Image
from searchfile import Download

class Slideshare:
	def __init__(self):
		pass

	def get_file(self, url):
		position_link = 0
		if url.find('slideshare.net')>position_link:
			d = Download(url)
			imgs = d.get_tags('img', 'class', 'slide_image')
			if imgs != 'error':
				links = d.get_urls('slideshare', imgs, 'data-full')
				pdf = FPDF('P', 'pt', 'Letter')
				index_cache = 0
				index_link = 0
				print "\nDownload images [",len(links),"]:\n"
				for pagina_pdf in links:
					file_path=urlretrieve(pagina_pdf.split('?')[index_link])[index_cache]
					print " ", pagina_pdf
					img=Image.open(file_path)
					pdf.add_page(format = img.size)
					pdf.image(file_path, x=0, y=0)
				pdf.output('slideshare.pdf', 'F')
				print 'se genero en archivo slideshare.pdf'
			else: print 'link de slideshare no hace referencia a un archivo valido'
		else: print 'link de slideshare no es valido'


url = 'http://www.slideshare.net/gloriaortizh/pop-up-books-9941995?qid=024b0da4-45e4-4b7e-9711-3c808c510ad5&v=qf1&b=&from_search=1'
url = raw_input('ingrese url de sildeshare:\n')
slideshare = Slideshare()
slideshare.get_file(url)
