# -*- coding: UTF-8 -*-
# 程序入口

import sys
import time

import components.MyLogger as log
from multiprocessing.dummy import Pool as Threadpool
import components.SQLTools as us
import components.DBOperation as dbm

import ReadEachHtml as rd
import GetHrefList as ghl

logging = log.get_logger('main')
logging.debug('''
*****************************************
***************日志文件*******************
*****************************************''')


DATABASE_ALL_HREFS = "ALL_HREFS"           # 保存所有需要读取的链接数据库
DATABASE_ALL_WORDS = "ALL_WORDS"           # 所有的单词数据库
DATABASE_HREF_ERRORS = "HREF_ERRORS"       # 出错的链接数据库
DATABASE_UNIQUE_WORDS = "UNIQUE_WORDS"     # 经处理后的唯一单词数据库

reload(sys)
sys.setdefaultencoding('utf-8')

dbm.create_tables(dbm.get_sql(DATABASE_HREF_ERRORS))
dbm.create_tables(dbm.get_sql(DATABASE_ALL_HREFS))
dbm.create_tables("""CREATE TABLE IF NOT EXISTS """ + DATABASE_ALL_WORDS + """ (
                 _ID INT(4) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                 WORD CHAR(10)) DEFAULT CHARSET=utf8""")
dbm.create_tables("""CREATE TABLE IF NOT EXISTS """ + DATABASE_UNIQUE_WORDS + """ (
                 _ID INT(4) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                 WORD CHAR(10),
                 FREQUENCY INT(8)) DEFAULT CHARSET=utf8""")

logging.debug("DataBase(TestOP) is Created!")

pool = Threadpool(100)

href_dict = ghl.get_href('https://docs.python.org/3/contents.html')

logging.debug("----------------列表获取完毕,开始数据库插入----------------------")

if href_dict:
    i = 0
    for key, value in href_dict.items():
        sql = us.get_i_sql(DATABASE_ALL_HREFS, {'NAME': key, 'URL': value})
        dbm.insert_data(sql)
    print i
logging.debug("----------------数据库插入完成,开始遍历页面,获取单词----------------------")

data = dbm.query_data(DATABASE_ALL_HREFS, "*", None)   # 返回元组格式

start_time = time.time()
pool.map(rd.download, data)
end_time = time.time()
print u"多线程使用时间为{}秒".format(end_time - start_time)
logging.debug("----------------------------单词获取完成--------------------------------")