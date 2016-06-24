# import scrapy
# from xiaomi.items import XiaomiItem

# class HomeSpider(scrapy.Spider):
#     name = "single_page"
#     allowed_domains = ["mi.com"]
#     start_urls = ["http://app.mi.com/category/5#page=3"]

#     def parse(self,response):
#         hrefs = response.xpath('//ul[@id="all-applist"]/li/h5/a/@href')[0:3]      
#         for href in hrefs:
#             url = response.urljoin(href.extract())
#             yield scrapy.Request(url,callback=self.parse_app_details)


#     def parse_app_details(self,response):
#         item = XiaomiItem()
        
#         sel_intro = response.xpath('//div[@class="intro-titles"]')
#         item['name'] = sel_intro.xpath('h3/text()').extract_first()
#         item['company'] = sel_intro.xpath('p/text()').extract()[0]
#         item['category'] = sel_intro.xpath('p/text()').extract()[1]
#         item['support'] = sel_intro.xpath('p/text()').extract()[2]
#         item['rating'] = sel_intro.xpath('div[@class="star1-empty"]/div/@class').extract_first()
#         item['comments_number'] = sel_intro.xpath('span[@class="app-intro-comment"]/text()').extract_first()
        
#         item['url'] = response.url
        
#         sel_detail = response.xpath('//ul[@class = " cf"]/li/text()')
#         item['size'] = sel_detail.extract()[1]
#         item['version'] = sel_detail.extract()[3]
#         item['updated_at'] = sel_detail.extract()[5]

#         item['root'] = response.xpath('//ul[@class="second-ul"]/li/text()').extract()
#         item['intro'] = response.xpath('//p[@class="pslide"]/text()').extract()
#         yield item