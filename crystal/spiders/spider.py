# -*- coding: utf-8 -*-
import copy
import re
from scrapy.spiders import Spider
from scrapy.selector import Selector
from crystal.items import Notification
#debug
from pdb import set_trace

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
        lines = response.xpath(self.seed.url_xpath)
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
                    print text.encode('utf8')
        set_trace()
        #use re.match to parse the notify_time
        notification['notify_time'] = None
        for text in texts:
            t = re.match('^(\d{4})年(\d+)月(\d+)日', text)
            if t is not None:
                 notification['notify_time'] = self.format_date(t)
        print notification['notify_time']

        #format notification time
        tt = re.search('(\d{4})年(\d+)月(\d+)日.*?(\d+).(\d+)', notification['time'])
        if tt is not None:
            notification['time'] = self.format_datetime(tt)
        print notification['time']

                    
        for (k, v) in self.words.items():
            print notification[k].encode('utf8')

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
            
        


