# -*- coding: UTF-8 -*-

import time
from multiprocessing.dummy import Pool as Threadpool
import components.SQLTools as us

import enchant

import components.DBOperation as dbm

GET_UNIQUE = "SELECT DISTINCT " + "WORD" + " FROM " + "ALL_WORDS"
d = enchant.Dict("en_US")


# 获取唯一的单词
def get_words_from_db():
    m_db = dbm.get_db()
    cursor = m_db.cursor()
    cursor.execute(GET_UNIQUE)
    words = cursor.fetchall()
    m_db.close()
    return words


# 根据单词查询出现的频率
def query_words_count(w):
    m_db = dbm.get_db()
    cursor = m_db.cursor()
    wor = str(w)
    sql = "SELECT COUNT(1) FROM ALL_WORDS WHERE WORD="+"\""+wor+"\""

    cursor.execute(sql)
    m = cursor.fetchall()
    return str(m[0][0])


# 保存单词到数据库
def save(word):
    str_word = word[0]
    if d.check(str_word):  # 通过PyEnchant库将无效单词剔除出去(简写 特有 库名等)
        fre = query_words_count(str_word)
        sql = us.get_i_sql("UNIQUE_WORDS", {'WORD': str_word, 'FREQUENCY': fre})
        dbm.insert_data(sql)
        print word[0]
        # with open('./python.txt', 'a') as ff:
        #     ff.write(str_word + ":" + str(query_words_count(str_word)) + "\n")

unique_words = get_words_from_db()

pool = Threadpool(10)
s_time = time.time()
pool.map(save, unique_words)
e_time = time.time()
print u"十线程时间为{}秒".format(e_time - s_time)
# for word in unique_words:
#     str_word = word[0]
#     if d.check(str_word):    # 通过PyEnchant库将无效单词剔除出去(简写 特有 库名等)
#         query_words_count(str_word)
#         with open('./cont.txt', 'a') as ff:
#             ff.write(str_word + ":" + str(query_words_count(str_word))+"\n")
print '写入完成'
# print (word[0] + ":" + str(query_words_count(word[0])))
