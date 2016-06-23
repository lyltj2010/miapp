# coding:utf-8
import requests
class Downloader(object):
	"""
	Input url, make a request, check it's status
	And then return the RESPONSE.
	"""
	def download(self,url):
		if url is None:
			return None

		response = requests.get(url)
		
		if response.status_code != 200:
			print "Request failed!"
			return None

		return response
		