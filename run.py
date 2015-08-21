#!/usr/bin/env python
# coding=utf-8

from crystal.spiders.scut import ScutSpider
from preprocesser import UrlPreprocesser
# scrapy api
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

configure_logging()
runner = CrawlerRunner()

urlPreprocesser = UrlPreprocesser('http://www2.scut.edu.cn/s/87/t/431/p/28/i/10/list.htm',u'学术报告')
urlPreprocesser.get_filted_urls()

#@defer.inlineCallbacks
#def crawl():
    #yield runner.crawl(ScutSpider)
    #reactor.stop()

#crawl()
#reactor.run() # the script will block here until the last crawl call is finished
