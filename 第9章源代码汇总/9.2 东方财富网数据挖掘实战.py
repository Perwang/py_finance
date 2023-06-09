# =============================================================================
# 9.2 东方财富网数据挖掘实战 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

from selenium import webdriver
import re


def dongfang(company):
    browser = webdriver.Chrome()  # 这里改成了有界面模式，方便调试代码
    url = 'http://so.eastmoney.com/news/s?keyword=' + company
    browser.get(url)
    data = browser.page_source
    browser.quit()
    # print(data)  # 如果正则发生变化，可以通过打印源代码进行调试

    p_title = '<div class="news-item"><h3><a href=".*?">(.*?)</a>'
    p_href = '<div class="news-item"><h3><a href="(.*?)">.*?</a>'
    p_date = '<p class="news-desc">(.*?)</p>'
    title = re.findall(p_title, data)
    href = re.findall(p_href, data)
    date = re.findall(p_date, data, re.S)

    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        date[i] = date[i].split(' ')[0]
        print(str(i+1) + '.' + title[i] + ' - '+ date[i])
        print(href[i])


dongfang('贵州茅台')  # 可以通过它来调试，如果没问题，再通过下面的代码批量运行

# companys = ['华能信托', '阿里巴巴', '腾讯', '京东', '万科']
# for i in companys:
#     try:
#         dongfang(i)
#         print(i + '该公司东方财富网爬取成功')
#     except:
#         print(i + '该公司东方财富网爬取失败')


