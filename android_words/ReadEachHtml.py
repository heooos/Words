# -*- coding: UTF-8 -*-
# 依次访问所有的网页

import re
from collections import Counter

import requests as req
from bs4 import BeautifulSoup

import components.DBOperation as dbm
import components.MyLogger as log
import components.SQLTools as us

DATABASE_LIST_WORDS = "TEST_WORDS_TEST"
DATABASE_LIST_ERROR = "TEST_ERROR"

all_words = []
p = {
        'http': 'socks5://test:12345678@67.205.155.10:1080',
        'https': 'socks5://test:12345678@67.205.155.10:1080'
    }
logging = log.get_logger('ReadEachHtml')


def download(m_data):

    url = m_data[2]
    # 读取获取到的链接
    try:
        body = req.get(url, timeout=10, proxies=p)  # timeout=10, proxies=p
        bs_body = BeautifulSoup(body.text, 'lxml')
    except Exception, e:
        logging.error("访问异常,自动跳过本次访问")
        logging.error(e)
        sql = us.get_i_sql(DATABASE_LIST_ERROR, {'NAME': m_data[1], 'URL': m_data[2]})
        dbm.insert_data(sql)
        return

    # 获取当前页面中所有的正文文字
    try:
        html_txt = bs_body.find(class_="jd-descr ").get_text()
    except:
        logging.error("该页面样式有误,无法读取")
        return

    # 正则规则
    pat = '[a-zA-Z]{5,}'
    # 使用正则表达式，把单词提出出来，并都修改为小写格式
    words = re.findall(pat, html_txt)

    for word in words:
        sql = us.get_i_sql(DATABASE_LIST_WORDS, {'WORD': str.lower(word.encode('utf-8'))})
        dbm.insert_data(sql)
    return words


# 统计词频方法 传入带有重复单词的列表
# 未使用
def stat_freq(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt

if __name__ == '__main__':
    words = download('https://developer.android.com/index.html')
    for w in words:
        print w