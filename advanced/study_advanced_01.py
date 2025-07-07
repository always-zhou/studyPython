# 三十、面向对象基础

# 1、面向对象
# 面向过程：就是先分析出解决问题的步骤，再把步骤拆成一个个方法，是没有对象去调用的，通过一个个方法执行解决问题
# 面向对象：将编程当成是一个事物（对象），对外界来说，事物是直接使用的，不用去管内部的情况，而编程就是设置事物能做什么事情
# 2、类和对象
# 类：对一系列具有相同属性和行为的事物的统称（三要素：类名、属性、方法）
    # 基本格式：
    # class 类名（遵循大驼峰命名法）：
    #     代码块
# 对象：类的具体表现，是面向对象编程的核心
    # 实例化（创建）对象的格式：
    # 对象名 = 类名（）
# 注意：1、先有类，再有对象。2、类只有一个，对象可以有多个
# 3、实例方法：
#   由对象调用，至少有一个self参数，执行实例方法的时候，自动将调用该方法的对象赋值给slef
class Test01:
    age = 27
    def name(self): # self参数是类中的实例方法必须具备的，代表对象本身，当对象调用实例方法的，Python
                    # 会自动将对象本身的引用作为参数，传递到实例方法的第一个参数self里面
     print("第一个实例方法！")
method01 = Test01()
method01.name()
# 4、实例属性
class Test02:
    sex = 'man'
    def method(self):
       print(f'{Test02.sex}永远是,{self.age}岁') # self.age 就是实例属性
new = Test02()
new.age = 18
new.method()       
# 类属性和实例属性的区别：
    # 类属性属于类，是公共的，大家都能访问到，实例属性属于对象，是私有的只能对象名访问。
# 5、构造函数 __init__()
    # 1、作用：通常用来做属性初始化或者赋值操作
    # 2、注意：在类实例话对象的时候，会被自动调用
class Test03:
   def __init__(self): # 构造函数
     self.name = 'zxw'
     self.age = 27
   def play(self):
      print(f'{self.name}')
   def study(self):
      print(f'{self.age}')
new02 = Test03()
new02.play();new02.study()

class Test04:
   def __init__(self, name, age):
     self.name = name
     self.age = age
   def play(self):
      print(f'{self.name}')
   def study(self):
      print(f'{self.age}')
new03 = Test04('zxw',28)
new03.play();new03.study() 
# 6、析构函数 
    # __del__方法：是对象被垃圾回收的时候起作用的一个方法，
                # 它的执行一般也就意味着对象不能继续引用，回收内存
class Test05:
   def __init__(self):
     print('init method')
   def __del__(self):
      print("last time") # 最后执行
new04 = Test05()
# del new04     # 执行语句的时候，内存立即被回收，会调用对象本身的__del__方法
print("haihahai")

# 三十一、封装&单继承

# 1、封装
    # 指的是隐藏对象中一些不希望被外部所访问到的属性或者方法
    # 1、隐藏属性（私有权限）：只允许在类的内部使用，无法通过对象访问
        # 在属性名或者方法名前面加上两个下划线 __
        # 隐藏属性实际上是将名字修改为：_类名__属性名
        # 子类无法继承
        # 这种命名一般是Python中的魔术方法或属性，都是有特殊含义或者功能的，一般不要轻易定义
class Test06:
   name = 'zxw'
   __age = 27   # 隐藏属性
   def liu(args):
    print(f'{args.name},{args.__age}') # 取出隐藏属性的另一个方法，常用
new05 = Test06()
print(new05.name)
print(new05._Test06__age) # 取出隐藏属性的办法,一般不使用
new05.liu()
    # 2、私有方法/属性
        # 单下划线开头，定义在类中，外部可以使用，子类可以继承，一般再另一个py文件
        # 通过 from xxx import * 导入时，无法导入
class Test07:
   name = 'zxw'
   _age = 27
new06 = Test07()
print(new06._age) # 使用对象名._属性名调用

