# -*- coding: utf-8 -*-
import scrapy
import json
import re
import requests



from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LifeAtTheMaxSpider(CrawlSpider):
    name = 'lifeatthemax-spider'
    allowed_domains = ['www.lifeatthemax.us']
    start_urls = ['https://www.lifeatthemax.us/calendar/eventsbyweek']

    def parse(self, response):
        i = 0
        # print(response)
        for div in response.xpath('//a'):
            item = {}
            item = div.xpath('./@href').get()
            #print(item)
            eventurl =  "https://www.lifeatthemax.us/" + item
            yield scrapy.Request(eventurl, callback=self.parse_details)

    def parse_details(self, response):
        detail = {}
        detail['title'] = response.xpath('//div[@class="jev_evdt_title"]/text()').get()
        detail['summary'] = response.xpath('//div[@class="jev_evdt_summary"]/text()').get() 
        detail['location'] = response.xpath('//div[@class="jev_evdt_location"]/text()').get() 
        print(detail)
        print("------------------------")
        return detail
