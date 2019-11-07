import requests
# import urllib
import time
import json
# import chardet
import re
import csv
import random

# 每个类别大于200条即可？

START_URL = "https://blog.csdn.net/api/articles?type=more&category=db&shown_offset={}"
# START_URL = "https://blog.csdn.net/api/articles?type=more&category=python&shown_offset={}"

# START_URL = "https://blog.csdn.net/api/articles?type=more&category=java&shown_offset={}"
# START_URL = "https://blog.csdn.net/api/articles?type=more&category=web&shown_offset={}"  # 前端
# START_URL = "https://blog.csdn.net/api/articles?type=more&category=arch&shown_offset={}"  # 架构
# START_URL = "https://blog.csdn.net/api/articles?type=more&category=fund&shown_offset={}"  # 基础



keys = []

# url = 'https://blog.csdn.net/n88Lpo/article/details/100680243'

header = {
    "Accept": "application/json",
    # "Accept-Encoding": "gzip, deflate, br",
    "Host": "blog.csdn.net",
    "Referer": "https://blog.csdn.net/nav/db",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

# header2 = {
#     "Accept": "application/json",
#     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
# }

headerForDetailArticles = {

}

def writeKeyRows(json_data):
    csv_file = open("db/db.csv", "w", newline="")
    writer = csv.writer(csv_file)
    keys = json_data[0].keys()
    writer.writerow(keys)
    csv_file.close()


def trans2csv(json_data):
    csv_file = open("db/db.csv", "a+")
    writer = csv.writer(csv_file)

    for dic_data in json_data:
        # 写数据
        for key in keys:
            if key not in dic:
                dic[key] = ''
        writer.writerow(dic_data.values())
        # print(data)
        # dic_data = json.loads(json_data, encoding='utf8')

    csv_file.close()




def get_url(url, count):

    try:
        res = requests.get(url, headers=header, timeout=3)

        if res.content:
            # print(res.text)
            articles = res.json()
            if articles["status"]:
                need_data = articles["articles"]
                if need_data:
                    # need_data是一个list了
                    trans2csv(need_data)
                    print("成功插入{}条数据".format(len(need_data)))
                    count += len(need_data)
                    if count >= 110:
                        #  结束
                        return
                last_shown_offset = need_data[len(need_data)-1]["shown_offset"]  # 获取最后一条数据的时间戳
                print(last_shown_offset)
                if last_shown_offset >= 0:
                    time.sleep(1)
                    get_url(START_URL.format(last_shown_offset), count)

                    # get_url(START_URL, count)
    except Exception as e:
        print(e)
        print("系统暂停30s，当前出问题的是{}".format(url))

        time.sleep(30)  # 出问题之后，停止30s, 结束
        return


if __name__ == '__main__':
    r = requests.get(START_URL,
                     headers=header)
    count = 0
    first = r.json()
    if first["status"]:
        write_row_data = first["articles"]
        if write_row_data:
            writeKeyRows(write_row_data)
            trans2csv(write_row_data)
        count += len(write_row_data)
    # get_url(START_URL, count)
    get_url(START_URL.format(first["articles"][len(first)-1]["shown_offset"]), count)

