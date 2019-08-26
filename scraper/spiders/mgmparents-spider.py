# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MgmParentsSpider(CrawlSpider):
    name = 'mgmparents-spider'
    allowed_domains = ['montgomeryparents.com']
    start_urls = ['http://montgomeryparents.com/index.php/family-calendar']

    def parse(self, response):
#        for div in response.xpath('//*[@id="ai1ec-calendar-view"]/div'):

        for div in response.xpath('//div[contains(@class, "ai1ec-event-description")]'):
            item = {}
            item['title'] = div.xpath('.//a/div/img/@alt').get()
            item['url'] = div.xpath('.//a/@href').get()
            item['description'] = div.xpath('.//p/text()').get()
            item['starts_at'] = div.xpath('.//preceding-sibling::div/div[contains(@class, "ai1ec-event-time")]/text()').get()
            #item['ends_at'] = div.xpath('.//div/div[@class="mn-date"]/div/meta/@content').get()
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
