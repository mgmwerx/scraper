# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class RiverRegionJourneySpider(CrawlSpider):
    name = 'riverregionjourney-spider'
    allowed_domains = ['www.readjourneymagazine.com']
    start_urls = ['https://www.readjourneymagazine.com/index.php?option=com_k2&view=item&layout=item&id=222&Itemid=119']

    def parse(self, response):
        i = 0
        for div in response.xpath('//p'):
            item = {}
            tmp = div.xpath('.//font').get()
            if ( tmp is not None ):
              item['title'] = tmp
              print(item)

              # Parse String from day time -

              print("------------------------")

    def parse_details(self, response):
        detail = {}
        #print(detail)

        return detail
