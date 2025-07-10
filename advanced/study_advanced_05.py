import os
import sys
import time
import logging
import random
# 四十七、内置模块

# 1、os模块
    # 用于和操作系统进行交互
    # 通用操作：
    #     1、获取平台信息
    #     2、对目录的操作
    #     3、判断操作
print(os.name) # 正在使用的工作平台(返回操作系统类型) windows-nt linux-posix
print(os.getenv('path')) # 虚拟环境会返回None
print(os.path.dirname(r'/Users/zxw/Documents/studyPython/advanced/study_advanced_05.py')) #目录名字
print(os.path.basename(r'/Users/zxw/Documents/studyPython/advanced/study_advanced_05.py')) #文件名
# 路以/结尾，那么返回空值，如果以、结尾就会报错
print(os.path.exists(r'p')) # 判断路径(文件或目录)是否存在，存在返回True 
print(os.path.isfile(r'p')) # 判断是否存在文件
print(os.path.isdir(r'p'))  # 判断目录是否存在
print(os.path.abspath(r'p')) # 获取当前路径下的绝对路径
print(os.path.isabs(r'p')) # 判断是否是绝对路径
# 2、sys模块
    # 负责程序跟Python解释器的交互
print(sys.getdefaultencoding()) # 获取系统默认编码格式
li = sys.path                   # 获取环境变量的路径，跟解释器相关，第一项是当前所在的工作目录
for i in li:
    print(i)
print(sys.platform)             # 获取操作系统平台名称
print(sys.version)              # 获取Python解释器的版本信息
# 3、time模块
    # 三种时间表示
        # 1、时间戳(timestamp)
        # 2、格式化的时间字符串(format time)
        # 3、时间元组(strut_time)
print(time.time())  #浮点型
print(time.localtime()) # 时间元组 将一个时间戳转换为当前时区的struct_time,九个元素
print((time.localtime()).tm_year)
print(time.asctime())  # 系统当前时间，把struct_time转换成固定的字符串表达式
print(time.ctime())    # 系统当前时间，把时间戳转换成固定的字符串表达式

print(time.strftime('%Y-%m-%d',time.localtime())) # 把struct_time转换成字符串表达式
print(time.strptime('2025-04-28','%Y-%m-%d'))   # 把字符串表达式转换成struct_time

# 4、logging模块
    # 记录日志信息
    # logging中的等级
    # NOTEST 0            不设置级别，按照父logger的级别显示日志，如果是root logger，会显示所有的日志
    # DEBUG  10           程序的详细调试信息
    # INFO   20           普通信息
    # WARNING 30          警告
    # ERROR   40          程序发生错误，某些功能无法运行
    # CRITICAL(FATAL) 50  程序出现致命错误，无法运行
# 默认是warning级别的，logging只会显示级别大雨warning的日志信息
# logging.basicConfig(filename='test.log')
# logging.basicConfig(filename='test.log',filemode='w')
# logging.basicConfig(filename='test.log',filemode='w',level=logging.ERROR)
logging.basicConfig(filename='test.log',filemode='w',level=logging.ERROR,format ='%(levelname)s:%(asctime)s\t%(message)s')
    # filename：指定日志文件的文件名。所有会显示的日志都会存放到这个文件中去
    # filemode:写日志的方式，默认是a，追加 w是覆盖
    # level:指定日志的级别，默认是warning
    # format：日志信息的输出格式
logging.debug("this is a debug")
logging.info("this is a info")
logging.warning("this is a waining")
logging.error('this is a error')
logging.critical('this is a critical')

# 5、random模块
    # 用于实现各种分布的伪随机数生成器，可以根据不同的实数分布来随机生成值
print(random.random())  # 0-1之间的小数
print(random.uniform(1,2))  # 产生指定范围的随机小数
print(random.randint(1,3))  # 指定范围内的整数，左闭右闭
print(random.randrange(1,8,3))  # 产生start，stop范围内随机步长的整数，包含开头但是不包含结尾