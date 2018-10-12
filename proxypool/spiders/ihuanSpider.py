# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from proxypool.items import ProxyItem

class IhuanSpider(scrapy.Spider):

    name = 'ihuan'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    main_url = 'https://ip.ihuan.me/address/5Lit5Zu9.html'
    crawl_range = 30

    def start_requests(self):
        yield scrapy.Request(self.main_url, headers=self.headers)

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        ip_list = soup.find('tbody').find_all('tr')
        for ip_info in ip_list:
            item = ProxyItem()
            td_list = ip_info.find_all('td')
            item['host'] = td_list[0].find('a').text.strip()
            item['port'] = td_list[1].text.strip()
            if td_list[4].text.strip() == '支持':
                item['type'] = 'HTTPS'
            else:
                item['type'] = 'HTTP'
            yield item

            # 递归爬取下一页
            curr_idx = int(soup.find('ul', class_='pagination').find_all('a')[-2].text.strip())
            if (curr_idx) < self.crawl_range:
                q = soup.find('ul', class_='pagination').find_all('a')[-1]['href']
                yield scrapy.Request('%s%s' % (self.main_url, q), headers=self.headers, callback=self.parse)

