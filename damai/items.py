# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field
from damai.settings import KEY_WORD
class YanItem(Item):#在此处定义需要爬取的字段的名称，并且定义了数据库中集合的名字
    collection = KEY_WORD
    
    name = Field()
    showtime = Field()
    city = Field()
    actors = Field()
    page = Field()


