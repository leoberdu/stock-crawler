BOT_NAME = 'stock-crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

ITEM_PIPELINES = [
    'crawler.pipelines.StockPipeline',
]

USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'stockdb'
MONGODB_COLLECTION = 'stock-collection'