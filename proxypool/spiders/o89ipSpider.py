# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from proxypool.items import ProxyItem

class O89ipSpider(scrapy.Spider):

    name = '89ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    crawl_range = 200

    def start_requests(self):
        for i in range(self.crawl_range):
            url = 'http://www.89ip.cn/index_%s.html' % str(i+1)
            print(url)
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        try:
            ip_list = soup.find('tbody').find_all('tr')
            for ip_info in ip_list:
                item = ProxyItem()
                item['host'] = ip_info.find_all('td')[0].text.strip()
                item['port'] = ip_info.find_all('td')[1].text.strip()
                item['type'] = 'HTTP'
                yield item
                item['type'] = 'HTTPS'
                yield item
        except:
            yield
