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
        main_title = response.css('td[class=bt1]::text').extract()[0]
        vice_title = ""
        for text in response.css('td[class=bt2]::text').extract():
            if text != "":
                vice_title = text
                break
        article = response.css('td[class=xilan_content_tt]::text').extract()[0]
        st = response.css('td[class=domain] span[class=bt3]::text').extract()[0]
        sheet = st[2:][:-3].strip()
        date = str(datetime.date.today()).replace('-','')
        result = { "Main_title":main_title , 'Second_title':vice_title , 'Date':date , 'Sheet':sheet , 'Article':article }
        yield result
                  
