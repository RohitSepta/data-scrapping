# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

from scrapy_djangoitem import DjangoItem
from dataapp.models import ScrapingData

class ScrapingDataItem(DjangoItem):
    django_model = ScrapingData