from pytube import YouTube
from searchfile import Download
from pytube import utils

class Youtube:
	def __init__(self):
		pass

	def download_now(self, url, codec='mp4', location='/tmp/'):
		try:
			yt = YouTube(url)
			yt.get_videos()
			video = yt.filter(codec)[0]
			print 'file name:', video.filename
			video.download(location, on_progress=utils.print_status)
		except Exception, e:
			print "Error: Invalid URL or network problem or file exist"

	def get_files(self, url):
		position_link = 0
		if url.find('youtube.com')>position_link:
			d = Download(url)
			div = d.get_tags('div', 'class', 'playlist-videos-container yt-scrollbar-dark yt-scrollbar')
			indice_div = 0
			videos = d.get_tags_html(str(div[indice_div]), 'a', 'class', 'yt-uix-sessionlink')
#			print videos[:]
			if videos != 'error':
				links = d.get_urls('youtube', videos, 'href')
				video_url_preffix = 'https://www.youtube.com'
				for valor in links:
					valor = (video_url_preffix+valor).split('&')[0]
					self.download_now(str(valor), 'mp4', '/Users/samuel/Documents/python')
					print '\n'
				print 'se descargo la lista el archivo'
			else: print 'link de youtube no hace referencia a un archivo valido'

	def get_file(self, url):
		position_link = 0
		if url.find('youtube.com')>position_link:
			valor = (url).split('&')[0]
			self.download_now(str(valor), 'mp4', '/Users/samuel/Documents/python')
			print '\nse descargo el video'
		else: print 'link de youtube no hace referencia a un archivo valido'


# Muestra una barra de progreso que se actualiza en una misma linea. Ejemplo de uso:
youtube = Youtube()
#url = 'https://www.youtube.com/watch?v=qEvnwW-YtRw&list=PLOcurmo_gZqZPgMdgj_J14IH5VQLkXY_9'
#url = 'https://www.youtube.com/watch?v=fRh_vgS2dFE&index=4&list=PLSFitF4B6yNS82pcRx5XvD1PB6m8lIs5J'
opcion = raw_input('options\n press 1 and enter for download a list video\n press 2 and enter for download a video\n')
url = raw_input('ingrese url de youtube:\n')
if opcion == '1':
	youtube.get_files(url)
if opcion == '2':
	youtube.get_file(url)
