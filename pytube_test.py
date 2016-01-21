from pytube import YouTube
import lxml.html

class YouTubeDownloader:
	
	video_url_preffix = 'https://www.youtube.com'
	video_url_index = 0
	split_char = '&'
	playlist_video_urls = []
	
	def get_videos(self, url, codec='mp4', location='/tmp/'):
		print "Analizing Youtube url"
		
		main_video_url = url.split(self.split_char)[self.video_url_index]
		tree = lxml.html.parse(url)
		root = tree.getroot()
		xpath_string_playlist = ".//ol[@id='playlist-autoscroll-list']"
		xpath_string_single_video = ".//a"
		video_url_attrib = 'href'
		
		for video_node in root.findall(xpath_string_playlist):
			video_url_node = video_node.find(xpath_string_single_video)
			video_url_suffix = video_url_node.get(video_node_attrib).split(self.split_char)[self.video_url_index]
			self.playlist_video_urls.append(self.video_url_preffix + video_url_suffix)
			
		for video_url in self.playlist_video_urls:
			print video_url
		
		#print "Downloading main video"
		#download_now(main_video_url, codec, location)
		
	
	def download_now(self, url, codec='mp4', location='/tmp/'):
		try:
			yt = YouTube(self.url)
			yt.get_videos()
			video = yt.filter(codec)[0]
			video.download(location)
		except Exception, e:
			print e
			print "Error: Invalid URL or network problem"
