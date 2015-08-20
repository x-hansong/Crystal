#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver

class UrlPreprocesser():

    """Use webdriver to get all lists of url needed"""

    def __init__(self):
        self.start_url = ''
        self.urls = []
        self.driver = webdriver.PhantomJS()

    def __del__(self):
        self.driver.close()

    def getUrlList(self, url):
        """get the list of url which we need
        
        :url: the url where webdriver start
        :returns: the list of url

        """

        self.driver.get(url)
        elements = driver.find_elements_by_xpath("//a[@style]")  
        for element in elements:
            titles_urls[element.text] = element.get_attribute('href')
            
        word = u'学术报告'
        for title in titles_urls.keys():
            if word not in title:
                del titles_urls[title]

        for title in titles_urls.keys():
            print title.encode('utf8'), titles_urls[title]
 
        return titles_urls.values()

        
