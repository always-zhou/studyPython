# 二十一、类型转换&深浅拷贝

# 1、类型转换
    # 1、int(x) 将x转换为一个整数
        # 1、浮点型强制整型，会去掉小数点后，只保留整数部分
        # 2、只能转换由纯数字组成的字符串
        # 3、正负号只能写到前面，不然会报错
age = int(input("请输入年龄："))
if age < 18:
    print("还是少年啊")
    # 2、float(x) 将x转换为一个浮点数
        # 1、整型转为浮点型，会自动加一个小数 18.0
        # 2、正负号写到前面
    # 3、str(x) 将对象x转换为字符串
        # 1、任何类型都可以转为字符型类型
        # 2、浮点型转为字符串，会去掉末尾为0的小数部分，只保留一位小数
f1 = 1.0000
print(str(f1)) # 1.0
    # 4、eval(str) 用来计算在字符串中的有效Python表达式，并返回一个对象
        # 1、可以实现列表，字典，元组和字符串之间的转换
        # 2、非常强大，但是不够安全，容易被修改数据，不建议使用
print(eval('10+10')) # 20
    # 5、tuple(s) 将序列s转换为一个元组
    # 6、 list(s) 将序列s转换为一个列表
        # 1、支持转换的类型为：集合，字典，元组，字符串
        # 2、字典转换为列表，只取key作为列表的值
    # 7、chr(x) 将一个整数转换为一个字符
# 2、深浅拷贝（只针对可变对象，不可变对象没有拷贝的说法）
    # 1、浅拷贝：拷贝最外层的对象，内部元素只拷贝了一个引用（数据半共享）
        # 1、会创建一个新对象，拷贝第一层的数据，嵌套层会指向原来的内存地址
import copy # 导入copy模块
li1 = [1,2,3,[4,5,6]]
li2 = copy.copy(li1) 
        # 2、查看内存地址 id(),地址不一样，说明不是同一个对象
        # 3、在外层添加元素，不会被copy，再嵌套列表里面添加会被拷贝
        # 4、优点：拷贝速度快，占用空间少，拷贝效率高
print(id(li1))
    # 2、深拷贝：外层的对象和内部的元素都拷贝了一遍（数据完全不共享）
        # 1、数据变化只会影响本身。跟原来的对象没有关联
        # 2、相当于产生一个新的对象
# copy.deepcopy()
# 3、可变对象
    # 1、含义：存储空间保存的数据允许被修改（内存地址不会改变），这种数据就是可变类型
    # 2、常见的可变类型：list，set，dict
# 4、不可变对象
    # 1、含义：存储空间保存的数据不允许被修改（修改就会生成一个新的值从而分配新的内存空间），这种数据就是不可变类型
    # 2、常见的不可变类型：
    #     1、数值类型：int,bool,float,complex
    #     2、字符串 str
    #     3、元组 tuple

# 二十二、函数基础

# 1、函数
    # 1、含义：将具有独立功能的代码块组织成一个整体，使其具有特殊功能的代码集
    # 2、结构：
    #     def 函数名():
    #         函数体
    # 3、调用： 函数名()
def first_metod():
    print("first metod")
first_metod()
# 2、返回值
    # 1、函数执行结束后，最后给调用者的一个结果
    # 2、返回多个值，以元组的形式；没有返回值，是None
def second_method():
    return 'second method'
second_method()
print(second_method())
# 3、参数
    # 1、形参：定义函数时，括号里面的值；实参：调用函数时，括号里面的值
    # 2、必备参数（位置参数） 顺序和个数必须一致
    # 3、默认参数 :所有的位置参数必须再默认参数前，包括定义和调用
    #       def func(age=27)
    # 4、可变参数：传入的值的数量是可以改变的，可以传入多个，也可以不传
    #       def func(*args)  以元组的形式接收
    # 5、关键字参数
    #       def func(**kwargs)  以字典的形式接收，调用的时候，入参需要按照 kv的形式
def third_method(a,b):
    return a+b;
print(third_method(1,2))

def fouth_method(**kwargs):
    return kwargs
print(fouth_method(name='zxw',age=27))
# 4、函数嵌套 （不要再内层函数中调用外层函数，会陷入死循环，直到超过递归的最大深度）
    # 1、嵌套调用
    # 2、嵌套定义
def test01():
    print('外函数')
    def test02():
        print('内涵数')
    test02()    # 不调用，在外层函数被调用时，不会输出；调用和定义是同级的

# 二十三、函数进阶

# 1、作用域
    # 1、变量生效的范围，分为：全局变量和局部变量
    # 2、在函数内部修改全局变量的值，用关键字：global
    # 3、关键字：global（将变量声明为全局变量,也可以再局部作用域中声明一个全局变量，多个变量用逗号分割）
    # 4、关键字：nonlocal (将变量声明为外层变量（外层的局部变量，而且不能是全局变量）) 对上一层进行修改
a = 1
def five_method():
    global a
    a = 6
