# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MgmchamberSpider(CrawlSpider):
    name = 'mgmchamber-spider'
    allowed_domains = ['montgomerychamber.com']
    start_urls = ['https://www.montgomerychamber.com/events']

    def parse(self, response):
#        for div in response.xpath('//div[@id="mn-events-listings"]').getall():
        i = 0
        for div in response.xpath('//div[@itemscope]'):
            item = {}
            item['title'] = div.xpath('.//div/div/a/text()').get()
            item['url'] = div.xpath('.//div/div/a/@href').get()
            item['starts_at'] = div.xpath('.//div/div[@class="mn-date"]/div/span/@content').get()
            item['ends_at'] = div.xpath('.//div/div[@class="mn-date"]/div/meta/@content').get()
            item['categories'] = div.xpath('.//div/div/div[@class="mn-category"]/text()').get()
            #TODO: follow read more link to get details
            #yield scrapy.Request(item['url'], callback=self.parse_details)
            yield item

    def parse_details(self, response):
        detail = {}
        #detail['description'] = response.xpath('')
        #detail['location-name'] = response.xpath('')
        #detail['location-street1'] = response.xpath('')
        #detail['location-street2'] = response.xpath('')
        #detail['location-city'] = response.xpath('')
        #detail['location-state'] = response.xpath('')
        #detail['location-zip'] = response.xpath('')
        return detail
