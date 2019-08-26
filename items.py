# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    categories = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    uri = scrapy.Field()
    starts_at = scrapy.Field()
    ends_at = scrapy.Field()
    location-name = scrapy.Field()
    location-street1 = scrapy.Field()
    location-street2 = scrapy.Field()
    location-city = scrapy.Field()
    location-state = scrapy.Field()
    location-zip = scrapy.Field()
    pass
