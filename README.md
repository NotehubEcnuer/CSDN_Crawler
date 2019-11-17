# CSDN_Crawler
业余爬虫，几个类型均110条左右

## 说明

+ `csdnCrawler.py`: 用作爬不同标签的博客信息(110-120条)，并存csv文件.

+ `tomd.py`: 把html文件转md，效果较差，但是问题不大，能显示和做分析。

+ `detailCrawler.py`：根据url（csv文件里面的）来爬取具体的html内容。

+ `split.py`: 将csv file分为多个的demo，可以丰富后使用

## 问题与解决方案

+ 具体内容无法直接爬到，会出现403，模拟headers也没用.

    1. 傻瓜式解决方案：查看网页源代码并存本地，调用第三个朋友文件的函数来转并存txt。示例：`1.txt`（见python文件夹）

+ 标签文件夹内容未真正有分类感

    1. ~~在数量不多的前提下，可以根据简介手动操作一下。~~
    2. 利用`split.py`进行分类，分成多个csv文件，然后concatenate在一起(工具文件待写).需要手动写特征词(eg):
    ```python
    dbTags = ["mysql", "sql", "Oracle", "事务", "隔离", "Hadoop", "Hbase", "Mongo", "PgSql"]
    ```
> 根据summary进行分类即可，分好再tomd等操作


