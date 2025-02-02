# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SdsHotelScraperItem(scrapy.Item):
    hotel_name = scrapy.Field()
    image_url = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    booking_url = scrapy.Field()


class AgodaScraperItem(scrapy.Item):
    hotel_name = scrapy.Field()
    image_url = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    booking_url = scrapy.Field()