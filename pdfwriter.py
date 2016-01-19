from fpdf import FPDF

pdf = FPDF('P', 'mm', 'Letter')

numpages = 3

for pag in range(numpages):
	pdf.add_page()
	path = '0' + str(pag+1) + '.jpg'
	pdf.image(path, x=0, y=0, w=200)
pdf.output('test.pdf', 'F')
