import scrapy


class MarcaSpider(scrapy.Spider):
    name = "marca"
    allowed_domains = ["www.marca.com"]
    start_urls = ["https://www.marca.com/"]

    def parse(self, response):
        pass
