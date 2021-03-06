# Written by Dennis Brown. Curse his name when you have to maintain this fine piece of
# software artistry in the future.

from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import json
import ast
import scrapy
from scraper.items import ScraperItem

class gumptownMagazineHelper():
    # I can't get any LD+JSON parser to work in Python so resort to parsing with AST
    def bruteForceParseEvent(event):
#        print("!!!!!! ", str(event))
        eventDict = ast.literal_eval(str(event))
        item = ScraperItem()
        item['title'] = eventDict['name']
        item['uri'] = eventDict['url']
        item['description'] = eventDict['description']
        startsAtDate = datetime.strptime(eventDict['startDate'], "%Y-%m-%dT%H:%M:%S+00:00")
        item['starts_at'] = datetime.strftime(startsAtDate, "%Y-%m-%dT%H:%M")
        endsAtDate = datetime.strptime(eventDict['endDate'], "%Y-%m-%dT%H:%M:%S+00:00")
        item['ends_at'] = datetime.strftime(endsAtDate, "%Y-%m-%dT%H:%M")
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

class gumptownMagazineSpider(scrapy.Spider):
    name = "gumptownMagazine-spider"

    # The allowed domain and the URLs where the spider should start crawling:
    allowed_domains = ["gumptownmag.com"]
    start_urls = ['https://gumptownmag.com/events/']

    # Walk through the web page making broad assumptions about how the information
    # is organized and presented. Such is the nature of web scraping. Minimal error catching.
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        scripts = soup.find_all('script', {'type':'application/ld+json'})
        events = json.loads(scripts[1].string)
        for event in events:
            item = gumptownMagazineHelper.bruteForceParseEvent(event)
            yield item
