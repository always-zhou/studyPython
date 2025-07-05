# 十一、字符串编码

# 本质上就是二进制数据与语言文字的一一对应关系
# Unicode：所有字符都是2个字节
# 优点：字符与数字之间转换速度更快一些
# 缺点：占用空间大
# UTF-8: 精准，对不同的字符用不同的长度表示
# 优点：节省空间
# 缺点：字符与数字之间转换速度较慢，每次都要计算字符要用多少个字节来表示

# 1、字符串编码转换
#     encode() 编码
#     decode（）转码

# 十二、字符串常见操作(再Python中字符串是不可变的)

# 1、字符串运算符
    # + 字符串拼接
str1 = '文文'
str2 = '明明'
str3 = '文明老六'
str4 = '老六'
print(str1, str2) # 文文 明明
print(str1, str2, sep='') # 文文明明
    # * 字符串重复输出
print('文明\n'*5) # 
# 2、成员运算符 in/ not in
print(str1 in str2) # False
# 3、下标/索引 从零开始，从左往右。 倒过来是从-1开始
print(str3[0]) # 文
print(str3[-1]) # 六
# 4、切片 
    # 1、语法【起始：结束：步长】包前不包后原则
    # 2、步长表示选取的间隔，不写步长默认是1
    # 3、步长绝对值大小决定切取数据间隔，正负号决定切取的方向
print(str3[0:3])
print(str3[0:])
print(str3[:6])
print(str3[:-1]) #文明老
print(str3[-3:-1]) #明老
# print(str3[-1::-1]) #六老明文
# 5、find 检测 字符是否包含在字符串中 
    # 1、语法 find(子字符串，开始位置下标，结束位置下标)
    # 2、存在返回开始下标，不存在则-1
    # 3、包前不包后原则
print(str3.find(str2)) # -1
print(str3.find(str4)) # 2
print(str3.find(str3,1)) # -1
# 6、count 返回出现的次数
    # 1、返回子字符串在字符串出现的次数，没有则输出0
    # 2、包前不包后原则
print(str3.count(str4)) # 1
print(str3.count(str4,1,2)) # 0
print(str3.count(str2)) # 0
# 7、replace 替换
    # 1、语法 （old，new，connt）要被更换的字段串，新字符串，替换的次数，默认是-1，所有匹配项
print(str3.replace('六','X')) # 文明老X
# 8、split 分割
    # 1、参数sep和maxsplit sep：分隔符，默认是任意空白字符 空格，换行，制表符。maxsplit：最大分割次数，默认-1
    # 2、以列表的形式返回
    # 3、不包含分割内容，则返回一个整体
str5 = 'hello Python'
print(str5.split()) # ['hello', 'Python']
print(str5.split('o')) # ['hell', ' Pyth', 'n']
# 9、index 和find作用一样，但是会报异常
    # 1、语法 index(子字符串，开始位置下标，结束位置下标)
    # 2、包前不包后原则
# print(str3.index(str2)) # 找不到报错
print(str3.index(str4)) # 2
# 10、capitalize 第一个字符大写
# 11、startswith 是否是某字符开头的
print(str5.startswith('h')) # true
print(str5.startswith('h',1,3)) # False
# 12、endswith 是否是某字符结束
# 13、lower 大写字符转为小写
print(str5.lower())
print(str5.islower()) # 是否是小写 False
# 14、upper 小写字母转为大写
print(str5.upper())


# 十三、列表

# 1、一个列表中的元素可以各不相同
list = [1,2,3,'列表']
print(list,type(list)) # [1, 2, 3, '列表'] <class 'list'>
# 2、列表可以进行切片操作
print(list[1:3]) # [2, 3]
# 3、列表是可迭代对象
for item in list:
    print(item)
 
# 十四、列表的相关操作

# 1、添加元素 
    # append() 整体添加到后面
list.append('append')
print(list)
    # extend() 分割成一个个元素添加进去
list.extend('666')
# list.extend(1) # 报错 要添加可迭代元素，整型不是可迭代对象
print(list)
    # insert() 从指定的位置添加进去，如果原有位置存在元素中，则原有的后移
list.insert(1,6)
print(list)

# 2、修改元素
    # 1、通过下标修改
list[1] = 'fix'
print(list)
# 3、查找元素
    # 1、in
    # 2、not in
    # 3、index 不存在的话，会报错
    # 4、count
# 4、删除元素
    # 1、del
        # del list 删除列表
        # del list[0] 删除指定下表的元素
del list[0]
print(list)
    # 2、pop 删除指定下表的元素，不能超出下标，会报错，Python3版本默认回删除最后一个元素
list.pop()
print(list)
list.pop(0)
print(list)
    # 3、remove 根据元素的值进行删除,不存在也会报错。默认会删除最开始出现的元素
list.remove('append')
print(list)
# 5、排序
    # 1、sort 将列表按特定的顺序重新排列，默认从小到大
num_list = [4,2,5,1]
num_list.sort()
print(num_list) # [1, 2, 4, 5]
    # 2、reverse 将列表倒叙
list.reverse()
print(list)
# 6、列表推导式
    # 1、写法 
    # 【表达式 for 变量 in 列表】  in后面不仅可以放列表，还可以放range(),可迭代对象
test_list = []
[test_list.append(i) for i in range(1,6)]
print(test_list)
    # 【表达式 for 变量 in 列表 if 条件】
test_list1 = []
[test_list1.append(i) for i in range(1,6) if i%2>0]
print(test_list1)
# 7、列表嵌套
test_list3 = [1,2,3,[4,5,6]]
print(test_list3[3]) # [4, 5, 6]
print(test_list3[3][0]) # 4
