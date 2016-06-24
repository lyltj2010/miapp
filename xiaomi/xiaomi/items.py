# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class XiaomiItem(scrapy.Item):
    name = scrapy.Field()
    company = scrapy.Field()
    category = scrapy.Field()
    rating = scrapy.Field()
    comments_number = scrapy.Field()
    root = scrapy.Field()
    support = scrapy.Field()
    size = scrapy.Field()
    version = scrapy.Field()
    updated_at = scrapy.Field()
    url = scrapy.Field()
    intro = scrapy.Field()