# -*- coding: UTF-8 -*-

import ConfigParser as cp

import MySQLdb as mdb
import components.MyLogger as log
import components.SQLTools as us

logging = log.get_logger('main')


# 读取参数
def read_conf():
    # 解析配置文件
    conf = cp.SafeConfigParser()
    conf.read('../default.conf')

    # 读取参数
    m_user = conf.get('db', 'user')
    m_passwd = conf.get('db', 'passwd')
    m_host = conf.get('db', 'host')
    m_name = conf.get('db', 'db_name')
    m_charset = conf.get('db', 'charset')
    m_tables = conf.get('db', 'tables')
    return m_user, m_passwd, m_host, m_name, m_charset, m_tables


def get_db():
    c = read_conf()
    # 打开数据库连接
    db = mdb.connect(user=c[0], passwd=c[1], host=c[2], db=c[3], charset=c[4])
    # 使用cursor()方法获取操作游标
    return db


def get_sql(tables):
    '''
    :param tables: 根据传入的表明创建数据表
    :return: 返回创建的sql语句
    '''
    sql = """CREATE TABLE IF NOT EXISTS """ + tables + """ (
                         _ID INT(4) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                         NAME CHAR(100),
                         URL CHAR(100),
                         IS_READ TINYINT(1) DEFAULT 1) DEFAULT CHARSET=utf8"""
    return sql


# 创建链接数据表
def create_tables(sql):

    # 解析配置文件
    # c = read_conf()

    m_db = get_db()
    cursor = m_db.cursor()

    # 创建数据表SQL语句
    cursor.execute(sql)


# 创建单词数据表
def create_words_tables(tables):

    m_db = get_db()
    cursor = m_db.cursor()

    # 创建数据表SQL语句
    sql = """CREATE TABLE IF NOT EXISTS """ + tables + """ (
                 _ID INT(4) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                 WORD CHAR(10))"""
    cursor.execute(sql)


# 增
def insert_data(sql):
    m_db = get_db()
    cursor = m_db.cursor()

    # SQL 插入语句
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        m_db.commit()
    except Exception, e:
        m_db = get_db()
        # 发生错误时回滚
        m_db.rollback()
        # 关闭数据库连接
        m_db.close()


# 查
def query_data(tables, keys, conditions, isdistinct=0):
    m_db = get_db()
    cursor = m_db.cursor()

    # SQL 查询语句
    sql = us.get_s_sql(tables, keys, conditions)
    cursor.execute(sql)  # 返回值long类型  数据数量
    m = cursor.fetchall()  # 返回值tuple类型 获取数据库所有的值
    return m

if __name__ == '__main__':
    pass