class Test08:
   def __ww(self):
      print('隐藏方法')
   def mm(self):
      print("普通实例方法")
      self.__ww()   # 在实例方法中调用隐藏方法
   def _liu(self):
      print('私有方法')
new07 = Test08()
new07._liu()    #  调用私有方法
new07.mm()
# 2、继承(单继承/多继承)
    # 1、语法
    # class类名（父类名）:
    #     代码块...
    # 2、单继承
class Test09(Test08):
   def name(args):
    pass    #  pass是一个占位符，不写任何东西，会自动跳过，不会报错
new08 = Test09()
new08.mm()
    # 3、多重继承
        # 子类拥有父类以及父类的父类中的属性和方法
    # 4、多继承
        # 子类可以拥有多个父类，并且具有所以父类的属性和方法
class Test13(Test01,Test02):
   pass
        # 如果多个父类中存在同名的方法，会先选择离得最近的一个父类调用
        # 如果在当前类中找到了方法，就直接执行，不再搜索
        # 多继承的弊端：1、容易引发冲突；2、会导致代码设计的复杂度增加
    # 5、方法中的搜索顺序(了解)
        # __mro__ 可以查看方法搜索顺序 print(Test13.__mro__)
# 3、方法的重写
    # 1、如果从父类中继承的方法不能满足子类的需求，可以在子类中重写父类的方法
    # 这个过程称为 方法的覆盖或方法的重写
class Test10:
   def name(args):
    print("一个method")
class Test11(Test10):
   def name(args):   # 方法重写
      print("另一个方法")
new09 = Test11()
new09.name()
    # super（） 是super类，实例化的一个对象
class Test11:
   def name(args):
    print("一个method")
class Test12(Test11):
   def name(args):   # 方法重写
      Test11.name(args) # 调用父类的方法（方法一）
      super().name()    # 调用父类的方法（方法二）推荐这种
      super(Test12,args).name() # 调用父类的方法（方法三）
      print("另一个方法")
new09 = Test12()
new09.name()
# 4、新式类写法
    # 1、派生类，子类中有不同于父类的方法/属性
    # 2、class A（object） 新式类：继承了object类或者该类的子类都是新式类 --推荐使用
        # object  --对象，pyhton为所有对象提供的基类（顶级父类），提供了一些内置的属性和方法，可以用dir()查看
    # 3、Python3中如果一个类没有继承任何类，默认都是继承了object，所以都是新式类

# 三十二、多态

# 1、含义：一个对象具有多种形态，在不同的使用环境中以不同的形态展示其功能，就称该对象具有多态特征
# 2、前提：继承、重写
# 3、特点：
    # 1、不关注对象的类型，关注对象具有的行为，也就是对象的实例方法是否同名
    # 2、好处就是增加代码的外部调用灵活度，让代码更加通用，兼容性比较强
    # 3、不同的子类对象，调用相同的父类方法，会产生不同的执行结果
# 4、多态性：一种调用方式，不同的执行结果
class Test13:
   def name(args):
    print('zzzzzzz')
class Test14(Test13):
   def name(args):
    print('xxxxxxx')
class Test15(Test13):
   def name(args):
    print('wwwwwww')
def name(args):
   args.name()
a = Test13()
name(a)
b = Test14()
name(b)
c = Test15()
name(c)

# 三十三、静态方法

# 1、使用@staticmethod装饰的方法,没有self，cls参数的限制
# class类名：
#     @staticmethod
#     def 方法名(形参):
#      方法体
# 2、调用格式：类名.方法名(形参)
class Test16:
   @staticmethod
   def cv():
    print('一个静态方法')
Test16.cv()
new10 = Test16()
new10.cv()
# 3、作用：
    # 1、取消不必要的参数传递，有利于减少不必要的内存占用和性能消耗

# 三十四、类方法

