# =============================================================================
# 1.2.3 列表与字典 by 华能信托-王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

# # 列表
class1 = ['丁一', '王二麻子', '张三', '李四', '赵五']
print(class1)

list1 = [1, '123', [1, 2, 3]]
print(list1)

class1 = ['丁一', '王二麻子', '张三', '李四', '赵五']
for i in class1:  # 这个for语句之后会重点讲，这边大家先运行看看效果即可
    print(i)

# 统计列表的元素个数的函数：len函数
class1 = ['丁一', '王二麻子', '张三', '李四', '赵五']
a = len(class1)
print(a)

# 调取一个列表元素的方法
class1 = ['丁一', '王二麻子', '张三', '李四', '赵五']
a = class1[1]
print(a)

# 选取多个列表元素的方法：列表切片
class1 = ['丁一', '王二麻子', '张三', '李四', '赵五']
a = class1[1:4]
print(a)

b = class1[1:]  # 选取从第二个元素到最后
c = class1[-3:]  # 选取从列表倒数第三个元素到最后
d = class1[:-2]  # 选取倒数第二个元素前的所有元素（因为左闭右开，所以不包含倒数第二个元素）
print(b)
print(c)
print(d)

# 列表增加元素的办法：append方法，这个先了解下即可
score = []
score.append(80)
print(score)

score = []
score.append(80)
score.append(90)
score.append(70)
print(score)

# 列表转换成字符串，这个先了解下即可，很远之后才用的上
class1 = ['丁一', '王二麻子', '张三', '李四', '赵五']
a = ",".join(class1)
print(a)

'''字典，关于字典这个知识，先了解下即可'''
# 字典名["键名"]提取值
class1 = {'丁一': 85, '王二麻子': 95, '张三': 75, '李四': 65, '赵五': 55}
score = class1['王二麻子']
print(score)

# 遍历字典内容1
class1 = {'丁一': 85, '王二麻子': 95, '张三': 75, '李四': 65, '赵五': 55}
for i in class1:  # 这个i代表的是字典中的键，也就是丁一、王二麻子等
    print(i)
    print(class1[i])

# 遍历字典内容2
class1 = {'丁一': 85, '王二麻子': 95, '张三': 75, '李四': 65, '赵五': 55}
for i in class1:
    print(i + ':' + str(class1[i]))  # 注意要str把85等数字转换成字符串，才能进行字符串拼接

# 遍历字典内容3
class1 = {'丁一': 85, '王二麻子': 95, '张三': 75, '李四': 65, '赵五': 55}
a = class1.items()
print(a)


'''元组和集合（了解即可）'''
# 元组 其实和列表基本一样，区别在于元组里的元素不可修改，及包围的括号为小括号
a = ('丁一', '王二', '张三', '李四', '赵五')  # 这就是个元组，是不是和列表很像呢
print(a[1:3])

# 集合
a = ['丁一', '丁一', '王二', '张三', '李四', '赵五']
print(set(a))  # 通过set()函数可以获得一个集合，集合一个主要特点，就是用来去重，结果为：{'丁一', '王二', '赵五', '张三', '李四'}









