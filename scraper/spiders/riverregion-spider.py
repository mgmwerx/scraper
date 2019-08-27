# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class RiverRegionSpider(CrawlSpider):
    name = 'riverregion-spider'
    allowed_domains = ['readjourneymagazine.com']
    start_urls = ['http://readjourneymagazine.com/index.php?option=com_k2&view=item&layout=item&id=222&Itemid=119']

    def parse(self, response):
        for div in response.xpath('//p'):
            item = {}
            title = div.xpath('.//font/b/text()').get()
            if (title is not None):
                title = title.strip()
                item['title'] = title
            description = div.xpath('.//font/text()').get()
            item['description'] = description
            if(title is not None and title == "AGLOW International"):
                item['starts_at'] = "3rd Thurs each month"
            #item['url'] = div.xpath('.//div/div/a/@href').get()
            #item['starts_at'] = div.xpath('.//div/div[@class="mn-date"]/div/span/@content').get()
            #item['ends_at'] = div.xpath('.//div/div[@class="mn-date"]/div/meta/@content').get()
            #item['categories'] = div.xpath('.//div/div/div[@class="mn-category"]/text()').get()
            #TODO: follow read more link to get details
            #yield scrapy.Request(item['url'], callback=self.parse_details)
            if (title is not None and description is not None):
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
