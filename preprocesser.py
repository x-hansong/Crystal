#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver

class UrlPreprocesser():

    """Use webdriver to get all lists of url needed"""

    def __init__(self, start_url, word = None):
        self.start_url = start_url
        self.word = word
        self.titles_urls = {}
        self.driver = webdriver.PhantomJS()

#    def __del__(self):
        #self.driver.close()

    def get_filted_urls(self):
        self.get_all_urls()
        self.filte_title()
        return self.titles_urls.values()

    def filte_title(self):
        """filte the url whose title doesn't match the word

        :returns: the filted list of url

        """
        #if word is None, it means no need to filte
        if self.word == None:
            return self.urls
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
        elements = self.driver.find_elements_by_xpath("//a[@style]")  
        for element in elements:
            self.titles_urls[element.text] = element.get_attribute('href')
            print element.text.encode('utf8')

        
            
    def nextpage(self, pre_page):
        """use webdriver to access the link of nextpage which may be a javascript function

        :returns: True if has nextpage
                  False if has not nextpage

        """
        nextpage = self.driver.find_element_by_link_text("下一页")
        try:
            nextpage.click()
            #if  the nextpage is the same as pre_page, then it's no more page
            if self.driver.page_source == pre_page:
                return False
            else:
                return True
        except Exception, e:
            return False

        
