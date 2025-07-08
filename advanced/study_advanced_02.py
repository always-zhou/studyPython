# 三十八、文件读写

# 1、基础操作
# 文件就是存储在某种长期储存设备上的一段数据
    # 操作；打开文件-》读/写文件 -〉关闭文件
    # 文件对象的方法：
        # open()：创建一个file对象，默认是以只读模式打开
        # read(n):n表示从文件中读取的数据的长度，没有传n值就默认一次性读取文件的所有内容
        # write();将指定内容写入文件
        # close()：关闭文件
    # 属性
        # 文件名.name：返回要打开的文件的文件名，可以包含文件的具体路径
        # 文件名.mode:返回文件的访问模式
        # 文件名.closed：检测文件是否关闭，关闭就返回True

# f = open('test.txt') # 注意脚本执行的目录，如果文件不在脚本执行的目录，会报错
# f = open('/Users/zhouxianwen/Documents/studyPython/advanced/test.txt') # 获取写全路径
# print(f.name)
# print(f.mode)
# print(f.closed)
# f.close()   # 打开文件后记得关闭文件

# 2、读写操作
    # read(n):读取文件
    # readline():一次读取一行内容
    # readlines():按照行的方式一次性读取全部内容
    # write():写入内容
# f = open('test.txt')
# print(f.read())
# print(f.readline())
# print(f.readlines())
# f.write('hahahha')  这里不加文件的访问模式，默认是只读的模式，所以会报错，不可以写
# f.close()

    # 访问模式：
        # 模式    可做操作    若文件不存在    是否覆盖
        # r         只能读      报错           -
        # r+        可读可写     报错          是
        # w         只能写       创建          是
        # w+        可读可写     创建（先写后读）          是
        # a         只能写       创建          否，追加写
        # a+        可读可写      创建         否，追加写
        # 读取图片 模式是 rb    写入图片是 wb
# f = open('test.txt','r+') # 从开始位置开始写
# f = open(÷'test.txt','a+')   # 追加写
# f = open('test.txt','w+')   # 这种模式，写完直接read是读不出任何东西的，因为文件指针再最后位置
# f.write('family') 
# f.close()
    # 文件指针：标记从哪个位置开始读取数据
    # 文件定位操作
        # tell():显示文件内当前位置，即文件指针当前位置
        # teek(offset,whence):移动文件读取指针到指定位置
        #                     offset：偏移量，表示要移动的字节数
        #                     whence:起始位置，表示移动字节的参考位置，默认是0表示文件开头做参考位置，1是当前位置，2是文件末尾位置。seek(0,0)就是文件的开头
# f= open('test02.txt','w+')
# f.write("hello Python")
# print('first:',f.read()) # 先写后读模式读不出来的，因为现在文件光标在文件末尾，就是写入内容的长度
# f.seek(0,0) # 移动文件光标位置到文件开头
# print(f.read())
# f.close()
# with open('test02.txt','r') as f: # 这种方式，里面自带关闭文件
#     print(f.tell())
#     print(f.read())
# print(f.closed) 
# 3、编码格式
    # windows默认编码是GBK,所以需要加上编码格式。但是mac或者linux则不需要
with open('test.txt','a+',encoding='utf-8') as f: # 这种方式，里面自带关闭文件
    # f.write('你好啊')
    print(f.tell())
    print(f.read())
print(f.closed) 

# 4、目录常用操作
    # 导入模块 import os
    # 文件重命名：os.name(旧文件名，新文件名)
    # 删除文件:os.remove(旧文件名)
    # 创建文件夹:os.mkdir(文件夹名)
    # 获取当前目录:os.getcwd()
    # 获取目录列表:os.listdir(目录)
    # 删除文件夹:os.rmdir(文件夹名)
import os
# os.rmdir('test11')
print(os.listdir('../')) # 获取上一级目录的列表

# 三十九、迭代器

# 可迭代对象：Iterable
# 可迭代对象的条件：
#     1、对象实现了__iter__()方法
#     2、__iter__()方法返回了迭代器对象
# for循环的工作原理：
    # 1、先通过__iter__()获取可迭代对象的迭代器
    # 2、对获取到的迭代器不断调用__next__()方法来获取下一个值将其赋值给临时变量i
# isinstance()
    # 判断一个对象是否是可迭代对象或者是一个已知的数据类型
    # 两个参数 o：对象，t：类型，可以是直接或者间接类名，基本类型或者元组
    # 需要导入模块
from collections.abc import Iterable,Iterator

# print(isinstance('123',(int,dict))) # False

# list = [1,2,3,4]
# li = list.__iter__()
# print(li)
# print(li.__next__())
name = 'zxw'
name2 = iter(name)
print(isinstance(name,Iterable))
print(isinstance(name2,Iterable))
print(isinstance(name,Iterator))
print(isinstance(name2,Iterator))
print(dir(name))
print(dir(name2))
# 总结：
    # 能够for循环的都是可迭代对象
    # 能够作用于next()的都是迭代器
    # 迭代器对象一定是可迭代对象
    # 可迭代对象可以通过iter()转换成迭代器对象
    # 如果一个对象拥有__iter__()就是可迭代对象,如果用__iter_()和__next__()是迭代器对象
    # dir()方法可以查看对象的属性和方法
# 迭代器协议
    # 对象必须提供一个next方法，执行该方法要么就返回迭代中的下一项，要么就引发StopIteration异常，来终止迭代
# 自定义迭代器类
    # 两个属性：__iter__()和__next__()
class myIterator(object):
    a = 0 
    def __iter__(self):
      return self    
    def __next__(self):
      if self.a == 10:
         raise StopIteration('stop stop stop')
      self.a += 1
      return self.a
tt = myIterator()
for i in tt:
   print(i)

# 四十、生成器

# Python中一边循环一遍计算计算的机制：generator
# 生成器表达式
    # 列表推导式：[i*5 for i in range(5)]
    # 生成器表达式：(i*5 for i in range(5))
aaa = (i*5 for i in range(5))
for i in aaa:
   print(i)
# 生成器函数
    # 使用了yield关键字的函数就是生成器函数
    # yield的作用：使函数中断，并保存中断的状态
        # 1、类似retun，将指定值或多个值返回调用者
        # 2、yield语句一次返回一个结果，在每个结果之间，挂起函数，执行next()，再重新从挂起点继续往下执行
def test66():
   yield 1
   yield 2
   yield 3
vv = test66()
print(next(vv)) # 1
print(next(vv)) # 2
print(next(vv)) # 3 

# 三者的关系
# 可迭代对象：实现了Python迭代协议，可以通过for..in..循环遍历对象，比如list、dict、str...迭代器、生成器
# 迭代器：可以记住自己遍历位置的对象，直观体现就是可以使用next()函数返回值，迭代器只能往前，不能往后，当遍历完毕后，next()抛出异常
# 生成器：特殊的迭代器，需要注意迭代器并不一定是生成器，它是Python提供的通过简便的方法写出迭代器的一种手段
# 包含关系：可迭代对象>迭代器〉生成器

