# -*- coding: utf-8 -*-
import copy
import re
from scrapy.spiders import Spider
from scrapy.selector import Selector
from crystal.items import Notification

class CommonSpider(Spider):
    name = "common"
    start_urls = (
            'http://www2.scut.edu.cn/s/87/t/431/cb/4d/info117581.htm',
    )
    

    def __init__(self):
        self.words = {'title':u'报告题目：', 'speaker':u'报 告 人:', 'time':u'报告时间：', 'venue':u'报告地点：'}
        pass


    def parse(self, response):
        notification = Notification()
        texts = []
        #get all the lines
        lines = response.xpath("//*[@id='infocontent']/p")
        for line in lines:
            #the list of text
            ls = line.xpath('.//text()').extract()
            #join the item of list to a string and append to texts
            texts.append("".join(ls)) 
        #parse the text to notification fields:title, speaker, venue, time
        for text in texts:
            print text.encode('utf8')
            for (k, v) in self.words.items():
                if v in text:
                    notification[k] = text

        #use re.match to parse the notify_time
        notification['notify_time'] = None
        for text in texts:
            if re.match()
                    
        for (k, v) in words.items():
            print notification[k].encode('utf8')

        


