# -*- coding: utf-8 -*-
from scrapy import cmdline
from proxypool.services.ValidateService import ValidateService
import threading
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
from multiprocessing import Process
from proxypool.util import logger_s

# project需要改为你的工程名字（即settings.py所在的目录名字）
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'proxypool.settings')


def start_crawl():
    process = CrawlerProcess(get_project_settings())
    spider_list = process.spider_loader.list()
    for spider_name in spider_list:
        process.crawl(spider_name)
    process.start()
# start_crawl()

if __name__ == '__main__':
    while True:
        p = Process(target=start_crawl)
        p.start()
        p.join()
        logger_s.info('sleep interval 60 * 10')
        time.sleep(60 * 10)




# name = 'xicidaili'
# name = 'kuaidaili'
# name = '89ip'
# name = 'ihuan'
# cmd = 'scrapy crawl {0}'.format(name)
# cmdline.execute(cmd.split())