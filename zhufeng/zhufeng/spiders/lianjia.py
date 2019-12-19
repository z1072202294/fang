# -*- coding: utf-8 -*-
import scrapy
from zhufeng.items import ZhufengItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://sh.lianjia.com/zufang/SH2410145002782474240.html']

    def parse(self, response):
        item = ZhufengItem()
        facility_list = ['电视', '冰箱', '洗衣机', '空调', '热水器', '床', '暖气', '宽带', '衣柜', '天然气']
        j = response.xpath('.//p[@class="content__title"]/text()').get().split(' ')
        infos = response.xpath(".//div[@id='info']//li/text()").getall()
        infojoin = ''
        for i in infos[1:]:
            if i:
                infojoin += i.strip() + ' '
        region = response.xpath(".//p[@class='bread__nav__wrapper oneline']//a/text()").getall()[1]
        lease = response.xpath(".//ul[@class='content__aside__list']//li/text()").get()
        price = response.xpath(".//div[@class='content__aside--title']//span/text()").get()
        agency_fee = response.xpath(".//ul[@class='table_row']//li/text()").getall()[-1]
        facility = response.css("ul.content__article__info2").css('li.facility_no::text').getall()
        for i in facility:
            if i.strip() in facility_list:
                facility_list.remove(i.strip())
        site = j[0]
        house_type = j[1]
        mess_dict = '{}#{}#{}#{}#{}#{}#{}#{}'.format(infojoin, region, lease, price, agency_fee, facility_list, site,
                                                     house_type)
        item['mess'] = mess_dict
        yield item