five_method()
print(a)
# 2、匿名函数
    # 1、语法： 函数名 = lambda 形参：返回值（表达式）
    # 2、lambda是定义匿名函数的关键字，相当于函数的def（对def的简化，一行代码，只能实现简单的逻辑）
    # 3、调用： 结果 = 函数名（实参）
add = lambda a,b:a+b
print(add(1,2))
    # 4、lambda的参数形式
        # 1、无参
noneArgs = lambda  : '无参函数'
        # 2、一个参数
oneArgs = lambda name:name
print(oneArgs("zxw"))
        # 3、默认参数 （必须写在非默认参数后）
default_args = lambda name,age=27:(name,age)
print(default_args('zxw'))
        # 4、关键字参数
keywords_args = lambda **kwargs:kwargs
print(keywords_args(name='zxw',age=18))
    # 5、lambda结合if判断
a = 1;b = 2
print('a>b') if a>b else print(a<b) # 原本的三元运算符
comp = lambda c,d : 'c>d' if c>d else 'c<d'
print(comp(2,3))
# 3、内置函数
    # 1、查看所有的内置函数
import builtins
print(dir(builtins)) # 大写字母开头一般都是内置常量名，小写字母开头一般都是内置函数名
    # 2、abs():返回绝对值
    # 3、sum():求和 
        # 1、要放可迭代对象（字符串/字典也不可以进行相加）
        # 2、运算时，只要有一个浮点数，结果就是浮点型
    # 4、min() 求最小值
print(min(-3,4,key=abs)) # 传入绝绝对值函数，就先求绝对值再比较大小
    # 5、max() 求最大值
    # 6、zip() 将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
        # 1、输出的是一个元组对象
        # 2、输出方式：1、for循环；2、转换为列表打印（必须是可迭代对象）
li1 = [1,2,3]
li2 = ['1','2','3']
print(list(zip(li1,li2))) 
for i in zip(li1,li2):
    print(i)    # 如果元素个数不一样，按照长度最短的返回
    # 7、map() 可以对可迭代对象中的每一个元素进行映射，分别取执行
        # 1、map（func，iterl）自己定义的函数，可迭代对象
        # 2、只要写函数名
def funa(a):
    return a*5
res = map(funa, li1)
print(list(res))        
    # 8、reduce() 对参数序列中元素进行累积
        # 定义：先把函数中的两个元素拿出来，计算然后保存起来，和后一个元素进行计算，依次执行
        # 1、需要先导包 from functools import reduce
        # 2、reduce（func，iterl）函数：必须是两个参数的，可迭代对象
test02 = lambda a,b:a+b
from functools import reduce
print(reduce(test02, li1))
# 4、拆包
    # 1、对于函数中的多个返回数据，去掉元组，列表或字典 直接获取里面数据的过程
        # 1、方法1:直接根据个数去接收，要求对象内有多少数据，就要定义多少个变量接收
a,b,c=li1
print(a,b,c) # 1 2 3
        # 2、先把单独的取完，其他剩下的都交给带*的变量,一般在函数调用时使用
a,*b = li1
print(a,b) # 1 [2, 3]

# 二十四、异常

# 1、抛出异常 raise
# raise Exception("一个异常信息")
def login():
    pwd = input("请输入密码：")
    if len(pwd) <= 6:
        return "login success!"
    raise Exception("login fail,pwd len is lt 6")
# print(login())
# 2、捕获异常
try:
    print(login())
except Exception as e:
    print(e)

# 二十五、模块

# 1、含义：一个py文件就是一个模块，即导入一个模块本质上就是执行一个py文件
# 2、分类
    # 1、内置模块 random,time,os,logging 直接导入即可使用
    # 2、第三方模块（第三方库）
        # macos 下载不能用 pip install 模块名。会报错。推荐使用虚拟环境
        # python3 -m venv venv # 创建名为venv的虚拟环境
        # source venv/bin/activate # 激活虚拟环境
        # pip install 模块名
        # deactivate # 完成后 退出虚拟环境
    # 3、自定义模块 
        # 1、注意命名规范，不要与内置模块起冲突
# 3、import （导入模块）    可以一个import导入多个模块，但最好一个模块单独使用一个import
    # 1、方式一：
    #     import 模块名    
    #     调用的话直接：模块名.功能名
    # 2、方式二：
        #  from 模块名 import 功能1，功能2...  # 导入的函数只需要函数名，不需要小括号
        # 调用的话：直接 功能名
    # 3、方式三：
        # from 模块名 import *  把模块中的所有内容全部导入
    # 注意：不建议过多的使用from...import...声明，有时候命名冲突会造成一些错误 一般会选择最后一个
# 4、as给模块起别名
    # 1、语法：import 模块名 as 别名
# 5、as给功能起别名
    # 1、语法 from 模块名 import 功能 as 别名 （导入多个功能用逗号隔开，后面的功能也可以取别名）
# 6、内置全局变量 __name__
    # 1、语法：     if __name__ = '__main__':
    # 2、作用：用来控制py文件在不同的应用场景执行不同的逻辑
    # 3、文件在当前程序执行（即自己执行自己）：__name__ = "__main__"
    # 4、文件被当作模块被其他文件导入： __name__ = 模块名
    # 注意： 被当作模块导入时，__name__ = "__main__" 下面的代码不会被显示出来

