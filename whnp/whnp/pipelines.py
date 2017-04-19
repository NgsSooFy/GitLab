# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime

class WhnpPipeline(object):
    def process_item(self, item, spider):
        return item

class CJRBPipeline(object):
    def open_spider(self,spider):
        fname = str(datetime.date.today()).replace('-','')+'.txt'
        self.f = open(fname,'w')

    def close_spider(self,spider):
        self.f.close()

    def process_item(self,item,spider):
        res = dict(item)
        self.f.write("\n")
        self.f.write("\n")
        self.f.write("正标题："+res['Main_title']+"\n")
        self.f.write("副标题："+res['Second_title']+"\n")
        self.f.write("版面："+res['Sheet']+"\n")
        self.f.write("版次："+res['Sheet_number']+"\n")
        self.f.write("正文：\n")
        self.f.write(res['Article'])
        
