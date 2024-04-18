# importing packages 
from pytube import YouTube 
import os
from decouple import config
import logging


class YoutubeService():
	def __init__(self) -> None:
		pass
	def download_youtube_mp3_by_url(self, url: str, output_path: str = config('OUTPUT_PATH')):
		# url input from user 
		yt = YouTube(str(url))
		
		# extract only audio 
		video = yt.streams.filter(only_audio=True).first()
		# download the file 
		out_file = video.download(output_path=output_path)
		# save the file 
		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file) 
		# result of success 
		logging.info(yt.title + " has been successfully downloaded.")

if __name__ == "__main__":
	service = YoutubeService()
	service.download_youtube_mp3_by_url("https://www.youtube.com/watch?v=ErhGuwNgrmw")