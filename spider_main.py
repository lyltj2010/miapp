# coding:utf-8
import html_downloader
import html_parser
import json_outputer
import re

class SpiderMain(object):
	def __init__(self):
		self.downloader = html_downloader.Downloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = json_outputer.JsonOutputer()

	def spider(self,root_url):
		print "Spider opened!"
		# from homepage and craw category urls
		cats_cont = self.downloader.download(root_url)
		cats_urls = self.parser.parse_cats_urls(cats_cont)
		count = 0
		for cat_url in cats_urls: # use slice like [:3] to craw at different time!
			print "Start Crawing category %s." % cat_url
			try: 
				pages_cont = self.downloader.download_js(cat_url)
				pages_urls = self.parser.parse_pages_urls(pages_cont,cat_url)
				for page_url in pages_urls:
					print "Start Crawing page %s." % page_url
					try:
						applist_cont = self.downloader.download(page_url)
						applist_urls = self.parser.parse_applist_urls(applist_cont)

						try:
							for app_url in applist_urls:
								app_cont = self.downloader.download(app_url)
								app_detail = self.parser.parse_app_details(app_cont)
								self.outputer.collect_data(app_detail)
								count += 1
								print "Crawed app %s successfully!" % app_detail['name']
						except:
							print "Craw Failed for app %s." % app_url
					except:
						print "Craw Failed for page %s." % page_url

					print "Totally Crawed %d apps now." % count	
				
				name = 'category' + re.findall(r'\d+',cat_url)[0] + ".json"
				self.outputer.output_json(name)
			except:
				print "Craw failed for category %s !" % cat_url
		
		print "Totally Crawed %d apps!" % count
		print "Spider Closed."

if __name__ == "__main__":
	root_url = 'http://app.mi.com/'
	spider = SpiderMain()
	spider.spider(root_url)