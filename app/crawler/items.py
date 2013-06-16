# coding: utf-8
from scrapy.item import Item, Field

class StockItem(Item):
	title = Field()
	value = Field()
