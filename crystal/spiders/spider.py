# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from crystal.items import Notification

class CommonSpider(Spider):
    name = "common"
    start_urls = (
            'http://www2.scut.edu.cn/s/87/t/431/cb/4d/info117581.htm',
    )
    

    def __init__(self):
        pass


    def parse(self, response):
        notification = Notification()
        texts = []

        lines = response.xpath("//*[@id='infocontent']/p")
        for line in lines:
            #the list of text
            ls = line.xpath('.//text()').extract()
            #join the item of list to a string and append to texts
            texts.append("".join(ls)) 

        for text in texts:
            print text.encode('utf8')

        
    def parse_text(self, texts, notification):
        pass
