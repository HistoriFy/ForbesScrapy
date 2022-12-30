# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class ForbesItem(scrapy.Item):

    a= scrapy.Field()
    Rank = scrapy.Field()
    Name = scrapy.Field()
    Industries = scrapy.Field()
    Country = scrapy.Field()
    Employees = scrapy.Field()
    Link = scrapy.Field()


class CompanyItem(scrapy.Item):
    b= scrapy.Field()
    Name = scrapy.Field()
    Founded = scrapy.Field()
    Revenue_2022 = scrapy.Field()
    Revenue_2021 = scrapy.Field()
    Assets_2022 = scrapy.Field()
    Assets_2021 = scrapy.Field()
    Profits_2022 = scrapy.Field()
    Profits_2022 = scrapy.Field()



