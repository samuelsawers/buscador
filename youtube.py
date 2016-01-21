from pytube import YouTube
from searchfile import Download

class Youtube:
	def __init__(self):
		pass

	def download_now(self, url, codec='mp4', location='/tmp/'):
		try:
			yt = YouTube(url)
			yt.get_videos()
			video = yt.filter(codec)[0]
			video.download(location)
		except Exception, e:
			print e
			print "Error: Invalid URL or network problem"

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
					print video_url_preffix+valor
					valor = (video_url_preffix+valor).split('&')[0]
					print valor
					self.download_now(str(valor), 'mp4', '/Users/samuel/Documents/python')
				print 'se bdescargo la lista el archivo'
			else: print 'link de slideshare no hace referencia a un archivo valido'

#		else: print 'link de slideshare no es valido'


url = 'https://www.youtube.com/watch?v=qEvnwW-YtRw&list=PLOcurmo_gZqZPgMdgj_J14IH5VQLkXY_9'
#url = raw_input('ingrese url de sildeshare:\n')
youtube = Youtube()
youtube.get_files(url)
