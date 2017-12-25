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

#项目结构介绍
```
|-- Words
  |-- docs               //文档
  |-- words              //网页数据爬取源码
    |-- test.py             //测试
    |-- DBOperation.py      //数据库操作封装类
    |-- main.py             //程序入口
    |-- GetHtmlList.py      //检索列举所有的网页 添加到数据库
    |-- MyLogger.py         //日志配置类
    |-- ReadEachHtml.py     //依次访问所有的网页 爬取单词
    |-- SQLTools.py         //数据库工具类
  |-- words_analysis     //对爬取数据进行处理
  	|-- cont.txt            //爬取到的数据读取到文件
  	|-- alice.png           //生成的云图
  	|-- gen_cloud_img.py    //生成云图源码
  	|-- main.py             //程序入口
  	|-- test.jpg            //云图模板
  |-- db                 //数据库备份
  	|-- py_tables_TEST_MAIN.sql    //访问链接数据库(1300+)
  	|-- py_tables_TEST_WORDS.sql   //单词数据库 (78w+)
 -- README.md   //README
 -- TODO.md     //待完成清单
 -- default.conf   //配置参数 *数据库* *代理*
```

# How to run project?
