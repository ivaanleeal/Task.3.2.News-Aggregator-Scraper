import scrapy


class LavozgaliciaSpider(scrapy.Spider):
    name = "laVozGalicia"
    allowed_domains = ["www.lavozdegalicia.es"]
    start_urls = ["https://www.lavozdegalicia.es/"]

    def parse(self, response):
        pass
