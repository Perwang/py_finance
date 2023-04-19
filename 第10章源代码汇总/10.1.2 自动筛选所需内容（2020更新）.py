# =============================================================================
# 10.1.2 自动筛选所需内容 by 王宇韬
# =============================================================================

from selenium import webdriver
import re
import time
browser = webdriver.Chrome()
url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=理财'
browser.get(url)
time.sleep(3)
data = browser.page_source
p_count = '<span class="total-box" style="">约(.*?)条'
count = re.findall(p_count, data)[0]  # 获取公告个数，注意这里要加一个[0],因为findall返回的是一个列表
pages = int(int(count)/10)

# 1.自动翻页获取源码源代码
datas = []
datas.append(data)  # 这边是把第一页源代码先放到datas这个列表里
for i in range(3):  # 这边为了演示改成了range(3)，想爬全部的话改成range(pages)
    browser.find_element_by_xpath('//*[@id="fulltext-search"]/div/div[1]/div[2]/div[4]/div[2]/div/button[2]').click()
    time.sleep(2)
    data = browser.page_source
    datas.append(data)
    time.sleep(1)
alldata = "".join(datas)
browser.quit()

# 2.编写正则表达式
p_title = '<span title="" class="r-title">(.*?)</span>'
p_href = '<a target="_blank" href="(.*?)"data-id='
p_date = '<span class="time">(.*?)</span>'
title = re.findall(p_title, alldata)
href = re.findall(p_href, alldata)
date = re.findall(p_date, alldata, re.S)

# 3.清洗数据
for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    href[i] = 'http://www.cninfo.com.cn' + href[i]
    href[i] = re.sub('amp;', '', href[i])
    date[i] = date[i].strip()
    date[i] = date[i].split(' ')[0]
    print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
    print(href[i])

# 4.自动筛选
for i in range(len(title)):
    if '2020' in date[i] or '2021' in date[i]:  # 筛选2019和2020年的，可以自己调节
        title[i] = title[i]
        href[i] = href[i]
        date[i] = date[i]
    else:
        title[i] = ''
        href[i] = ''
        date[i] = ''
while '' in title:
    title.remove('')
while '' in href:
    href.remove('')
while '' in date:
    date.remove('')

'''利用同样的思路，我们也能对标题进行清洗，如果该标题里还有某些不想要的关键词，比如说“保底”、“刚兑”等关键词，我们就把它赋值为空值，代码如下：'''
for i in range(len(title)):
    if '保底' in title[i] or '刚兑' in title[i]:
        title[i] = ''
        href[i] = ''
        date[i] = ''
    else:
        title[i] = title[i]
        href[i] = href[i]
        date[i] = date[i]
while '' in title:
    title.remove('')
while '' in href:
    href.remove('')
while '' in date:
    date.remove('')
