#!/usr/bin/env python
# coding=utf-8

from crystal.spiders.spider import CommonSpider
from preprocesser import UrlPreprocesser
# scrapy api
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
#debug
from ipdb import set_trace
import crash_on_ipy
#model
from model.db_config import DBSession
from model.seeds import Seed
from model.notifications import Notification

#use settings.py
process = CrawlerProcess(get_project_settings())

db = DBSession()

seeds = db.query(Seed)
urlPreprocesser = UrlPreprocesser()

def get_existed_urls(seed):
    urls = db.query(Notification.url).filter(Notification.college == seed.college).all()
    existed_urls = []
    for url in urls:
        existed_urls.append(url[0])
    return existed_urls

for seed in seeds:
    existed_urls = get_existed_urls(seed)
    #set_trace()
    urlPreprocesser.set_start_url(seed.start_url)
    urlPreprocesser.set_url_xpath(seed.url_xpath)
    urlPreprocesser.set_word(seed.word)
    urlPreprocesser.set_existed_urls(existed_urls)
    urls = urlPreprocesser.get_filted_urls()
    #set_trace()
    process.crawl(CommonSpider, seed, urls)

process.start()


