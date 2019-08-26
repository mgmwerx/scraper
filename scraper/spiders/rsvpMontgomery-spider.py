from bs4 import BeautifulSoup
import scrapy
from items import ScraperItem

class rsvpMontgomeryHelper():
    # Given a date and time IN THE SPECIFIC FORMAT USED BY RSVP MONTGOMERY,
    # return a standard date/time for start and end of the event.
    # NOT WORKING YET
    def fix(date, time):
        starts_at = date + " WRONG"
        ends_at = time + " WRONG"
        return starts_at, ends_at

class rsvpMontgomerySpider(scrapy.Spider):
    name = "rsvpMontgomery-spider"
    
    # The allowed domain and the URLs where the spider should start crawling:
    allowed_domains = ["rsvp-montgomery.com"]
    start_urls = ['http://www.rsvp-montgomery.com/events']

    # Walk through the web page making broad assumptions about how the information
    # is organized and presented. Such is the nature of web scraping. Minimal error catching.
    def parse(self, response):
        baseUrl = "http://www.rsvp-montgomery.com"
        soup = BeautifulSoup(response.text, 'lxml')

        # Iterate through tables containing events but skip the first table,
        # which does not contain events.
        tables = soup.find_all('table')
        if len(tables) < 2:
            return
        for table in tables[1:]:
            item = ScraperItem()
            # Look for headers for event title and URL. Give up if none.
            h3 = table.find('h3')
            if h3 is None:
                break
            item['title'] = h3.string
            item['uri'] = baseUrl + h3.find('a').get('href')
            # Paragraphs following headers contain date, time, description
            paragraphs = table.find_all('p')
            if len(paragraphs) < 2:
                return
            dateTimeLocation = paragraphs[1].string.split(' | ')
            if len(dateTimeLocation) < 3:
                return
            # Get "starts at" and "ends at" values from the date and time
            item['starts_at'], item['ends_at'] = rsvpMontgomeryHelper.fix(dateTimeLocation[0], dateTimeLocation[1])
            item['location_name'] = dateTimeLocation[2]
            item['description'] = paragraphs[2].string
            #print("======= ITEM START ===========")
            #print(item)
            #print("======= ITEM END   ===========")
            yield item

