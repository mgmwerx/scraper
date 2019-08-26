# -*- coding: utf-8 -*-
import scrapy
import json
import re

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LifeAtTheMaxSpider(CrawlSpider):
    name = 'lifeatthemax-spider'
    allowed_domains = ['www.lifeatthemax.us']
    start_urls = ['https://www.lifeatthemax.us/calendar/eventsbyweek']

    def parse(self, response):
        i = 0
        for div in response.xpath('//li'):
            item = {}
            #item = div.xpath('.//a')
            print(div)
            # Parse String from day time -
            print("------------------------")
           
    def parse_details(self, response):
        detail = {}
        #print(detail)
        
        return detail
