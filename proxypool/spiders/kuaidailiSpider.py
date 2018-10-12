# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from proxypool.items import ProxyItem

class KuaidailiSpider(scrapy.Spider):

    name = 'kuaidaili'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    crawl_range = 3

    def start_requests(self):
        url_prefixs = [
            'https://www.kuaidaili.com/free/inha/',
            'https://www.kuaidaili.com/free/intr/'
        ]
        for url_prefix in url_prefixs:
            for i in range(self.crawl_range):
                url = url_prefix + str(i+1)
                yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        ip_list = soup.find('div', id='list').find_all('tr')
        for i in range(len(ip_list) - 1):
            item = ProxyItem()
            idx = i + 1
            tr = ip_list[idx]
            item['host'] = tr.find('td', {'data-title': 'IP'}).text.strip()
            item['port'] = tr.find('td', {'data-title': 'PORT'}).text.strip()
            item['type'] = tr.find('td', {'data-title': '类型'}).text.strip()
            yield item

