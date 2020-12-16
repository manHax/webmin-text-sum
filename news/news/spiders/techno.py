import scrapy


class TechnoSpider(scrapy.Spider):
    name = 'techno'
    allowed_domains = ['sindonews.com']
    start_urls = ['https://nasional.sindonews.com/']

    def parse(self, response):
        cont = response.css('.homelist-new')
 
        # Collecting title
        kat = cont.css('.homelist-channel')
        tgl = cont.css('.homelist-date')
        judul = cont.css('.homelist-title')
        desk = cont.css('.homelist-desc')
        c=0

        # Combining the results
        for review in kat:
            yield{'Kategori': ''.join(review.xpath('./text()').extract()),
                  'tgl': ''.join(tgl[c].xpath("./text()").extract()),
                  'Judul': ''.join(judul[c].xpath(".//text()").extract()),
                  'link': ''.join(judul[c].xpath(".//@href").extract()),
                  'deskripsi': ''.join(desk[c].xpath("./text()").extract())
                     }
            c=c+1
