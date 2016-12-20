#-*- coding:utf8 -*-
import urllib2
import urllib
import re
from lxml import etree
from bs4 import BeautifulSoup
import os
import pdfkit
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def GetPage(url):

    #生成request并设置代理
    request = urllib2.Request(url)
    request.add_header('User_Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) '
                                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/52.0.2743.116 Safari/537.36')
    #爬取页面并返回
    try:
        page = urllib2.urlopen(request)
        return page.read()

    except Exception:
        return None


def GetContent(page):

    #使用BeautifulSoup解析页面
    soup = BeautifulSoup(page, 'lxml')

    #选取出页面的内容部分，这里用的是CSS selector定位内容的div
    selector = '#main > div.uk-container.x-container > div:nth-of-type(2) > ' \
               'div > div.x-center > div.x-content > div.x-wiki-content'
    content = soup.select(selector)

    #将选择出来的内容转化成字符串，作为content
    str_content = str(content[0]).encode('utf8')

    #使用正则表达式选取出content中的图片的src
    pattern = re.compile(r'img.*?src="(.*?)"/')

    for image_url in pattern.findall(str_content):
        #将图片下载并将图片的src进行替换
        if image_url.startswith('/files'):
            DownloadImage(image_url)
            temp = image_url.split('/')
            str_content = str_content.replace(image_url,"./download/" +
                                              temp[3] + ".png")

    return str_content


def CombineHtml(content,title):

    #将内容追加到网页中
    with open('total.html', 'ab') as f:
        f.write(('<h1>'+ title + '</h1>').encode('utf8'))
        f.write(content.encode('utf8'))
        f.write(('<br><br><br><br><br>').encode('utf8'))


def DownloadImage(url):

    #下载图片到download文件中
    try:
        temp = url.split('/')
        if not os.path.isdir("download"):
            os.mkdir("download")
        filename = './download/' + temp[3] + '.png'
        urllib.urlretrieve('http://www.liaoxuefeng.com' + url, filename)

    except IndexError:
        pass


def Main():

    #计数
    count = 0
    #依次访问的URL list
    url_list = []
    prefix = 'http://www.liaoxuefeng.com'
    index = 'http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000'

    #获取主页
    page = GetPage(index)

    #从主页中提取所有页面的URL和所有页面的主标题
    index_content = etree.HTML(page)
    url_xpath = '//*[@id="main"]/div/div/div/div/div/ul/li/a/@href'
    title_xpath = '//*[@id="main"]/div/div/div/div/div/ul/li/a/text()'
    url_result = index_content.xpath(url_xpath)
    title_result = index_content.xpath(title_xpath)

    #创建一个HTML网页用来存储所有教材内容
    with open('total.html', 'wb') as f:
        f.write(('<head><meta http-equiv="content-type" content="text/html; charset=UTF-8"></head>')
                .encode('utf8'))

    #给爬取出来的每个URL添加前缀
    for item in url_result:
        url = prefix + item
        url_list.append(url)

    #对每个URL进行爬取，然后获取需要的内容，将其合成网页
    for url in url_list:
        page = GetPage(url)
        content = GetContent(page)
        CombineHtml(content,title_result[count])
        count = count + 1
        print count

    #将HTML转成PDF
    path_wkthmltopdf = r'D:/wkhtmltopdf/bin/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)
    pdfkit.from_file('total.html','total.pdf',configuration = config)


if __name__ == "__main__":
    Main()