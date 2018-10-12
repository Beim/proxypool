# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from proxypool.items import ProxyItem

class XicidailiSpider(scrapy.Spider):

    name = 'xicidaili'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    crawl_range = 3

    def start_requests(self):
        url_prefixs = [
            'http://www.xicidaili.com/nn/',
            'http://www.xicidaili.com/nt/',
            'http://www.xicidaili.com/wn/',
            'http://www.xicidaili.com/wt/',
        ]
        for url_prefix in url_prefixs:
            for i in range(self.crawl_range):
                url = url_prefix + str(i+1)
                yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        ip_list = soup.find('table', id='ip_list').find_all('tr')
        for i in range(len(ip_list) - 1):
            item = ProxyItem()
            idx = i + 1
            td_list = ip_list[idx].find_all('td')
            item['host'] = td_list[1].text
            item['port'] = td_list[2].text
            item['type'] = td_list[5].text
            yield item

