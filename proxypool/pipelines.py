# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from proxypool.util import test_alive
from proxypool.db.db import dbCursor
from proxypool.util import logger_s

class ProxypoolPipeline(object):
    def process_item(self, item, spider):
        if test_alive(item['host'], item['port'], item['type']):
            dbCursor.insert(['insert into proxy(host, port, type, platform) values ("%s", "%s", "%s", "%s")' %
                            (item['host'], item['port'], item['type'], spider.name)])
        return item
