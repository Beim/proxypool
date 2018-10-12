# -*- coding: utf-8 -*-
import requests
import logging

# logging.basicConfig(filename='%s/logs/logger.log' % os.getcwd(), level=logging.INFO)

def get_logger(name):
    logger_name = name
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    log_path = './logs/%s.log' % name
    fh = logging.FileHandler(log_path)
    # fh.setLevel(logging.WARN)
    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def test_alive(host, port, type):
    proxies = {}
    if type == 'HTTP' or type == 'http':
        proxies['http'] = '%s:%s' % (host, port)
    else:
        proxies['https'] = '%s:%s' % (host, port)
    try:
        res1 = requests.get('%s://www.baidu.com' % type, proxies=proxies, timeout=3)
        if not res1.status_code == 200: return False
        res2 = requests.get('%s://www.baidu.com' % type, proxies=proxies, timeout=3)
        return res2.status_code == 200
    except:
        return False

logger_v = get_logger('validateService')
logger_s = get_logger('spider')