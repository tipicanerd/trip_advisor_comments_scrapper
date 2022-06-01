# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    comment = scrapy.Field()
    score = scrapy.Field()
    stars = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    quality_price = scrapy.Field()
    url = scrapy.Field()
    pass
