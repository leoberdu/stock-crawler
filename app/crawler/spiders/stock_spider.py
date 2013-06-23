# coding: utf-8
import re

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from crawler.items import StockItem


class StockSpider(BaseSpider):
	name = 'stock'
	allowed_domains = ['br.financas.yahoo.com']
	start_urls = [
		'http://br.financas.yahoo.com/q?s=PETR4.SA',
		'http://br.financas.yahoo.com/q?s=OGXP3.SA',
		'http://br.financas.yahoo.com/q?s=VALE5.SA',
	]

	def parse(self, response):
		self.log('URL: %s' % response.url)

		hxs = HtmlXPathSelector(response)
		r = hxs.select('//*[@id="yfi_rt_quote_summary"]/div[1]/div/h2/text()').extract()
		r = re.match(r"(?P<key>.*) \((?P<value>.*[A-Z-0-9])", str(r)).groupdict()

		item = StockItem()
		item['title'] = r['key']
		item['ticker'] = r['value']
		item['value'] = hxs.select('//*[@id="yfi_rt_quote_summary"]/div[2]/p/span[1]/span/text()').extract()
		return item