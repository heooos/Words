# -*- coding: UTF-8 -*-
# 检索列举所有的网页 添加到数据库

import sys
import requests as req

import components.MyLogger as log
from lxml import etree


logging = log.get_logger('GetHrefList')

p = {
        'http': 'socks5://test:12345678@67.205.155.10:1080',
        'https': 'socks5://test:12345678@67.205.155.10:1080'
    }

BASE_URL = 'https://docs.python.org/3/{}'
href_dict = {}


def get_href(url):
    try:
        content = req.get(url, timeout=10)  # , proxies=p
    except Exception, e:
        logging.error("Connecting is error" + e)
        return href_dict

    txt = content.text
    ele = etree.HTML(txt.decode('utf-8'))
    l1 = ele.xpath('//*[@id="python-documentation-contents"]/div[1]/ul/li')
    for l1_item in l1:
        l1_text = l1_item.xpath('a')[0].text
        l1_url = BASE_URL.format(l1_item.xpath('./a/@href')[0])
        if "#" not in l1_url:
            href_dict[l1_text] = l1_url
            print '{}:{}'.format(l1_text,l1_url)
        l2 = l1_item.xpath('./ul/li')
        for l2_item in l2:
            l2_text = l2_item.xpath('a')[0].text
            l2_url = BASE_URL.format(l2_item.xpath('./a/@href')[0])
            if "#" not in l2_url:
                href_dict[l2_text] = l2_url
                print '\t{}:{}'.format(l2_text, l2_url)
            l3 = l2_item.xpath('./ul/li')
            for l3_item in l3:
                l3_text = l3_item.xpath('a')[0].text
                l3_url = BASE_URL.format(l3_item.xpath('./a/@href')[0])
                if "#" not in l3_url:
                    href_dict[l3_text] = l3_url
                    print '\t\t{}:{}'.format(l3_text, l3_url)
                l4 = l3_item.xpath('./ul/li')
                for l4_item in l4:
                    l4_text = l4_item.xpath('a')[0].text
                    l4_url = BASE_URL.format(l4_item.xpath('./a/@href')[0])
                    if "#" not in l4_url:
                        href_dict[l4_text] = l4_url
                        print '\t\t\t{}:{}'.format(l4_text, l4_url)
                    l5 = l4_item.xpath('./ul/li')
                    for l5_item in l5:
                        l5_text = l5_item.xpath('a')[0].text
                        l5_url = BASE_URL.format(l5_item.xpath('./a/@href')[0])
                        if "#" not in l5_url:
                            href_dict[l5_text] = l5_url
                            print '\t\t\t\t{}:{}'.format(l5_text, l5_url)
    return href_dict