# 二十六、包（项目结构中的文件夹/目录）

    # 1、与普通文件夹的区别：包是还有__init__.py的文件夹
    # 2、作用：将有联系的模块放到同一个文件夹下，有效地避免模块名称冲突问题，让结构更清晰
    # 注意：import导入包时，首先执行__init__.py文件的代码
    #      不建议在init中编写python模块，尽量保证init的内容简单
    # 3、__all__ ：本质上是一个列表，列表里面的元素九代表要导入的模块。 作用：可i控制要引入的东西
    # 4、包的本质上依然是一个模块，包可以包含包

# 二十七、递归函数

# 1、含义：如果一个函数在内部不调用其他的函数，而是调用它本身的话，这个函数就是递归函数
# 2、条件：
#     1、必须有一个明确的结束条件 --递归的出口
#     2、每进行更深一层的递归，问题规模相比上次递归都要有所减少
#     3、相邻两次重复之间有紧密的联系
# 3、优点：简洁
# 4、缺点：使用递归函数的时候，需要反复调用函数，耗内存，运行效率低
# 例子：实现1-100的和
# 普通函数实现：
def add():
    res = 0
    for i in range(1,101):
        res += i
    return res
print(add())
# 递归函数实现：
def add_01(n):
    if n == 1:
        return 1
    return n+add_01(n-1)
print(add_01(100))

# 斐波那契数列 1，1，2，3，5，8，13.....
def add_02(n):
    if n <= 1:
        return n
    return add_02(n-2) + add_02(n-1)
print(add_02(3))    # 2

# 二十八、闭包

# 1、含义：再嵌套函数的前提下，
#         内部函数使用了外部函数的变量，
#         而且外部函数返回了内部函数，我们就把使用了外部函数变量的内部函数称为闭包
# 简单的闭包函数
def outer():
    liu = 10
    def inner():
        print(liu)
    return inner
print(outer()) # 返回的是内部函数的内存地址
# 调用方法：
    # 1、outer()()   # 10
    # 2、wai = outer(); wai() # 10
# 2、带参数的时候如何调用
def outer(m):
    n = 10
    def inner(c):
        print(m+n+c)
    return inner  # 返回函数名，而不是带小括号，因为inner函数里面参数比较多时或者说受到限制时，写法不规范
outer(1)(2)    # 13
# 3、函数引用
    # 1、print(函数名) 函数名里面保存了函数所在位置的引用
    # 2、id() 显示变量的内存地址
ww = 1; mm = 2; 
print(id(ww)) # 4310278304 内存地址
print(id(mm)) # 4310278336
# 4、每次开启内涵数都在使用同一份闭包变量

# 总结：使用闭包的过程中，一旦外函数被调用一次，返回了内涵数的引用，虽然每次调用内函数，会开启一个函数，执行后消亡
# 但是闭包变量实际上只有一份，每次开启内函数都在使用同一份闭包变量

# 二十九、装饰器

# 1、含义：装饰漆本质上是一个闭包函数，它可以让其他函数在不需要做任何代码改动的前提下增加额外功能，装饰器的返回值也是一个函数对象
# 2、装饰漆需要满足两点：
    # 1、不修改原程序或函数的代码
    # 2、不改变函数或程序调用方法
# 3、标准版装饰器 （装饰器的原理就是将原有的函数名重新定义为以原函数为参数的闭包）
def send():
    print("send message")

def outer(fn):  # fn 是形参
    def inner():
        print("login into gthub")
        # 执行被装饰的函数
        fn()
    return inner

ot = outer(send)
ot()
# 4、装饰糖
    # 1、格式： @装饰器名称
def outer(fn):  # fn 是形参
    def inner():
        print("login into gthub")
        # 执行被装饰的函数
        fn()
    return inner    

@outer  # 装饰器的名称 不要加上小括号，前者是引用，后者是调用函数，返回该函数要返回的值
def send():
    print("send message")
send()
# 5、被装饰的函数有参数
def outer(fn):  
    def inner(name):
        print(f"{name}login into gthub")
        fn(name)
    return inner    

@outer  
def send(name):
    print("send message")
send('zxw')
# 6、被装饰的函数有可变参数 *args **kwargs
def outer(fn):  
    def inner(*args,**kwargs):
        print(args)
        print(kwargs)
        fn(*args,**kwargs)
    return inner    

def send(*args,**kwargs):
    print("send message")
outer(send)('zxw',name='wm')
# 7、多个装饰器
    # 1、装饰的过程，离函数最近的装饰器先装饰，然后外面的装饰器在进行装饰，由内而外  如下面就是先 outer再outer2
def outer(fn):  
    def inner(name):
        print(f"{name}login into gthub")
        fn(name)
    return inner    
def outer2(fn):  
    def inner(name):
        print(f"{name}login out gthub")
        fn(name)
    return inner 
@outer2
@outer  
def send(name):
    print("send message")
send('zxw')
