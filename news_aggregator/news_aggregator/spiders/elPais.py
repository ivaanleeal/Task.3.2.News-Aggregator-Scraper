import scrapy


class ElpaisSpider(scrapy.Spider):
    name = "elPais"
    allowed_domains = ["elpais.com"]
    start_urls = ["https://elpais.com/"]

    def parse(self, response):
        pass
