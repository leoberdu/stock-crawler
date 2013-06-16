# coding: utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from crawler.items import StockItem


class StockSpider(BaseSpider):
	name = 'stock'
	allowed_domains = ['br.financas.yahoo.com']
	start_urls = [
		'http://br.financas.yahoo.com/q?s=GOOG',
		'http://br.financas.yahoo.com/q?s=AAPL',
		'http://br.financas.yahoo.com/q?s=FB',
	]

	def parse(self, response):
		self.log('URL: %s' % response.url)

		hxs = HtmlXPathSelector(response)
		item = StockItem()
		item['title'] = hxs.select('//*[@id="yfi_rt_quote_summary"]/div[1]/div/h2/text()').extract()
		item['value'] = hxs.select('//*[@id="yfi_rt_quote_summary"]/div[2]/p/span[1]/span/text()').extract()
		return item
