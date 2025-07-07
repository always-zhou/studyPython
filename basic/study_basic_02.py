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

# 十二、字符串常见操作(在Python中字符串是不可变的)

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

# 十五、元组

# 1、元组格式 tua=（1，2，3）可以是不同数据格式
# 2、定义元组时，如果只有一个元素，末尾要加逗号，否则返回唯一值的数据类型，多个元素用，隔开。
tua = (1,2,3,'zxw')
tua2 = ('zxw')
print(type(tua)) # <class 'tuple'>
print(type(tua2)) # <class 'str'>
print(tua[0])
# 3、元组和列表的区别
    # 1、元组只有一个元素的时候，末尾必须加 ，列表不需要
    # 2、元组只支持查询，不支持增删改
    # 3、count(),index(),len()跟列表的用法相同
    # 4、格式化输出后面的（）本质上是一个元组
    # 5、数据不可以被修改的时候使用元组，保护数据安全
name = 'zxw'
age = 27
print('%s的年龄是:%d' % (name,age))
info = (name,age)
print(type(info)) #<class 'tuple'>

# 十六、字典

# 1、基本格式：字典名：{key：value，key2:value2}
# 2、字典中的key有唯一性，值可以重复，要是key重复，只会显示一个，前面的会被覆盖
# 3、字典中没有下标

# 十七、字典的常见操作

dic = {'name':'zxw','age':27}
# 1、查看元素
    # 1、变量名[key] key不存在会报错
    # 2、变量名.get(key) key不存在会返回None
print(dic.get('sex','没有性别的kv')) # 不存在返回后面设置的默认值
# 2、修改元素
    # 1、key不存在就新增，存在就修改
dic['sex'] = 'man'
print(dic)
# 3、添加元素

# 4、删除元素
    # 1、删除整个字典 del 字典名
    # 2、删除不存在的key，会报错
    # 3、删除元素， del dic['sex']
# 5、clear() 情况字典中的kv，保留这个字典
# 6、pop（）删除指定的kv。key不存在就会报错
    # popoitem() 3.7之前的版本是随机删除一个，之后是默认删除最后一个kv
# 7、求长度 len（）
print(len(dic))
# 8、返回字典里面包含所有键名的列表 keys（）
print(dic.keys())
for i in dic:
    print(i) # 取出的也是键名
# 9、返回字典里面包含所有值的列表
print(dic.values())
# 10、返回字典里面包含所有键值对（元组形式）的列表
print(dic.items())
# 11、字典的应用场景
# 使用键值对，存储描述一个物体的相关信息

# 十八、集合

# 1、集合的基本格式 s1 = {1,2,3} 里面元素可以是不同类型
# s1 = {} 定义的是一个空字典
# s1 = set() 定义一个空集合
# 2、集合是无序的（实现方式涉及hash表），里面的元素是唯一的；可以用于元组或列表去重
# 字符串每次运行结果都不一样；数字的话，每次都是一样
# 字符串类型每次运行的hash值不同，所以在hash表位置也不同，所以无序，但是int整型的hash值就是它本身，所以不会改变
# 3、不能修改集合中的值
# 4、集合具有唯一性，可以自动去重
s1 = {1,2,3,4,2,3}
print(s1) # {1, 2, 3, 4}

# 十九、集合的常见操作

# 1、add() 添加的是一个整体
    # 1、一次只能添加一个元素
    # 2、重复的值，不会添加进去
    # 3、想要添加多个，需要用到元组
s1.add(6)
s1.add((2,3))
print(s1) # {1, 2, 3, 4, 6, (2, 3)}
# 2、update() 把传入的元素拆分，一个个放入集合中
    # 1、要放入可迭代对象，比如123，就不可以
s1.update('890')
s1.update([1,2,3])
s1.update((2,3,4))
# 3、remove() 选择数字，有就删除，没有就报错
s1.remove(1)
# 4、pop() 进行无序排列，然后将左边第一个元素删除
s1.pop()
# 5、discard() 选择元素删除，有就删，没有不进行任何操作
s1.discard(9)

# 二十、交集和并集

# 1、交集 & ,没有共有的部分会返回 set() 空集合
s2 = {1,2,3}
s3 = {4,2,5}
print(s2 & s3) # {2}
# 2、并集 ｜ 所有的元素放到一起，去重
print(s2 | s3) # {1, 2, 3, 4, 5}