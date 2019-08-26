from bs4 import BeautifulSoup
import scrapy
from items import ScraperItem

class rsvpMontgomerySpider(scrapy.Spider):
    name = "rsvpMontgomery-spider"
    
    # The allowed domain and the URLs where the spider should start crawling:
    allowed_domains = ["rsvp-montgomery.com"]
    start_urls = ['http://www.rsvp-montgomery.com/events']

    def parse(self, response):
        baseUrl = "http://www.rsvp-montgomery.com"
        soup = BeautifulSoup(response.text, 'lxml')
        tables = soup.find_all('table')
        for table in tables[1:]:
            item = ScraperItem()
            h3 = table.find('h3')
            if h3 is None:
                break
            item['title'] = h3.string
            item['uri'] = baseUrl + h3.find('a').get('href')
            paragraphs = table.find_all('p')
            dateTimeLocation = paragraphs[1].string.split(' | ')
            # The next two are wrong -- to be fixed
            item['starts_at'] = dateTimeLocation[0]
            item['ends_at'] = dateTimeLocation[1]
            item['location_name'] = dateTimeLocation[2]
            item['description'] = paragraphs[2].string
            
            #print("======= ITEM START ===========")
            #print(item)
            #print("======= ITEM END   ===========")

            yield item

