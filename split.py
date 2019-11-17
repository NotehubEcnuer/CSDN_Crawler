
"""

@author: LEODPEN

@contact: leodpen@gmail.com

@file: split.py

@time: 2019/11/17 15:15

@desc: simple demo to split csv files

"""

import numpy as np
import pandas as pd
import csv
import os


pyTags = ["python", "py", "numpy", "pandas"]
dbTags = ["mysql", "sql", "Oracle", "事务", "隔离", "Hadoop", "Hbase", "Mongo", "PgSql"]


# 提取df,转dict，dict中加tag,分出多个dict，分别转df，再写入csv
# 此处为demo，只分两类
def split(file_folder):
    toSplitData = pd.read_csv(os.path.join(file_folder, 'arch.csv'), sep=',', index_col=None)
    # print(toSplitData)
    desCsvData = {}
    desCsvData["summary"] = toSplitData["summary"]
    desCsvData["url"] = toSplitData["url"]
    desCsvData["user_name"] = toSplitData["user_name"]
    py = {}
    py["summary"] = []
    py["url"] = []
    py["user_name"] = []
    db = {}
    db["summary"] = []
    db["url"] = []
    db["user_name"] = []
    # print(desCsvData)

    for i in range(0, len(desCsvData["summary"]), 1):
        content = desCsvData["summary"][i]
        # 一篇文章可能不止一个tag
        for str in pyTags:
            if content.find(str) >= 0:
                py["summary"].append(content)
                py["url"].append(desCsvData["url"][i])
                py["user_name"].append(desCsvData["user_name"][i])
                break
        for str in dbTags:
            if content.find(str) >= 0:
                db["summary"].append(content)
                db["url"].append(desCsvData["url"][i])
                db["user_name"].append(desCsvData["user_name"][i])
                break
    # print(len(py["url"]))
    # print(len(db["url"]))
    # print(db)
    df = pd.DataFrame.from_dict(db)
    # print(df)
    # 只将db转化为csv
    os.getcwd()
    df.to_csv('split_demo_db.csv', index=0)  # 不保存列index




    # df = pd.DataFrame.from_dict(desCsvData)
    # print(df)


if __name__ == '__main__':
    split("./")