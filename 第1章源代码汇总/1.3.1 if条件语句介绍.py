# =============================================================================
# 1.3.1 if语句 by 华能信托-王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

score = 100
year = 2018
if (score < 0) and (year == 2018):
    print('录入数据库')
else:
    print('不录入数据库')

score = 85
if score >= 60:
    print('及格')
else:
    print('不及格')

# 多种情况，这个用到的较少，了解即可
score = 55
if score >= 80:
    print('优秀')
elif (score >= 60) and (score < 80):
    print('及格')
else:
    print('不及格')