# 1、含有：使用@classmethod来标识的类方法，对于类方法，第一个参数必须是类对象，
#         一般是以cls作为第一个参数
# class类名：
#     @classmethod
#     def 方法名(cls,形参):
#      方法体
# 2、类方法内部可以访问类属性，或者调用其他的类方法
# 3、当方法中需要使用到类对象(如访问私有类属性)，定义类方法。类方法一般配合类属性使用
class Test17:
   age = 27
   @classmethod
   def name(cls):
    print('cls:',cls) # cls就是类对象本身，类本身上就是一个对象
    print("一个类方法")
    print('%d:' % cls.age)
Test17.name()

# 总结：实例方法可以访问类属性和实例属性，静态方法和类方法不能访问实例属性
        # 因为类属性是公共的，实例属性是私有的
        # 静态方法不需要访问类属性，因为和类、对象没有关联


# 三十五、__init__（） 和 __new__()
    # __new__() ：object基类提供的内置的静态方法
    # 作用：1、在内存中为对象分配内存空间；2、返回对象的引用
class Test18:
   def __init__(self):
     print("__init__")
   def __new__(cls):      # __new__()是静态方法，形参里面有cls，实参就必须传cls
      print("__new__()")
      res = super().__new__(cls) # res保存的是实例对象的引用
      return res                   
new11 = Test18() # 先调用new 再调用init
# 注意：重写__new__()一定要return super().__new__(cls)，否则pthon解释器
    #    得不到分配的内存空间的对象引用，就不会调用__init__()
# 总结：
#   1、__new__()是创建对象，__init__（）是实例化对象   
#   2、__new__()是返回对象的引用，__init__（）是定义实例属性   
#   3、__new__()是类级别的方法，__init__（）是实例级别的方法   

# 三十六、单例模式

# 1、可以理解为一个特殊的类，这个类只存在一个对象
# 2、优点：节省内存空间，减少不必要的资源浪费
# 3、缺点：多线程访问的时候容易引发线程安全问题
# 4、方式：
#     1、通过@classmethod
#     2、通过装饰器实现
#     3、通过重写__new__()实现(重点)
#     4、通过导入模块实现
# 5、设计流程
#     1、定义一个类属性，初始值是None，用来记录单例对象的引用
#     2、重写__new__()方法
#     3、进行判断，如果类属性是None，把__new__()返回的对象引用保存进去
#     4、返回类属性中记录的对象引用
# 重写__new__()方法实现单例模式
class Test19:
   obj = None
   def __new__(cls):
      if cls.obj == None:
         cls.obj =  super().__new__(cls)
      return cls.obj
gg = Test19()
hh = Test19()
print(gg)
print(hh)
# 第四种实现单例模式
# from 文件 import 对象名 as 别名
# from 文件 import 对象名 as 别名1
# 这样使用的拿到都是同一个对象（模块就是天然的单例模式）
# 6、应用场景
    # 1、回收站对象
    # 2、音乐播放器：一个音乐播放软件负责播放的对象只有一个
    # 3、开发游戏设计 场景管理器
    # 4、数据库配置、数据库连接池的设计

# 三十七、魔法方法/属性

# 1、__xx__()函数叫做魔法方法，指的是具有特殊功能的函数
# 2、常见的魔法方法/魔法属性：
    # 1、__new__()：在内存中为对象分配空间并返回对象的引用
    # 2、__init__()：初始化对象或给属性赋值(构造函数)
    # 3、__doc__:类/函数的描述信息、
    # 4、__module__：表示当前操作对象所在模块
    # 5、__class__：表示当前操作对象所在的类
    # 6、__str__()：对象的描述信息
    # 7、__del__()：删除对象（析构函数）
    # 8、__call__()：使一个实例对象成为一个可调用对象
        # 可调用对象：函数/内置函数和类都是可调用对象，凡是可以把一对()应用到
                  # 某个对象身上都可以称之为可调用对象 callable()可以判读是否是可调用对象
        # 调用一个可调用的实例对象，其实就是在调用它的__call__()方法
    # 9、__dict__：返回对象具有的属性和方法
class Test20:
   """类的描述信息"""
   sex = 'man'
   def name(args):
    print('just test')
res = Test20()
print(Test20.__doc__)
print(res.__module__)
print(res.__class__)
print(res.__str__())
print(Test20.__dict__)
