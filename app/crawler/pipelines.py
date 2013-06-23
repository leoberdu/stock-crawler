from datetime import datetime
import settings
import pymongo

from scrapy import log


class StockPipeline(object):
	def __init__(self):
		self.server = settings.MONGODB_SERVER
		self.port = settings.MONGODB_PORT
		self.db = settings.MONGODB_DB
		self.col = settings.MONGODB_COLLECTION
		connection = pymongo.Connection(self.server, self.port)
		db = connection[self.db]
		self.collection = db[self.col]

	def process_item(self, item, spider):
		n = self.collection.find_one({'ticker':item['ticker']})

		if n:
			if n['value'][-1] != item['value']:
				self.collection.update(n, { 
					'$push': {'value': item['value']},
					'$set': {'updated_at': datetime.now()}, 
				})
		else:
			self.collection.insert(dict(item))

		return item
