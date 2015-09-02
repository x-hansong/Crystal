# -*- coding: utf-8 -*-
import copy
import re
from scrapy.spiders import Spider
from scrapy.selector import Selector
from crystal.items import Notification
#debug
from ipdb import set_trace
import crash_on_ipy

class CommonSpider(Spider):
    name = "common"

    def __init__(self, seed, urls):
        self.seed = seed
        self.words = {'title':seed.title, 'speaker':seed.speaker, 'time':seed.time, 'venue':seed.venue}
        self.start_urls = urls
        pass


    def parse(self, response):
        notification = Notification()
        texts = []
        #get all the lines
        lines = response.xpath(self.seed.text_xpath)
        for line in lines:
            #the list of text
            ls = line.xpath('.//text()').extract()
            #join the item of list to a string and append to texts
            texts.append("".join(ls)) 
        #parse the text to notification fields:title, speaker, venue, time
        for text in texts:
            print text.encode('utf8')
            text = text.replace(u'\xa0', u' ')
            for (k, v) in self.words.items():
                if v in text:
                    notification[k] = text
        #set_trace()
        #use re.match to parse the notify_time
        for text in texts:
            t = re.match(u'^(\d{4})年(\d+)月(\d+)日', text)
            if t is not None:
                 notification['notify_time'] = self.format_date(t)

        #format notification time
        tt = re.search(u'(\d{4})年(\d+)月(\d+)日.*?(\d+).+(\d+)', notification['time'])
        if tt is not None:
            notification['time'] = self.format_datetime(tt)

        #set college and url
        notification['college'] = self.seed.college
        notification['url'] = response.url
                    
#        for (k, v) in self.words.items():
            #print notification[k].encode('utf8')

        return notification

    def format_date(self, t):
        y = t.group(1)
        m = t.group(2)
        d = t.group(3)
        if len(m) == 1:
            m = '0' + m
        if len(d) == 1:
            d = '0' + d
        return y+'-'+m+'-'+d

    def format_datetime(self, t):
        date = self.format_date(t)
        h = t.group(4)
        m = t.group(5)
        s = '00'
        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        return date+' '+h+':'+m+':'+s
            
        


