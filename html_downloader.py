# coding:utf-8
import requests
from selenium import webdriver

class Downloader(object):
	"""
	Input url, make a request, check it's status
	And then return the RESPONSE.
	"""
	def download_root(self,root_url):
		# for javascript rendered pages
		driver = webdriver.Firefox()
		driver.get(root_url)
		response = driver.page_source
        driver.quit()
        return response

	def download(self,url):
		response = requests.get(url)
		if response.status_code != 200:
			print "Request failed!"
			return None

		return response
		