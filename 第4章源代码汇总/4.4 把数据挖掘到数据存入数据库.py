# =============================================================================
# 4.4 把数据挖掘到数据存入数据库 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

import requests
import re
import pymysql
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


def baidu(company):
    url = 'http://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company
    res = requests.get(url, headers=headers).text

    # 正则表达式编写
    p_href = '<h3 class="news-title_1YtI1 "><a href="(.*?)"'
    href = re.findall(p_href, res, re.S)
    p_title = '<h3 class="news-title_1YtI1 ">.*?>(.*?)</a>'
    title = re.findall(p_title, res, re.S)
    p_date = '<span class="c-color-gray2 c-font-normal c-gap-right-xsmall" .*?>(.*?)</span>'
    date = re.findall(p_date, res)
    p_source = '<span class="c-color-gray" .*?>(.*?)</span>'
    source = re.findall(p_source, res)

    # 数据清洗及打印
    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过这里好像不太需要了
        title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
        if ('小时' in date[i]) or ('分钟' in date[i]):  # 下面这几行代码是对日期做了一个处理，如果包含小时或者分钟，就转为当天日期
            date[i] = time.strftime("%Y-%m-%d")
        else:
            date[i] = date[i]
        print(str(i + 1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')')
        print(href[i])

    # 将数据存入数据库
    for i in range(len(title)):
        db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='monitor2', charset='utf8')
        cur = db.cursor()
        sql = 'INSERT INTO test(company,title,href,source,date) VALUES (%s,%s,%s,%s,%s)'
        cur.execute(sql, (company, title[i], href[i], source[i], date[i]))
        db.commit()
        cur.close()
        db.close()


baidu('阿里巴巴')
print('数据爬取并导入数据库成功')
