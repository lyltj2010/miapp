# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
class DataCleanPipeline(object):
	def process_item(self,item,spider):
		item['comments_number'] = item['comments_number'].strip('()')
		return item


class MongoPipeline(object):

	def __init__(self):
		connection = pymongo.MongoClient(
			settings["MONGODB_SERVER"],
			settings["MONGODB_PORT"]
			)
		db = connection[settings["MONGODB_DB"]]
		self.collection = db[settings["MONGODB_COLLECTION"]]

	def process_item(self,item,spider):
		self.collection.insert(dict(item))
		log.msg("App info added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
		return item



# class DuplicatesPipeline(object):
# 	def __init__(self):
# 		self.names_seen = set()

# 	def process_item(self,item,spider):
# 		if item['name'] in self.names_seen:
# 			raise DropItem("Duplicated item found: %s" % item['name'])
# 		else:
# 			self.names_seen.add(item['name'])
# 			return item