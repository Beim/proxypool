# -*- coding: utf-8 -*-
from scrapy import cmdline
from proxypool.services.ValidateService import ValidateService
import threading
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
# 必须先加载项目settings配置
# project需要改为你的工程名字（即settings.py所在的目录名字）
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'proxypool.settings')

class ValidateThread(threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.validateService = ValidateService()

    def run(self):
        self.validateService.start()


validateThread = ValidateThread(1, 'validateThread')
# validateThread.start()


def start_crawl():
    process = CrawlerProcess(get_project_settings())
    spider_list = process.spider_loader.list()
    for spider_name in spider_list:
        process.crawl(spider_name)
    process.start()
start_crawl()

while True:
    time.sleep(60 * 10)
    start_crawl()


# name = 'xicidaili'
# name = 'kuaidaili'
# name = '89ip'
# name = 'ihuan'
# cmd = 'scrapy crawl {0}'.format(name)
# cmdline.execute(cmd.split())