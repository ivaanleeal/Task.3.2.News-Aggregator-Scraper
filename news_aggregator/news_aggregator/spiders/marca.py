import scrapy


class MarcaSpider(scrapy.Spider):
    name = "marca"
    allowed_domains = ["www.marca.com"]
    start_urls = ["https://www.marca.com/"]

    def parse(self, response):
        title = response.xpath('//title/text()').get()
        autor = response.xpath("//span[@class='ue-c-cover-content__byline-name']/text()").get()
        noticia = response.xpath('//main//div//header//a//h2/text()').get()
        dato = response.xpath("//li[@class='ue-c-cover-content__related-link']/a/span/text()").get()
        url_actual = response.url
        
        autores= [n.strip() for n in autor.split("/") if n.strip()]

        datoLimpio= [n.strip() for n in dato.split("/") if n.strip()]
        
        print(f'Fuente: {url_actual}')
        print(f'Título: {title}')
        print(f'Autor: {autores}')
        print(f'Noticia: {noticia}')
        print(f'Dato: {datoLimpio}')
        
        yield {
            'Fuente': url_actual
        }
        
        yield {
            'Título': title
        }

        yield {
            'Autor': autores
        }
        
        yield {
            'Noticia': noticia
        }
        
        yield {
            'Dato': datoLimpio
        }