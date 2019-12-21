# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # 地址
    location = scrapy.Field()
    # 区
    district = scrapy.Field()
    # 户型
    house_type = scrapy.Field()
    # 租赁方式
    lease_way = scrapy.Field()
    # 基本信息
    information = scrapy.Field()
    # 配套设施
    ancillary_facility = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 中介费
    agency_fee = scrapy.Field()
    # 页面的url
    url = scrapy.Field()
