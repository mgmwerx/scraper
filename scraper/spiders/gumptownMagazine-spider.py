from bs4 import BeautifulSoup
import json
import ast
import scrapy
from scraper.items import ScraperItem

class gumptownMagazineHelper():
    # I can't get any LD+JSON parser to work in Python so resort to parsing with AST
    def bruteForceParseEvent(event):
        eventDict = ast.literal_eval(event)
#        print("$$$$$$ ", eventDict)
        item = ScraperItem()
        item['title'] = eventDict['name']
        item['uri'] = eventDict['url']
        item['description'] = eventDict['description']
        item['starts_at'] = eventDict['startDate']
        item['ends_at'] = eventDict['endDate']
#        if "location" in eventDict:
#            locationDict = ast.literal_eval(eventDict['location'])
#            item['location_name'] = str(locationDict)
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
            event = str(event)
            item = gumptownMagazineHelper.bruteForceParseEvent(event)
            yield item
