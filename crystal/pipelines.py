# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrystalPipeline(object):
    words_to_filter = ['学术报告','讲座']
    def process_item(self, item, spider):
        return item
