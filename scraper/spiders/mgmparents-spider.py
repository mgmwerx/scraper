# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class MgmParentsSpider(CrawlSpider):
    name = 'mgmparents-spider'
    allowed_domains = ['montgomeryparents.com']
    start_urls = ['http://montgomeryparents.com/index.php/family-calendar']

    def parse(self, response):
        for div in response.xpath('//div[contains(@class, "ai1ec-event-summary ai1ec-expanded")]'):
            item = {}
            item['title'] = div.xpath('.//a/div/img/@alt').get()
            item['url'] = div.xpath('.//a/@href').get()
            item['description'] = div.xpath('.//p/text()').get()

            #Get start and end date and convert to standard date format
            dateStr = div.xpath('.//preceding-sibling::div/div[contains(@class, "ai1ec-event-time")]/text()').get().strip()
            dateArray = dateStr.split("@")
            Date = dateArray[0].strip()
            TimeArray = dateArray[1].split("\u2013")
            startTime = TimeArray[0].strip()
            endTime = TimeArray[1].strip()
            today = datetime.today()
            year = today.year
            startDate = Date + ' ' + str(year) + ' ' + startTime #Aug 31 2019 3:30 pm
            endDate = Date + ' ' + str(year) + ' ' + endTime
            #TODO: convert to date object
            #startDatetimeFmt = datetime.parse('%b %d %y %I:%M %p')
            #endDatetimeFmt = datetime.parse('%b %d %y %I:%M %p')
            #TODO: convert to standard date format
            #%y-%m-%dT%H:%M # 2019-09-10T18:00
            startDateFmt = startDate
            endDateFmt = endDate

            item['starts_at'] = startDateFmt
            item['ends_at'] = endDateFmt
            item['categories'] = div.xpath('.//following-sibling::div/span/a/text()').get().strip()
            #TODO: follow read more link to get details
            #yield scrapy.Request(item['url'], callback=self.parse_details)
            yield item

    def parse_details(self, response):
        detail = {}
        #detail['location-name'] = response.xpath('')
        #detail['location-street1'] = response.xpath('')
        #detail['location-street2'] = response.xpath('')
        #detail['location-city'] = response.xpath('')
        #detail['location-state'] = response.xpath('')
        #detail['location-zip'] = response.xpath('')
        return detail
