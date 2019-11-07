import requests
# import urllib
import time
import re
import csv
import random
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup, Comment
from tomd import Tomd

header = {
    # "Accept": "*/*",
    # "Host": "event.csdn.net",
    # "Referer": "https://blog.csdn.net/qq_15267543",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
    # "X-Requested-With": "XMLHttpRequest"
}


def delete_ele(soup: BeautifulSoup, tags: list):
	for ele in tags:
		for useless_tag in soup.select(ele):
			useless_tag.decompose()


def delete_ele_attr(soup:BeautifulSoup, attrs:list):
	for attr in attrs:
		for useless_attr in soup.find_all():
			del useless_attr[attr]


def delete_blank_ele(soup:BeautifulSoup, eles_except:list):
	for useless_attr in soup.find_all():
		try:
			if useless_attr.name not in eles_except and useless_attr.text == "":
				useless_attr.decompose()
		except Exception:
			pass


def getDetailFromUrl(url):
    # print(url)
    response = requests.get(url, headers=header, timeout=20)
    html = response.text
    print(html)
    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one("#content_views")
    # 删除注释
    for useless_tag in content(text=lambda text: isinstance(text, Comment)):
        useless_tag.extract()
    # 删除无用标签
    tags = ["svg", "ul", ".hljs-button.signin"]
    delete_ele(content, tags)

    # 删除标签属性
    attrs = ["class", "name", "id", "onclick", "style", "data-token", "rel"]
    delete_ele_attr(content, attrs)

    # 删除空白标签
    eles_except = ["img", "br", "hr"]
    delete_blank_ele(content, eles_except)
    # 转换为markdown
    md = Tomd(str(content)).markdown
    return md

def getDetailFromLocal(html):

    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one("#content_views")
    # 删除注释
    for useless_tag in content(text=lambda text: isinstance(text, Comment)):
        useless_tag.extract()
    # 删除无用标签
    tags = ["svg", "ul", ".hljs-button.signin"]
    delete_ele(content, tags)

    # 删除标签属性
    attrs = ["class", "name", "id", "onclick", "style", "data-token", "rel"]
    delete_ele_attr(content, attrs)

    # 删除空白标签
    eles_except = ["img", "br", "hr"]
    delete_blank_ele(content, eles_except)
    # 转换为markdown
    md = Tomd(str(content)).markdown
    return md



def getDetailAndSave():
    df = pd.read_csv(r'python/python.csv')
    newColumn = df["url"]
    df["content"] = newColumn
    print(df["url"][0])
    md = getDetailFromUrl(df["url"][0])
    print(md)


    # for i in range(len(df["url"])):
    #     getDetailFromUrl(df["url"][i])
    #     df["content"][i] = 1
    # df.to_csv(r"newPython.csv", mode='w', index=False)

def writeTxt(md):
    file_txt = open('python/1.txt', 'w', encoding='utf-8')
    file_txt.write(md)
    file_txt.close()

if __name__ == '__main__':
    # getDetailFromUrl("https://blog.csdn.net/qq_15267543/article/details/102930590")
    # getDetailAndSave()
    htmlfile = open("python/1.html", 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()
    md = getDetailFromLocal(htmlhandle)
    writeTxt(md)
    print(md)