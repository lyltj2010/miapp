# -*- coding: utf-8 -*-
import scrapy
from xiaomi.items import XiaomiItem
from scrapy_splash import SplashRequest
import re
# Run splash with docker
# docker-machine start default; docker-machine regenerate-certs default; eval "$(docker-machine env default)"
# docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
class HomeSpider(scrapy.Spider):
    name = "xiaomiapp"
    allowed_domains = ["mi.com"]
    start_urls = ["http://app.mi.com/"]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url,self.parse,args={'wait':0.1,'html':1,})

    def parse(self,response):
        # Start from start_urls
        # Parse category urls and yield request to follow
        hrefs = response.xpath('//ul[@class="category-list"]/li/a/@href') #[0:1]        
        for href in hrefs:
            url = response.urljoin(href.extract()) # + "#page=" + '0'
            yield scrapy.Request(url,callback=self.parse_cat_app)
            # yield SplashRequest(url,self.parse_cat_app,args={'wait':0.1,'html':1,})

    def parse_cat_app(self,response):
        hrefs = response.xpath('//ul[@id="all-applist"]/li/h5/a/@href') #[0:3]
        for href in hrefs:
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_app_details)
            # yield SplashRequest(url,callback=self.parse_app_details,args={'wait':0.1,'html':1,})

        # cat_url = response.url # like http://app.mi.com/category/5#page=66
        # next_page_num = int(re.findall('\d+',cat_url)[-1]) + 1 # like 66
        # if next_page_num < 10:
        #     next_page_url = re.sub(r'=\d+','='+str(next_page_num),cat_url)
        #     yield SplashRequest(next_page_url,callback=self.parse_cat_app,args={'wait':0.01,'html':1,})
            
        # try:
        #     next_page_url = response.url + '#page=' + str(current_page[0])
        # except IndexError:
        #     next_page_url = None

    def parse_app_details(self,response):
        item = XiaomiItem()
        
        sel_intro = response.xpath('//div[@class="intro-titles"]')
        item['name'] = sel_intro.xpath('h3/text()').extract_first()
        item['company'] = sel_intro.xpath('p/text()').extract()[0]
        item['category'] = sel_intro.xpath('p/text()').extract()[1]
        item['support'] = sel_intro.xpath('p/text()').extract()[2]
        item['rating'] = sel_intro.xpath('div[@class="star1-empty"]/div/@class').extract_first()
        item['comments_number'] = sel_intro.xpath('span[@class="app-intro-comment"]/text()').extract_first()
        
        item['url'] = response.url
        
        sel_detail = response.xpath('//ul[@class = " cf"]/li/text()')
        item['size'] = sel_detail.extract()[1]
        item['version'] = sel_detail.extract()[3]
        item['updated_at'] = sel_detail.extract()[5]

        item['root'] = response.xpath('//ul[@class="second-ul"]/li/text()').extract()
        item['intro'] = response.xpath('//p[@class="pslide"]/text()').extract()
        yield item
    # def parse(self,response):
    # 	for sel in response.xpath('//ul[@class="applist"]/li/h5/a'):
    # 		item = XiaomiItem()
    # 		name = sel.xpath('text()').extract()[0]
    # 		relative_url = sel.xpath('@href').extract()[0]
    # 		url = response.urljoin(relative_url)
    # 		item['name'] = name
    # 		item['url'] = url
    # 		# print name

    # 		yield item

    	# for href in response.xpath(''):
    	# 	url = response.urljoin(href.extract())
    	# 	yield scrapy.Request(url,callback=self.parse_app_details)
    
    # def parse_app_details(self,response):
    	# pass
    	# for sel in response.xpath(''):
    	# 	item = XiaomiItem()
    	# 	item['name'] = sel.xpath('').extract()
    	# 	yield item

    # def parse_articles_follow_next_page(self,response):
    # 	pass
    	# for article in response.xpath('//article'):
    	# 	item = ArticleItem()
    	# 	...extract something 
    	# 	yield item

    	# next_page = response.css('')
    	# if next_page:
    	# 	url = response.urljoin(next_page[0].extract())
    	# 	yield scrapy.Request(url,self.parse_articles_follow_next_page)
