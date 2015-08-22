#!/usr/bin/env python
# coding=utf-8

from crystal.spiders.scut import ScutSpider
from preprocesser import UrlPreprocesser
# scrapy api
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
#debug
from pudb import set_trace
#model
from model.db_config import DBSession
from model.seeds import Seed

db = DBSession()
configure_logging()
runner = CrawlerRunner()

seeds = db.query(Seed)
urlPreprocesser = UrlPreprocesser()
for seed in seeds:
    set_trace()
    urlPreprocesser.set_start_url(seed.start_url)
    urlPreprocesser.set_url_xpath(seed.url_xpath)
    urlPreprocesser.set_word(seed.word)
    urls = urlPreprocesser.get_filted_urls()

#@defer.inlineCallbacks
#def crawl():
    #yield runner.crawl(ScutSpider)
    #reactor.stop()

#crawl()
#reactor.run() # the script will block here until the last crawl call is finished
