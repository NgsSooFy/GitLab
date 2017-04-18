# -*- coding: utf-8 -*-
import scrapy
import datetime

class CjrbSpider(scrapy.Spider):
    name = "cjrb"

    def start_requests(self):
        today = datetime.date.today()
        year = str(today.year)
        month = str(today.month).zfill(2)
        day = str(today.day).zfill(2)
        urls = [
                  'http://cjrb.cjn.cn/html/'+year+'-'+month+'/'+day+'/node_2.htm'
               ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        origin_url = response.url
        home = origin_url[0:origin_url.index('node')]
        for href in response.css('a[class=black]::attr(href)').extract():
            page_url = home + href.replace('./', '')
            yield scrapy.Request(url=page_url,callback=self.parse_page)

    def parse_page(self,response):
        origin_url = response.url
        home = origin_url[0:origin_url.index('node')]
        for href in response.css('td[class=black] a[href*=content]::attr(href)').extract():
            article_url = home + href
            yield scrapy.Request(url=article_url,callback=self.parse_article)

    def parse_article(self,response):
        pass
