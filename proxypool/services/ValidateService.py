# -*- coding: utf-8 -*-
from proxypool.db.db import dbCursor
from proxypool.util import test_alive
from proxypool.util import logger_s

class ValidateService(object):

    miss_max = 3

    def start(self):
        while True:
            num = dbCursor.query('select count(host) from proxy')[0][0]
            for i in range(0, num, 20):
                proxy_info_list = dbCursor.query('select host, port, type, miss from proxy limit %s, %s' % (i, 20))
                for proxy_info in proxy_info_list:
                    miss = proxy_info[3]
                    # miss
                    if not test_alive(proxy_info[0], proxy_info[1], proxy_info[2]):
                        miss = miss + 1
                        if miss > self.miss_max:
                            sql = 'delete from proxy where host="%s" and port="%s"' % (proxy_info[0], proxy_info[1])
                            logger_s.info('[miss] %s' % sql)
                            dbCursor.delete([sql])
                        else:
                            sql = 'update proxy set miss=%s where host="%s" and port="%s"' % (miss, proxy_info[0], proxy_info[1])
                            logger_s.info('[miss] %s' % sql)
                            dbCursor.update([sql])
                    # hit
                    else:
                        if miss > 0:
                            miss = miss - 1
                            sql = 'update proxy set miss=%s where host="%s" and port="%s"' % (miss, proxy_info[0], proxy_info[1])
                            # logger_s.info('[hit] %s' % sql)
                            dbCursor.update([sql])
                        # else:
                        #     logger_s.info('[hit]')



