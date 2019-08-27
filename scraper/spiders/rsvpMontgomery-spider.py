# Written by Dennis Brown. Curse his name when you have to maintain this fine piece of
# software artistry in the future.

from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import scrapy
from scraper.items import ScraperItem

class rsvpMontgomeryHelper():
    # Given a date and time IN THE SPECIFIC FORMAT USED BY RSVP MONTGOMERY,
    # return a standard date/time for start and end of the event.
    # TIME NOT WORKING -- too much variety in the original source (9 am, 8 a.m., 5, 5pm,
    # various free text, etc...)
    def fix(uglyDate, uglyTime):
        startsAtDate = date.today()
        endAtDate = date.today()
        uglyDate = uglyDate + " " + str(date.today().year)
        uglyDate = uglyDate.replace("st", "")
        uglyDate = uglyDate.replace("nd", "")
        uglyDate = uglyDate.replace("rd", "")
        uglyDate = uglyDate.replace("th", "")
        try:
            startsAtDate = datetime.strptime(uglyDate, '%b %d %Y')
            endsAtDate = datetime.strptime(uglyDate, '%b %d %Y')
        except ValueError:
            return startsAtDate.strftime('%Y-%m-%dT%H:%M'), endsAtDate.strftime('%Y-%m-%dT%H:%M')
        startsAt = startsAtDate.strftime('%Y-%m-%dT%H:%M')
        endsAt = endsAtDate.strftime('%Y-%m-%dT%H:%M')
        return startsAt, endsAt

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
            # Add time to the front of the description because of the difficulty parsing it--
            # the user can read and interpret themselves.
            item['description'] = "TIME: " + dateTimeLocation[1] + " -- " + paragraphs[2].string
            #print("======= ITEM START ===========")
            #print(item)
            #print("======= ITEM END   ===========")
            yield item
