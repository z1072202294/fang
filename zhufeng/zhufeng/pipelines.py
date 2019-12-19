# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from redis import Redis


class ZhufengPipeline(object):
    def process_item(self, item, spider):
        r = Redis(host='192.168.1.129')
        r.set('mess', item['mess'])
        return item
