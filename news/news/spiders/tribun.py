import scrapy


class TribunSpider(scrapy.Spider):
    name = 'tribun'
    allowed_domains = ['tribunnews.com']
    start_urls = ['https://www.tribunnews.com/news']

    def parse(self, response):
        cont = response.css('.lsi')
 
        # Collecting title
        #jd = cont.css('.mt140')
        nama = cont.css('.ln24')
        #link = cont.css('.mt140')
        des = cont.css('.ln18')

        c=0



        # Combining the results
        for review in nama:
            yield{'Judul': ''.join(review.xpath('./text()').extract()),
                  'link': ''.join(review.xpath('./@href').extract()),
                  'deskripsi': ''.join(des[c].xpath("./text()").extract())
                     }
            c=c+1
