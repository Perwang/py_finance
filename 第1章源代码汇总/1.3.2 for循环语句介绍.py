# =============================================================================
# 1.3.2 for语句 by 华能信托-王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

class1 = ['丁一', '王二麻子', '张三', '李四', '赵五']
for i in class1:
    print(i)

# 这个i只是个代号，可以换成任何别的内容
class1 = ['丁一', '王二麻子', '张三', '李四', '赵五']
for haha in class1:
    print(haha)

# for和range函数合用
for i in range(3):
    print('hahaha')

'''
总结
（1）对于"for i in 区域"来说，如果说这个区域是一个列表，那么那个i就表示这个列表里的每一个元素；
（2）对于"for i in 区域"来说，如果说这个区域是一个range(n)，那么那个i就表示0到n -1这n个数字，之前提到过，python中序号都是从0开始的，所以这边也是从0开始，到n - 1结束。
（3）对于"for i in 区域"来说，若区域是一个字典，那么i就表示字典的键名；
'''
# 注意python中序号都是从0开始的
for i in range(5):
    print(i)

# 在实战中的应用
title = ['标题1', '标题2', '标题3', '标题4', '标题5']
for i in range(len(title)):  # len(title)表示一个有多少个新闻，这里是5；这里的i就表示数字0-4
    print(str(i+1) + '.' + title[i])  # 这个其实把字符串进行一个拼接