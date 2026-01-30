import scrapy


class LavozgaliciaSpider(scrapy.Spider):
    name = "laVozGalicia"
    allowed_domains = ["www.lavozdegalicia.es"]
    start_urls = ["https://www.lavozdegalicia.es/"]

    def parse(self, response):
        title = response.xpath('//title/text()').get()
        autor = response.xpath('//section//div//p//span//a/text()').get()
        noticia = response.xpath('//section//div//h4//a/text()').get()
        dato = response.xpath('//section//div//p//text()').get()
        url_actual = response.url

            
        autores= [n.strip() for n in autor.split("/") if n.strip()]
        
        print(f'Título: {url_actual}')
        print(f'Título: {title}')
        print(f'Autor: {autores}')
        print(f'Noticia: {noticia}')
        print(f'Datos: {dato}')
        
        
        yield {
            'Fuente': url_actual,
        }
        
        yield {
            'Título': title,
        }
        
        yield {
            'Autor': autores
        }
        
        yield {
            'Noticia': noticia
        }
        
        yield {
            'Dato': dato
        }
