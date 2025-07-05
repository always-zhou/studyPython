print("Hello Python")

# 一、变量

num1 = 1
num2 = 2
total = num1 + num2
print(total)

# 二、标识符

# 1、只能由数字，字母，下划线（_）组成
    # python3可以用中文命名，但是不推荐
    # 标识符被包在（）内对标识符本身没有影响
中文 = "哈哈"
print(中文)
(zxw) = 27
print(zxw)
print((zxw))
# 2、不能是关键字

# 三、数值类型

# 1、数值（number）：
#       整数 int ：任意大小的整数
#       浮点型 float ：小数
#       布尔型 bool ：（固定写法）True/Flase 可以当作整数对待，True=1 False=0
#       复数 complex ：（固定写法）z = a + bj -- a是实部 b是虚部 j是虚数单位 1+2j

# 四、字符串

    # 1、加上引号，单双引号都可以，包含了多行内容的时候也可以使用三引号
    # 注意多行注释和三引号的字符串类型的区别，因为多行注释也是三引号


# 五、占位符

    # 1、占位符的作用：生成一定格式的字符串
    # 2、占位符的三种方式：
    # %; 
    # format(); 
    # 格式化 f
# %s 字符串（常用）
name = '周小文'
print("my name is: %s" % name)
# %d 整数（常用）
age = 27
print("my name is: %s, age is: %d" % (name, age))
# %4d 整数：前面数字表示位数，不足会补空白，或者设置为0补全，超出的按照原位数输出
print("%4d", age) # 空白
print("%04d", age) # 0补全
# %f 浮点数（常用）：默认后六位小数，遵循四舍五入的原则
pai = 3.14
print('%f' % pai) # 3.140000
# %.2f 设置小数点后位数
print('%.1f' % pai) # 3.1
# %% 占位符
print('I am%%a%% man' % ())
# f 格式化输出 f "{}"
print(f'my name is {name}, age is {age}')

# 六、运算符

# 1、算数运算符
    # 使用运算符 / 商一定是浮点数，且除数不能为0
    # // 取商的整数部分，向下取整，不管四舍五入原则，小数全部舍掉
    # % 取余数的位数
    # ** 幂 m**n m的n次方
    # 如果有浮点数，结果也会用浮点数表示 如 5.0/2 = 2.0； 1.0+1 = 2.0
# 2、运算符优先级
    # 先乘除后加减
    # 同级运算符从左往右计算
    # 可以用（）调整计算的优先级
    # 幂是最高优先级的 幂 > 乘、除、取余、取整数> 加减
math1 = 5
math2 = 2
print(math1 // math2) # 2
print(math1 % math2)  # 1
print(math1 ** math2)  # 25
# 3、赋值运算符（针对变量存在）
    # =
    # +=、-=  a+=1 等效于 a = a + 1
# 4、比较运算符 == ; ！= ; > ; <
# 5、逻辑运算符 and or not（非）
# 6、三目运算（三元表达式）if else
a = 2;b=1
print('a大于b')if a >= b else print('a小于等于b')

# 七、输入函数

# 1、input输入函数 里面的参数是prompt 是提示，会在控制台显示
    # 输入的默认为 字符串
input("请输入你的梦想：")

# 八、转义字符

# 1、\t 制表符 通常表示空四个字符，也称缩进
# 2、\n 换行符
# 3、\r 回车 表示将当前位置移到本行开头
print('abc\rzxw') # zxw
# 4、\\ 反斜杠符号
# 5、r 原生字符串表示不转义
print(r'abc///tzxw') # abc///tzxw

# 九、if相关

# 1、if判断
score = input("请输入你的考试分数：")
if score == '100':
    print("你很棒棒哦！！！")
if score == '60':
    print("继续加油吧")
# 2、if-esle 判断结构
    # 1、if-else 二选一
    # 2、if-elif 多选一 最后可以用else表示都不符合的条件
# 3、if嵌套
always = 27
time = True
if time == True:
    print("begin study python->",end="")
    if 18 <= always <= 30:
        print("不小啦")
    else:
        print("那时年少")
else:
    print("who you are?")

# 十、循环语句

# 1、while循环(记得写改变变量，避免死循环)
a = 0
i = 1
while i <= 100:
    a+=i
    i+=1
print(a)
# 2、while循环嵌套
# 3、for循环 （字符串是可被迭代对象）
# 基本格式
# for 临时变量 in 可迭代对象：
    # 循环满足条件时可执行的代码
str = 'hello Python'
for item in str:
    print(item)
# 4、range() 函数 用来记录循环的次数，相当于一个计数器 
# 三个参数（start，stop，step）可以写任意参数 只写一个，代表循环的次数
for item in range(1,6): # 左闭右开 只打印1-5
    print(item) 
# 4、break和continue
    # 只能放到循环内
    # continur前一定要修改计时器，否则会死循环,如 i+=1
for item in range(1,5):
    if(item == 2):
        i+=1
        continue
    print(item)