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
    location_name = scrapy.Field()
    location_street1 = scrapy.Field()
    location_street2 = scrapy.Field()
    location_city = scrapy.Field()
    location_state = scrapy.Field()
    location_zip = scrapy.Field()
    pass
