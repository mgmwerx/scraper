# Written by Dennis Brown. Curse his name when you have to maintain this fine piece of
# software artistry in the future.

from bs4 import BeautifulSoup
import json
import ast
import scrapy
from scraper.items import ScraperItem

class eventbriteHelper():
    # I can't get any LD+JSON parser to work in Python so resort to parsing with AST
    def bruteForceParseEvent(event):
#        print("!!!!!! ", str(event))
        eventDict = ast.literal_eval(str(event))
        item = ScraperItem()
        item['title'] = eventDict['name']
        item['uri'] = eventDict['url']
        item['description'] = eventDict['description']
        item['starts_at'] = eventDict['startDate'] + "T00:00"
        item['ends_at'] = eventDict['endDate'] + "T00:00"
        if "location" in eventDict:
#            print("======== ", eventDict['location'])
            locationDict = ast.literal_eval(str(eventDict['location']))
            if "name" in locationDict:
                item['location_name'] = locationDict['name']
            if "address" in locationDict:
                addressDict = ast.literal_eval(str(locationDict['address']))
                if "streetAddress" in addressDict:
                    item['location_street1'] = addressDict['streetAddress']
                if "addressLocality" in addressDict:
                    item['location_city'] = addressDict['addressLocality']
                if "addressRegion" in addressDict:
                    item['location_state'] = addressDict['addressRegion']
                if "postalCode" in addressDict:
                    item['location_zip'] = addressDict['postalCode']

        return item

class eventbriteSpider(scrapy.Spider):
    name = "eventbrite-spider"

    # The allowed domain and the URLs where the spider should start crawling:
    allowed_domains = ["eventbrite.com"]
    start_urls = ['https://www.eventbrite.com/d/al--montgomery/events/']

    # Walk through the web page making broad assumptions about how the information
    # is organized and presented. Such is the nature of web scraping. Minimal error catching.
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        scripts = soup.find_all('script', {'type':'application/ld+json'})
        events = json.loads(scripts[0].string)
        for event in events:
            item = eventbriteHelper.bruteForceParseEvent(event)
            yield item
