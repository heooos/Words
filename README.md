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
  |-- components         //公共组件
      |-- DBOperation.py      //数据库操作封装类
      |-- MyLogger.py         //日志配置类
      |-- SQLTools.py         //数据库工具类
  |-- android_words      //网页(https://developer.android.com/index.html)数据爬取源码
    |-- test.py             //测试
    |-- main.py             //程序入口
    |-- GetHtmlList.py      //检索列举所有的网页 添加到数据库
    |-- ReadEachHtml.py     //依次访问所有的网页 爬取单词
  |-- python_words      //网页(https://docs.python.org/3/contents.html)数据爬取源码
  	|-- GetHrefList.py      //检索列举所有的网页 添加到数据库
  	|-- ReadEachHtml.py     //依次访问所有的网页 爬取单词
  	|-- main.py             //程序入口
  |-- words_analysis     //对爬取数据进行处理
  	|-- android.txt         //Android爬取到的数据读取到文件
  	|-- python.txt          //Python爬取到的数据读取到文件
  	|-- gen_cloud_img.py    //生成云图源码入口
  	|-- main.py             //数据准备入口
  |-- image              //图册
  	|-- android_img.jpg       //Android图片模板
  	|-- android_img_com.png   //Android生成的云图
  	|-- python_img.jpg        //Python图片生产模板
  	|-- python_img_com.png    //Python生成的云图
  |-- db                 //数据库备份
  	|-- android
  		|-- py_tables_TEST_MAIN.sql    //访问链接数据库(1300+)
  		|-- py_tables_TEST_WORDS.sql   //单词数据库 (78w+)
  	|-- python
  		|-- python_tables_ALL_HREFS.sql  //访问链接数据库(449)
  		|-- python_tables_ALL_WORDS.sql  //单词数据库 (50w+)
  		|-- python_tables_UNIQUE_WORDS.sql //唯一单词数据库(7132) 频率
 -- README.md   //README
 -- TODO.md     //待完成清单
 -- default.conf   //配置参数 *数据库* *代理*
```

# How to run project?
