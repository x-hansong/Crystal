# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
#model
from model.notifications import Notification
from model.db_config import DBSession
#debug
from ipdb import set_trace

class CrystalPipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        #set_trace()
        self.validate_item(item)
        notification = Notification(url=item['url'].encode('utf8'),
                title=item['title'].encode('utf8'),
                college=item['college'].encode('utf8'),
                speaker=item['speaker'].encode('utf8'),
                venue=item['venue'].encode('utf8'),
                time=item['time'].encode('utf8'),
                notify_time=item['notify_time'].encode('utf8'))
        #set_trace()
        self.session.add(notification)
        self.session.commit()
        
        return item

    def validate_item(self, item):
        if 'url' not in item:
            raise DropItem("Invalid item found: %s" % item)

        if 'title' not in item:
            item['title'] = ''

        if 'college' not in item:
            item['college'] = ''
            
        if 'speaker' not in item:
            item['speaker'] = ''
            
        if 'venue' not in item:
            item['venue'] = ''
            
        if 'time' not in item:
            item['time'] = ''
            
        if 'notify_time' not in item:
            item['notify_time'] = item['time']


    def close_spider(self, spider):
        self.session.close()
