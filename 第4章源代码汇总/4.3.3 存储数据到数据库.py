# =============================================================================
# 4.3.3 数据插入数据库 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

# 先预定义些变量
company = '阿里巴巴'
title = '测试标题'
href = '测试链接'
source = '测试来源'
date = '测试日期'

# 连接数据库
import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='pachong', charset='utf8')

# 插入数据
cur = db.cursor()  # 获取会话指针，用来调用SQL语句
sql = 'INSERT INTO test(company, title, href, source, date) VALUES (%s, %s, %s, %s, %s)'  # 编写SQL语句
cur.execute(sql, (company, title, href, source, date))  # 执行SQL语句
db.commit()  # 当改变表结构后，更新数据表的操作
cur.close()  # 关闭会话指针
db.close()  # 关闭数据库链接
