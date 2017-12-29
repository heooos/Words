# -*- coding: UTF-8 -*-
# 程序入口

import sys
import time
from multiprocessing.dummy import Pool as Threadpool

import GetHtmlList as getl
import ReadEachHtml as rd
import components.DBOperation as dbm
import components.MyLogger as log
import components.SQLTools as us

logging = log.get_logger('main')
logging.debug('''
*****************************************
***************日志文件*******************
*****************************************''')

DATABASE_NAME_LIST = "TEST_MAIN"
DATABASE_NAME_REF = "TEST_REF"
DATABASE_NAME_CHILD = "TEST_CHILD"
DATABASE_LIST_WORDS = "TEST_WORDS_TEST"
DATABASE_LIST_ERROR = "TEST_ERROR"


reload(sys)  # 2
sys.setdefaultencoding('utf-8')  # 3
dbm.create_tables(dbm.get_sql(DATABASE_NAME_LIST))
dbm.create_tables(dbm.get_sql(DATABASE_NAME_REF))
dbm.create_tables(dbm.get_sql(DATABASE_NAME_CHILD))
dbm.create_tables(dbm.get_sql(DATABASE_LIST_ERROR))
dbm.create_words_tables(DATABASE_LIST_WORDS)
#
logging.debug("DataBase(TestOP) is Created!")
#
pool = Threadpool(100)
#
start_time = time.time()
# 访问列表获取
m_dict = getl.get_main_html('https://developer.android.com/index.html')
end_time = time.time()

print u"获取列表使用时间为{}秒".format(end_time - start_time)

logging.debug("----------------列表获取完毕,开始数据库插入----------------------")


if m_dict[0]:
    for item in m_dict[0]:
        o = item.split('*')
        sql = us.get_i_sql(DATABASE_NAME_LIST, {'NAME': o[0], 'URL': o[1]})
        dbm.insert_data(sql)
    if m_dict[1]:
        for item in m_dict[1]:
            o = item.split('*')
            sql = us.get_i_sql(DATABASE_NAME_REF, {'NAME': o[0], 'URL': o[1]})
            dbm.insert_data(sql)
    if m_dict[2]:
        for item in m_dict[2]:
            o = item.split('*')
            if o[0] == 'Get Started':
                sql = us.get_i_sql(DATABASE_NAME_LIST, {'NAME': o[0], 'URL': 'https://developer.android.com/things/get-started/index.html'})
                dbm.insert_data(sql)
                break
            sql = us.get_i_sql(DATABASE_NAME_CHILD,
                               {'NAME': o[0], 'URL': o[1]})
            dbm.insert_data(sql)
else:
    logging.error("Please check internet")

logging.debug("----------------数据库插入完成,开始遍历页面,获取单词----------------------")

data = dbm.query_data(DATABASE_NAME_LIST, "*", None)
start_time = time.time()
pool.map(rd.download, data)
# for m_data in data:
#     # print m_data[0]
#     rd.download(m_data)
end_time = time.time()
print u"二百线程使用时间为{}秒".format(end_time - start_time)
logging.debug("----------------------------单词获取完成--------------------------------")