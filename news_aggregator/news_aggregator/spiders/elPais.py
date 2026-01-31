import scrapy


class ElpaisSpider(scrapy.Spider):
    name = "elPais"
    allowed_domains = ["elpais.com"]
    start_urls = ["https://elpais.com/"]

    def parse(self, response):
        title = response.css('title::text').get()
        fecha = response.css('header div time span::text').getall()
        autor = response.css('main div section article div a::text').get()
        noticia = response.css('main div section div article header h2 a::text').get()
        url_actual = response.url
        
        datos= [t.strip() for t in fecha if t.strip()]
        
        hora= datos[3]
        dia= datos[5]
        
        autores= [n.strip() for n in autor.split("/") if n.strip()]
        
        print(f'Fuente: {url_actual}')
        print(f'Título: {title}')
        print(f'Fecha: {hora, dia}')
        print(f'Autor: {autores}')
        print(f'Noticia: {noticia}')
        
        yield {
            'Fuente': url_actual
        }
        
        yield {
            'Título': title
        }

        yield {
            'Fecha': [hora, dia ]
        }
        
        yield {
            'Autor': autores
        }
        
        yield {
            'Noticia': noticia
        }
