# -*- coding: utf-8 -*-

# 字符串类型
string = '字符串类型数据'

# 字符串操作
# 字符串截取（子串：一段来自于原字符串中的连续字符串）

# 下标法：string[下标]
print(string[0])
# 切片法： string[begin:end] begin: 默认从0开始  end：截取结束位置长度通常 <= len(string) 当end 为负数时：end 等价于len(string) + end
print(string[0:2])
print(string[:5])
print(string[2:])
print(string[2:len(string)])
print(string[2:-1])

# 数字类型
number = 100

# 数值类型一般应用于数值运算 加减乘除

# 列表类型
lists = [1, 2, 3, 4, 5, 6, 7]

# 应用：子列表、增、删、改、查

# 子列表: 从lists 中截取一部分生成一个新的列表, 解决方法同字符串
# 下标法：lists[index]
print(lists[0])
# 切片法：lists[begin:end] begin: 默认从0开始  end：截取结束位置长度通常 <= len(string) 当end 为负数时：end 等价于len(string) + end
print(lists[0:2])
print(lists[:5])
print(lists[2:])
print(lists[2:len(lists)])
print(lists[2:-1])

# 增加元素：lists.append(val) 从列表的尾部插入一个数据 val: 要插入的值
# lists.insert(index, val) 指定位置 后 插入一个数据 index：位置
lists.append('sd')
print(lists)

# 删 lists.pop(index) index: 指定数组下标
lists.pop(2)
print(lists)

# 改、查：一般使用循环
for index in range(len(lists)):
    print(index)
    if lists[index] == 2:
        lists[index] = '我修改了'
print(lists)

# 元组：从外形上 和 列表的区别就是 元组() 小括号包裹、列表[] 中括号包裹 与数组不同的是元组的数据不能修改
tuples = ('1', '2', '元组')

# 不可修改：下面语句报错 错误信息：TypeError: 'tuple' object does not support item assignment
# tuples[0] = 10

# 其他的操作同列表：切片法、坐标法


# 集合：集合中的元素是单一且唯一存在的，其构造形式 {} 和 set()

# 单一且唯一存在 (集合中无重复数据)
sets = {1, 2, 3, 4}
print({1, 2, 3, 4, 4})

# 空集合
sets_2 = set()

# 应用：字符串去重、字符串的交、差、并、补
string_new = 'nishiyigexiaokeaiGG'
string_new_2 = 'nihaishiyigexiaokeaimm'

# 去重
print(set(string_new))

a_set = set(string_new)
b_set = set(string_new_2)
print(a_set)
print(b_set)

# 交集
print(a_set & b_set)
# 差集
print(a_set - b_set)
# 并集
print(a_set | b_set)
# 补集
print(a_set ^ b_set)

# 字典: 键值对组成{key: val}
dicts = {'name': '张三', 'age': 20, 'sex': '女'}

# 取值 dicts[key]
print(dicts['name'])
# 改值
dicts['name'] = '李四'
print(dicts)
# 删
del dicts['name']
print(dicts)
# 增加
dicts['major'] = '学习'
print(dicts)

# 不同数据类型元素之间的转化

# string => number 字符串转数字
# 整型
print(int('123'))
# 浮点型
print(float('123'))

# 不能转化
# print(int('张三'))

# string => list 字符串转列表
print(list('字符串转列表'))

# string => tuple 字符串转元组
print(tuple('字符串转元组'))

# string => dict 字典格式的字符串 转字典
print(eval("{'name': '张三', 'age': 20, 'major': '说话'}"))

# 不同格式转字符串

# 字符串列表 转字符串
print(','.join(['粘防', '尽快尽快']))
# 含数值型列表 [1, 2, 3, 4.0, 5.0, '站南']
num = [1, 2, 3, 4.0, 5.0, '站南']
strs = ''
for val in num:
    strs += str(val)
print(strs)

# 字符串元组转字符串
print(','.join(tuples))
# 数值混合元组 处理方案和列表相同

# 字典转字符串
# json 引入
import json

print(json.dumps(dicts))
# 字符格式
print(type(json.dumps(dicts)))

# 集合转字符串

# 字符串集合
print(','.join({'1', '2', '3', '4'}))

# 含数值型集合
set_a = {1, 2, 3, 'sd'}
set_a_str = ''
for val in set_a:
    set_a_str += str(val)
print(set_a_str)

# 列表转集合

# # 列表先转字符串，再转集合(一般是用于列表去重)
print(set(''.join(['2', '3', '3'])))

# 集合转列表
# # 先转字符串 在转列表



