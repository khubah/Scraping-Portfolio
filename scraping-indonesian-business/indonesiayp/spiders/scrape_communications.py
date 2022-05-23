import scrapy


class ScrapeCommunicationsSpider(scrapy.Spider):
    name = 'scrape_communications'
    allowed_domains = ['www.indonesiayp.com']
    start_urls = ['https://www.indonesiayp.com/category/communications']
    base_url = 'https://www.indonesiayp.com'

    def parse(self, response):
        links = response.xpath('//h4/a/@href').extract()
        for link in links :
            url = self.base_url + link
            yield scrapy.Request(url, callback=self.parse_detail)

        next_part_url = response.xpath('//a[@rel="next"]/@href').extract_first()
        next_url = self.base_url + next_part_url
        yield scrapy.Request(next_url, callback=self.parse)
    def parse_detail(self, response):
        company_name = response.xpath('//b[@id="company_name"]/text()').extract_first()
        address = response.xpath('//div[@class="text location"]/text()').extract_first()
        city = response.xpath('//div[@class="text location"]/a/text()').extract_first()
        phone = response.xpath('//div[@class="text phone"]/text()').extract_first()
        website = response.xpath('//div[@class="text weblinks"]/a/text()').extract_first()

        yield{
            'Company Name' : company_name,
            'Address' : address,
            'City' : city,
            'Phone' : phone,
            'Website' : website
        }