# -*- coding: UTF-8 -*-
# 检索列举所有的网页 添加到数据库

import sys

import requests as req
from bs4 import BeautifulSoup

import components.MyLogger as log

logging = log.get_logger('GetHtmlList')
p = {
        'http': 'socks5://test:12345678@67.205.***.**:1080',
        'https': 'socks5://test:12345678@67.205.***.**:1080'
    }

# 链接数统计
m_count = 0
mm_list = []

unread_ref_list = []
unread_child_list = []


# 访问首页 进行文章链接获取
def get_main_html(url):
    try:
        content = req.get(url, timeout=10, proxies=p)  # , proxies=p
    except Exception, e:
        logging.error("Connecting is error"+e)
        return mm_list

    bs_content = BeautifulSoup(content.text, 'lxml')

    m = bs_content.find(id="dac-main-navigation")
    m_list = m.find_all('a')

    for af in m_list:
        # 特殊情况一 Policy center页面为中文 跳过
        if af.text.strip() == 'Policy center':
            continue
        mm_list.append((af.text + "*" + af['href']).strip())
        logging.debug((af.text + ":" + af['href']).strip())
        # 特殊情况二 Reference页面通过class解析
        if af.text.strip() == 'Reference':
            get_ref_html(af)
        get_html(af)
    num = bytes(m_count)
    logging.debug("共"+num+"条数据,下载完成")
    return mm_list, unread_ref_list, unread_child_list


# 特殊情况 Reference
def get_ref_html(af):

    global m_count
    url = af['href']
    try:
        content = req.get(url, timeout=10, proxies=p)  # , headers=headers , proxies=p
    except:
        logging.error("Connecting is error,break this loop")
        unread_ref_list.append((af.text + "*" + af['href']).strip())
        return
    bs_content = BeautifulSoup(content.text, 'lxml')
    m = bs_content.find(class_='dac-reference-nav')
    for af in m.find_all('a'):
        mm_list.append((af.text + "*" + af['href']).strip())
        logging.debug((af.text + ":" + af['href']).strip())
        m_count += 1
    # print "--------------------------"


# 进行各子页面文章链接获取
def get_html(af, *flag):

    global m_count
    cache = 0
    url = af['href']
    if url == '/things/get-started/index.html':
        url = 'https://developer.android.com/things/get-started/index.html'
    try:
        content = req.get(url, timeout=10, proxies=p)  #, headers=headers , proxies=p
    except:
        logging.error("Connecting is error,break this loop")
        unread_child_list.append((af.text + "*" + af['href']).strip())
        return
    bs_content = BeautifulSoup(content.text, 'lxml')
    m = bs_content.find(id='nav')

    if m is None:
        print "特殊任务"
        m = bs_content.find(id="dac-main-navigation")
        m_li = m.find_all('a')
        if len(m_li) > 20 or flag:
            m_count += 1
            print "当前页面"
        else:
            print "进入子界面"
            for af in m_li:
                cache += 1
                if cache == 1:
                    continue
                m_count += 1
                logging.debug((af.text + ":" + af['href']).strip())
                mm_list.append((af.text + "*" + af['href']).strip())
                get_html(af, True)
            print '----------------'

        return

    for af in m.find_all('a'):
        mm_list.append((af.text + "*" + af['href']).strip())
        logging.debug((af.text + ":" + af['href']).strip())
        m_count += 1


if __name__ == '__main__':

    reload(sys)  # 2
    sys.setdefaultencoding('utf-8')  # 3
    get_main_html('https://developer.android.com/index.html')