# Written by Dennis Brown. Curse his name when you have to maintain this fine piece of
# software artistry in the future.

from bs4 import BeautifulSoup
import json
import ast
import scrapy
from scraper.items import ScraperItem

class knowTheCommunityHelper():
    # I can't get any LD+JSON parser to work in Python so resort to parsing with AST
    def bruteForceParseEvent(event):
#        print("!!!!!! ", str(event))
        eventDict = ast.literal_eval(str(event))
        item = ScraperItem()
        item['title'] = eventDict['name']
        item['uri'] = eventDict['url']
        item['description'] = eventDict['description']
        item['starts_at'] = eventDict['startDate']
        item['ends_at'] = eventDict['endDate']
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

class knowTheCommunitySpider(scrapy.Spider):
    name = "knowTheCommunity-spider"

    # The allowed domain and the URLs where the spider should start crawling:
    allowed_domains = ["knowthecommunity.com"]
    start_urls = ['http://knowthecommunity.com/explore-calendar/']

    # Walk through the web page making broad assumptions about how the information
    # is organized and presented. Such is the nature of web scraping. Minimal error catching.
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        scripts = soup.find_all('script', {'type':'application/ld+json'})
        events = json.loads(scripts[1].string)
        for event in events:
            item = knowTheCommunityHelper.bruteForceParseEvent(event)
            yield item
