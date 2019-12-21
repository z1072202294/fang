# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from lianjia.items import LianjiaItem


class ZufangSpider(RedisSpider):
    # class ZufangSpider(scrapy.Spider):
    name = 'zufang'
    allowed_domains = ['lianjia.com']
    # start_urls = ['https://bj.lianjia.com/zufang/pg1/#contentList', ]

    redis_key = 'fang:start_urls'

    def parse(self, response):  # 通过解析三个城市的页面得到每个区的 url
        city_url = response.url + '/'  # 前缀url(城市)
        # print('************************', city_url)
        # 区域 url
        district_urls = response.xpath(
            '//div[@class="filter__wrapper w1150"]/ul[2]/li[@class="filter__item--level2  "]/a/@href').getall()
        for url in district_urls:
            # 通过拼接城市和区域得到完整的 url, 传递给 parse_district 函数
            u = city_url.strip('/zufang/') + url
            yield scrapy.Request(url=u, callback=self.parse_district,
                                 meta={'city_url': city_url})

    def parse_district(self, response):  # 通过解析每个区的租房信息首页得到房源信息详情页url以及后续页面的url
        prefix_url = response.url  # 前缀 url(包括城市, 区域)
        city_url = response.meta['city_url']
        info_urls = response.css('div.content__list--item>a::attr(href)').getall()
        for info_url in info_urls:
            # print(prefix_url + info_url.strip('/zufang/'))
            # prefix_url + info_url.strip('/zufang/')  # 第一页房源信息详情页url
            url = city_url + info_url.strip('/zufang/')
            yield scrapy.Request(url=url, callback=self.info_parse)
        next_urls = response.css('div.content__pg+ul>li>a::attr(href)').getall()
        for next_url in next_urls:
            page_url = prefix_url + next_url[next_url.index('pg'):]  # 后续页面的 url, 通过yield传给 函数再次解析, 切片以避免url重复
            # print('---------------------0', page_url)
            yield scrapy.Request(url=page_url, callback=self.parse_page, meta={'city_url': city_url})

    def parse_page(self, response):
        # prefix_url = response.url  # 前缀 url(包括城市, 区域)
        city_url = response.meta.get('city_url')
        info_urls = response.css('div.content__list--item>a::attr(href)').getall()
        for info_url in info_urls:
            # print(prefix_url + info_url.strip('/zufang/'))
            # prefix_url + info_url.strip('/zufang/')  # 后续几页房源信息详情页url
            yield scrapy.Request(url=city_url + info_url.strip('/zufang/'), callback=self.info_parse)

    def info_parse(self, response):

        facility_list = ['电视', '冰箱', '洗衣机', '空调', '热水器', '床', '暖气', '宽带', '衣柜', '天然气']
        j = response.xpath('.//p[@class="content__title"]/text()').get().split(' ')
        infos = response.xpath(".//div[@id='info']//li/text()").getall()
        information = ''
        for i in infos[1:]:
            if i:
                information += i.strip() + ' '
        district = response.xpath(".//p[@class='bread__nav__wrapper oneline']//a/text()").getall()[1]
        lease_way = response.xpath(".//ul[@class='content__aside__list']//li/text()").get()
        price = response.xpath(".//div[@class='content__aside--title']//span/text()").get()
        agency_fee = response.xpath(".//ul[@class='table_row']//li/text()").getall()[-1]
        ancillary_facility = response.css("ul.content__article__info2").css('li.facility_no::text').getall()
        for i in ancillary_facility:
            if i.strip() in facility_list:
                facility_list.remove(i.strip())
        location = j[0].split('·')[1]
        house_type = j[1]
        # mess_dict = '{}#{}#{}#{}#{}#{}#{}#{}#{}'.format(infojoin, region[:-2], lease, price, agency_fee, facility_list,
        #                                                 site,
        #                                                 house_type, response.url)
        # print(mess_dict)
        item = LianjiaItem(location=location, district=district[:-2], house_type=house_type,
                           lease_way=lease_way, information=information, ancillary_facility=facility_list,
                           price=price, agency_fee=agency_fee, url=response.url)
        yield item
