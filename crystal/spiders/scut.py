# -*- coding: utf-8 -*-
from selenium import webdriver
from scrapy.spiders import Spider
from scrapy.selector import Selector

class ScutSpider(Spider):
    name = "scut"
    allowed_domains = ["scut.edu.cn"]
    start_urls = (
            'http://www2.scut.edu.cn/s/87/t/431/p/28/i/10/list.htm',
    )

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def __del__(self):
        self.driver.close()

    def parse(self, response):
        urls = self.getUrlList(response)


        
    def getUrlList(self, response):
        """get the list of url which we need
        
        :response: the source of page
        :returns: the list of url

        """
        sel = Selector(response)
        urls = sel.xpath('//a[@style]/@href').extract()
        titles = sel.xpath('//font/text()').extract()
        titles_urls = dict(zip(titles, urls))
        word = u'学术报告'
        for title in titles_urls.keys():
            if word not in title:
                del titles_urls[title]

        for title in titles_urls.keys():
            print title.encode('utf8'), titles_urls[title]

        return titles_urls.values()
        
    def nextpage(self, url):
        """use webdriver to access the link of nextpage which may be a javascript function

        :url: the url of the page
        :returns: the response of the nextpage

        """
        self.driver.get(response.url)
        nextpage = self.driver.find_element_by_link_text("下一页")
        try:
            nextpage.click()
            return self.driver.page_source
        except Exception, e:
            return None
        
