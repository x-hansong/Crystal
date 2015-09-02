#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
import sys

class UrlPreprocesser():

    """Use webdriver to get all lists of url needed"""

    def __init__(self):
        self.start_url = None
        self.url_xpath = None
        self.word = None
        self.existed_urls = None
        self.driver = webdriver.PhantomJS()

    def __del__(self):
        self.driver.close()

    def set_start_url(self, start_url):
        self.start_url = start_url

    def set_existed_urls(self, existed_urls):
        self.existed_urls = existed_urls

    def set_word(self, word):
        '''set word to match'''
        self.word = word

    def set_url_xpath(self, url_xpath):
        self.url_xpath = url_xpath

    def reset(self):
        self.urls = []
        self.titles_urls = {}
        self.times = 0
        assert self.start_url != None
        assert self.url_xpath != None

    def get_filted_urls(self):
        self.reset()
        self.get_all_urls()
        self.filte_title()
        self.filte_duplicated_url()
        return self.urls

    def filte_duplicated_url(self):
        """filte the url which has already in database"""
        for url in self.titles_urls.values():
            if url not in self.existed_urls:
                self.urls.append(url)


    def filte_title(self):
        """filte the url whose title doesn't match the word"""
        #if word is None, it means no need to filte
        #set_trace()
        if self.word == None:
            return;

        for title in self.titles_urls.keys():
            if self.word not in title:
                del self.titles_urls[title]

        for title in self.titles_urls.keys():
            print title.encode('utf8'), self.titles_urls[title]
 

    def get_all_urls(self):
        """get the list of url
        
        :url: the url where webdriver start
        :returns: the list of all url needed

        """
        self.driver.get(self.start_url)
        self.parse_url()
        while self.nextpage(self.driver.page_source):
            self.parse_url()

    def parse_url(self):
        if self.url_xpath == None:
            print 'please set_url_xpath first'
            sys.exit()
        elements = self.driver.find_elements_by_xpath(self.url_xpath)  
        for element in elements:
            self.titles_urls[element.text] = element.get_attribute('href')

            
    def nextpage(self, pre_page):
        """use webdriver to access the link of nextpage which may be a javascript function

        :returns: True if has nextpage
                  False if has not nextpage

        """
        try:
            nextpage = self.driver.find_element_by_link_text("下一页")
            nextpage.click()
            #if  the nextpage is the same as pre_page, then it's no more page 
            # crawl 10 pages at most
            if self.driver.page_source == pre_page or self.times < 10:
                return False
            else:
                self.times += 1
                return True
        except Exception, e:
            return False

        
