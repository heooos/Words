# -*- coding: UTF-8 -*-
# 依次访问所有的网页

import re
import components.MyLogger as log
from bs4 import BeautifulSoup
import requests as req
import components.SQLTools as us

import components.DBOperation as dbm

DATABASE_ALL_WORDS = "ALL_WORDS"           # 所有的单词数据库
DATABASE_HREF_ERRORS = "HREF_ERRORS"       # 出错的链接数据库

logging = log.get_logger('ReadEachHtml')


def download(m_data):

    url = m_data[2]
    # 读取获取到的链接

    try:
        body = req.get(url, timeout=10)
        bs_body = BeautifulSoup(body.text, 'lxml')
        logging.debug("当前读取第{}条数据,title为{},url为{}".format(m_data[0], m_data[1], m_data[2]))
    except Exception, e:
        logging.error("访问异常,自动跳过本次访问")
        logging.error(e)
        sql = us.get_i_sql(DATABASE_HREF_ERRORS, {'NAME': m_data[1], 'URL': m_data[2]})
        dbm.insert_data(sql)
        return

    # 获取当前页面中所有的正文文字
    try:
        html_txt = bs_body.find(role="main").get_text()
    except Exception, e:
        logging.error("该页面样式有误,错误信息{}".format(e))
        return

    # 正则规则
    pat = '[a-zA-Z]{5,}'
    # 使用正则表达式，把单词提出出来，并都修改为小写格式
    words = re.findall(pat, html_txt)
    for word in words:
        sql = us.get_i_sql(DATABASE_ALL_WORDS, {'WORD': str.lower(word.encode('utf-8'))})
        dbm.insert_data(sql)
    return words

