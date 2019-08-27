# Written by Dennis Brown. Curse his name when you have to maintain this fine piece of
# software artistry in the future.

from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import scrapy
from scraper.items import ScraperItem

class visitingMontgomeryHelper():
    # Turn a "Visiting Montgomery" date into a Python date via fragile string parsing
    # with no error checking.
    def parseDateTimeString(dateTimeString, item):
        dateTimeString = dateTimeString.replace("<p>","")
        dateTimeString = dateTimeString.replace("</p>","")
        dateTimeString = dateTimeString.replace("<br/>","")
        dateTimeString = dateTimeString.strip()
        parts = dateTimeString.split(' – ')
        startsAtDate = datetime.strptime(parts[0], "%a., %b. %d, %Y, %I:%M%p")
        endsAtDate = datetime.strptime(parts[1], "%I:%M%p")
        endsAtDate = endsAtDate.replace(startsAtDate.year, startsAtDate.month, startsAtDate.day)
        item['starts_at'] = startsAtDateString = startsAtDate.strftime('%Y-%m-%dT%H:%M')
        item['ends_at'] = endsAtDateString = endsAtDate.strftime('%Y-%m-%dT%H:%M')
        return item

    # Turn a "Visiting Montgomery" address string into separate location fields.
    # Since there is such variety in how the addresses are entered, this is seldom
    # likely to produce complete information.
    def parseAddressString(addressString, item):
        item['location_name'] = addressString
        return item


class visitingMontgomerySpider(scrapy.Spider):
    name = "visitingMontgomery-spider"

    # The allowed domain and the URLs where the spider should start crawling:
    allowed_domains = ["visitingmontgomery.com"]
    start_urls = ['https://visitingmontgomery.com/calendar/']

    # Walk through the web page making broad assumptions about how the information
    # is organized and presented. Such is the nature of web scraping. Minimal error catching.
    def parse(self, response):
        baseUrl = "http://visitingmontgomery.com"
        soup = BeautifulSoup(response.text, 'lxml')

        # Parse the page and find the actual events, which hide their useful
        # details on deeper web pages
        possibleEvents = soup.find_all(href=True)
        for possibleEvent in possibleEvents:
            relativeUrl = possibleEvent.get('href')
            if "/event/" in relativeUrl:
                url = baseUrl + relativeUrl
                yield scrapy.Request(url, callback=self.parse_details)

    # Parse the details of an single-event webpage. fragileAF; no error checking.
    def parse_details(self, response):
        item = ScraperItem()
        soup = BeautifulSoup(response.text, 'lxml')
        usefulH2 = soup.find_all('h2')[1]
        
        # Event name
        item['title'] = usefulH2.string
        
        # Build the description from multiple paragraphs that may contain additional tags.
        leftPs = usefulH2.find_next_sibling('div', {'class':'att-detail-left-col'}).find_all('p')
        item['description'] = leftPs[0].text
        for thisP in leftPs[1:(len(leftPs) - 2)]:
            item['description'] = item['description'] + " " + thisP.text
        item['description'] = item['description'].replace("\xa0", " ")
        item['description'] = item['description'].replace("\n", " ")
        
        # Date and time
        item = visitingMontgomeryHelper.parseDateTimeString(leftPs[len(leftPs) - 2].text, item)
        
        # Address
        rightPs = usefulH2.find_next_sibling('div', {'class':'att-detail-right-col'}).find_all('p')
        item = visitingMontgomeryHelper.parseAddressString(rightPs[0].string, item)

        return item
