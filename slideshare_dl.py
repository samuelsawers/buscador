import lxml.html

class SlideShareDownloader:

	def downloadAsPdf(link, location='/tmp/'):
		# Only retiereves and parses image links
		tree = lxml.html.parse(link)
		root = tree.getroot()
		#print "Image links:"
		xpath_string = ".//*[@class='slide']"
		split_char = "?"
		img_index = 0
		for node in root.findall(".//*[@class='slide']"):
			img_node = node.find('img')
			img_path = img_node.get('data-normal').split(split_char)[img_index]
		#print img_path
