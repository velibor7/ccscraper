# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DigitalcurrItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    name = scrapy.Field()
    symbol = scrapy.Field()
    market_cap = scrapy.Field()
    price = scrapy.Field()
    circulating_supply = scrapy.Field()
    volume_24h = scrapy.Field()


