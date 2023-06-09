# =============================================================================
# 4.3.4 连接数据库并提取数据 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

# 1.根据1个条件查找并提取
import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='pachong', charset='utf8')

company = '阿里巴巴'

cur = db.cursor()  # 获取会话指针，用来调用SQL语句
sql = 'SELECT * FROM test WHERE company = %s'  # 编写SQL语句
cur.execute(sql,company)  # 执行SQL语句
data = cur.fetchall()  # 提取所有数据，并赋值给data变量
print(data)
db.commit()  # 这个其实可以不写，因为没有改变表结构
cur.close()  # 关闭会话指针
db.close()  # 关闭数据库链接


# 2.根据2个条件查找并提取
import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='pachong', charset='utf8')
company = '阿里巴巴'
title = '标题1'

cur = db.cursor()  # 获取会话指针，用来调用SQL语句
sql = 'SELECT * FROM test WHERE company = %s AND title = %s'  # 编写SQL语句
cur.execute(sql, (company, title))  # 执行SQL语句
data = cur.fetchall()  # 提取所有数据，并赋值给data变量
print(data)
db.commit()  # 这个其实可以不写，因为没有改变表结构
cur.close()  # 关闭会话指针
db.close()  # 关闭数据库链接

