#!/usr/bin/env python
# coding=utf-8

from crystal.spiders.spider import CommonSpider
from preprocesser import UrlPreprocesser
# scrapy api
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
#debug
from pdb import set_trace
#model
from model.db_config import DBSession
from model.seeds import Seed

settings = Settings()

# crawl settings
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
#settings.set("ITEM_PIPELINES" , {
    #'pipelines.DuplicatesPipeline': 200,
    ## 'pipelines.CountDropPipline': 100,
    #'pipelines.DataBasePipeline': 300,
#})

process = CrawlerProcess(settings)
db = DBSession()

seeds = db.query(Seed)
urlPreprocesser = UrlPreprocesser()
urls = ['http://www2.scut.edu.cn/s/87/t/431/cb/4d/info117581.htm']
for seed in seeds:
#    set_trace()
    urlPreprocesser.set_start_url(seed.start_url)
    urlPreprocesser.set_url_xpath(seed.url_xpath)
    urlPreprocesser.set_word(seed.word)
#    urls = urlPreprocesser.get_filted_urls()
    process.crawl(CommonSpider, seed, urls)
    process.start()


