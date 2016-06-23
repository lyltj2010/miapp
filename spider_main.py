# coding:utf-8
import html_downloader
import html_parser
import json_outputer

class SpiderMain(object):
	def __init__(self):
		self.downloader = html_downloader.Downloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = json_outputer.JsonOutputer()

	def spider(self,root_url):
		print "Spider opened!"
		pages_cont = self.downloader.download_root(root_url)
		pages_urls = self.parser.parse_pages_urls(pages_cont,root_url)
		count = 0
		for page_url in pages_urls:
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
					print "Craw Failed for app %s" % app_url
			except:
				print "Craw Failed for page %s" % page_url

			print "Totally Crawed %d apps!" % count	

		self.outputer.output_json(name='woo.json')
		
		print "Spider Closed!"

if __name__ == "__main__":
	root_url = 'http://app.mi.com/category/1'
	spider = SpiderMain()
	spider.spider(root_url)