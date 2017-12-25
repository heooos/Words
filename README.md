# 项目介绍
该项目是从Android官网爬取文章/API内容,然后讲网页单词提取和进行频率统计,
方便自己对于单词的记忆,以便更好的阅读英文文章。

# 环境及lib介绍
* Python2.7
* MySQLdb5.7.20
* ConfigParser    //配置文件
* BeautifulSoup   //网页解析库
* requests   //网络请求库
* Counter   //
* wordcloud  //绘制词云图
* PIL  //图形相关
* matplotlib.pyplot  //绘图库
* multiprocessing.dummy   //python多线程
* logging   //日志库
* re   //正则表达式库

#项目介绍
```
|-- Words
  |-- docs            //文档
  |-- words          //源码
    |-- test.py       //测试
    |-- main.py     //程序入口
 -- README.md   //README
 -- default.conf   //配置参数 *数据库* *代理*
```

# How to run project?
