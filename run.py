#!/usr/bin/env python
# coding=utf-8

from crystal.spiders.scut import ScutSpider
# scrapy api
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(ScutSpider)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished
