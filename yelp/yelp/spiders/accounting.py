import scrapy


class AccountingSpider(scrapy.Spider):
    name = 'accounting'
    allowed_domains = ['yelp.com']
    start_urls = ['http://yelp.com/']

    def parse(self, response):
        pass
