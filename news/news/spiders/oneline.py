import scrapy


class TechnoSpider(scrapy.Spider):
    name = 'techno'
    allowed_domains = ['jawapos.com']
    start_urls = ['https://www.jawapos.com/nasional/hukum-kriminal/13/12/2020/rizieq-ditahan-wakil-ketua-mui-pertanyakan-keadilan-polisi/']

    def parse(self, response):
        cont = response.css('.content')
 
        # Collecting title
        kat = cont.css('p')
        c=0

        # Combining the results
        for review in cont:
            yield{'paragraph': ''.join(review.xpath('.//text()').extract()),
                     }
            c=c+1
