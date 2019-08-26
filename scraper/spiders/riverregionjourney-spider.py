# -*- coding: utf-8 -*-
import scrapy
import json
import re

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
              match = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', tmp)
              phonenumbers = {}
              for phone in match:
                phonenumbers['phone'] =  phone
              item['phone'] = phonenumbers
              print(item)

              # Parse String from day time -
              
              print("------------------------")
           
    def parse_details(self, response):
        detail = {}
        #print(detail)
        
        return detail
