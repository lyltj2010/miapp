# coding:utf-8
import requests
from selenium import webdriver

class Downloader(object):
	"""
	Input url, make a request, check it's status
	And then return the RESPONSE.
	"""
	def download_js(self,url):
		# for javascript rendered pages
		driver = webdriver.Firefox()
		driver.get(url)
		response = driver.page_source
		driver.quit()
		return response

	def download(self,url):
		response = requests.get(url)
		if response.status_code != 200:
			print "Request failed! with stats_code %s!" % response.status_code
			return None

		return response
		