# 四十一、进程

# 1、进程的介绍
    # 是操作系统进行资源分配和调度的基本单位，是操作系统结构的基础
    # 进程的状态：
    #     1、就绪状态：运行的条件都已经满足，正在等待cpu执行
    #     2、执行状态：cpu正在执行其功能
    #     3、等待(阻塞)状态：等到某些条件满足，如一个程序sleep了，此时就处于等待状态
# 2、进程的语法结构
    # multiprocessing模块提供了Process类代表进程对象
    # Process类参数
        # target：执行的目标任务名
        # args：以元组的形式传参
        # kwargs：以字典的形式传参
    # 常用的方法：
        # start()、is_alive()()、join()
        # is_alive()：写在主进程中判断存活状态的时候需要加入join阻塞下，子进程就是False
    # 常用的属性：name：当前进程的别名，默认Process-N
            #   pid：当前进程的进程编号
from multiprocessing import Process
import os

def sing():
    print('zzz',os.getpid())    # 获取当前进程的编号
    print('xxxx',os.getppid()) # 获取主进程的方法
    print("sing some song")
def dance():
    print('mmm',os.getpid())
    print('yyy',os.getppid())
    print("dance with you")
if __name__ == '__main__': # 写这个目的：防止别人导入文件的时候执行main方法；防止windows系统递归创建子进程
    pa1 = Process(target=sing,name='进程1') # 修改进程名字的一种方式
    pa2 = Process(target=dance,name='进程2')
    pa1.start()
    pa2.start()
    pa1.name = 'ttt' # 修改进程名字的另一种方式
    pa2.name = 'rrr'
    print(pa1.name)
    print(pa2.name)
    print("在外部获取主进程的编号:",os.getpid(),"主进程的父进程:",os.getppid())
                                            # 运行py程序的软件进程
# 3、进程间的通信（# 进程间不公享全局变量）
    #  Queue(队列)
        # q.put(): 放入数据
        # q.get(): 取出数据，然后将其从队列删除
        # q.empty(): 判断队列是否为空
        # q.qsize(): 返回当前队列包含的消息数量
        # q.full(): 判断队列是否满了
from multiprocessing import Process,Queue,set_start_method
import time
li = ['zz','xx','cc','vv']
def writeData(q1):
    for i in range(5):
        # li.append(i)
        print("放入了：",i)
        q1.put(i)
        time.sleep(0.5)
    print('wirte:',li)
def readData(q2):
    while True:
        if q2.empty():
            break
        else:
            print("取出了，",q2.get())
    print('li',li)
if __name__ == '__main__':
    set_start_method('fork')  # 关键设置 （）macos需要加这个，不然会报错。因为Macos的spawn模式会重新导入模块，导致全局状态不一致系统临时文件描述符在子进程中无效
    q = Queue()
    a1 = Process(target=writeData,args=(q,))        
    a2 = Process(target=readData,args=(q,))        
    a1.start()
    a1.join()
    a2.start()

# 4、进程池

# 四十二、线程1

# 线程是Python中实现并发编程的一种方式，可以同时执行多个任务。
# 1、线程基础：
    # 线程是操作系统能够进行运算调度的最小单位，它被包含在进程之中，是进程中的实际运作单位。一个进程可以包含多个线程。
# 2、线程实现
#   Python 通过 threading 模块提供了线程操作接口。需要注意的是，由于 GIL（全局解释器锁）的存在，
#   Python 的多线程在 CPU 密集型任务上并不能真正并行，但在 I/O 密集型任务中仍然很有用。    
# 3、创建线程
    # 1、使用 threading.Thread 类
import threading

def worker(num):
    print(f'Worker: {num}')

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

    # 2、继承 Thread 类
class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    
    def run(self):
        print(f'Worker: {self.num}')

threads = []
for i in range(5):
    t = MyThread(i)
    threads.append(t)
    t.start()
# 4、线程的特点
    # 1、线程之间是无序的
        # 1、操作系统的线程调度机制 2‘Python的GIL(全局解释器锁) 3、硬件层面（多核cpu）
    # 2、线程之间共享资源
import threading,time
li = []
def wlist():
    for i in range(5):
        li.append(i)
        time.sleep(0.1)
    print('write:',li)    
def rlist():
    print('read:',li)
if __name__ == '__main__':
    # 创建子线程
    t1 = threading.Thread(target=wlist,args=())
    t2 = threading.Thread(target=rlist,args=())
    t1.start()
    t1.join() # 等t1线程结束再执行
    # time.sleep(0.5) 这种方法的时间，要和线程的时间保持一致，一般不建议使用
    t2.start()
    # 3、资源竞争(这个还是看电脑的cpu的，我用百万，没测出来)
a = 0;b = 10000000
def add1():
    for i in range(b):
        global a 
        a+=1
    print('first:',a)
def add2():
    for i in range(b):
        global a 
        a+=1
    print('second:',a)
if __name__ == '__main__':
    t1 = threading.Thread(target=add1,args={})    
    t2= threading.Thread(target=add2,args={})    
t1.start()
t2.start()

# 5、线程的同步
    # 两种方式：join和互斥锁
        # 互斥锁：对共享的数据进行锁定，保证多个线程访问共享数据不会出现数据错误问题；保证同一时刻只能有一个线程去操作
                # acquire()上锁   release()：释放锁。必须成对出现，不然会出现死锁
                # 也是多个锁互相抢，抢到先执行
from threading import Lock,Thread
import time
lock = Lock();
li = []
def wlist():
    lock.acquire()
    for i in range(5):
        li.append(i)
        time.sleep(0.1)
    print('write:',li)   
    lock.release() 
def rlist():
    lock.acquire()
    print('read:',li)
    lock.release() 
if __name__ == '__main__':
    # 创建子线程
    t1 = Thread(target=wlist)
    t2 = Thread(target=rlist)
    t1.start()
    t2.start()


# 四十三：线程2(后续补上)

# 1、多任务
    # 多个任务执行
# 2、多线程 
    # 线程
        # 守护线程 setDaemon(True),必须放在start前面。作用：主进程执行结束，子线程也会跟着结束
        # 获取线程名字：getName()

# 3、线程同步

# 4、互斥锁

# 四十四、协程

# 1、又称微线程，纤程。Coroutime。是Python中另外一种实现多任务的方式，只不过比线程更小，占用更小执行单元（需要的资源）
# ，自带cpu上下文。这样只要在合适的时机，我们可以把一个协程切换到另一个协程。只要这个过程中保持或恢复cpu上下文那么程序还是可以运行的

# 2、简单实现
import time
def task1():
    while True:
        yield 'hahaha'
        time.sleep(1)
def task2():
    while True:
        yield 'heiheihei'
        time.sleep(1)
if __name__ == '__main__':
    t1 = task1()
    t2 = task2()
    while True:
        print(next(t1))
        print(next(t2))
#  3、应用场景
    # 1、如果一个线程里面IO操作比较多的时候，可以用协程
        # Input/Output
        # 常见的IO操作：文件操作，网络请求
    # 2、适合高并发处理

# 4、greenlet
    # 为了更好使用协程来完成多任务，python中的greenlet模块对其封装，从而使得切换任务变得更加简单
    # 属于手动切换，当遇到IO操作，程序会阻塞，而不能进行自动切换
from greenlet import greenlet
def test01():
    print('11111')
    g2.switch() # 运行到这里去执行g2了
    print('22222')
def test02():
    print('3333')
    print('4444')
    g1.switch() # 继续把2222输出
if __name__ == '__main__':
    g1 = greenlet(test01)
    g2 = greenlet(test02)
    g1.switch() # 切换到g1中去运行
    g2.switch()

import gevent
import time
# 5、gevent
    # 比greenlet强大，能够自动切换
    # 使用：
    # gevent.spwan(函数名) ：创建协程对象
    # gevent.sleep()：耗时操作
    # gevent.join()：阻塞，等待某个协程执行结束
    # gevent.joinall()：等待所有协程对象都执行结束再退出，参数是一个协程对象列表
def test01():
    print('11111')
    gevent.sleep(2) # gevent会让sleep数值小的先运行
    print('22222')
def test02():
    print('3333')
    gevent.sleep(3) 
    print('4444')
if __name__ == '__main__':
    g1 = gevent.spawn(test01)
    g2 = gevent.spawn(test02)
    g1.join() # 这里至少要写一个，不然输出空
    g2.join()
  # joinall()
def code(name):
    for i in range(3):
        gevent.sleep(1)
        print(f'{name}push code in night{i}次')
if __name__ == '__main__':
    gevent.joinall( # joinall()等待所有的协程都执行结束再退出
        [gevent.spawn(code,'zxw'),
        gevent.spawn(code,'mm')]
    )
# monkey补丁：拥有在模块运行时替换的功能
import gevent
import time
from gevent import monkey
monkey.patch_all() # 将用到的time.sleep()代码替换成gevent里面自己实现耗时操作的gevent.sleep()代码
# 必须放在被打补丁的前面
def code(name):
    for i in range(3):
        time.sleep(1)
        print(f'{name}push code in night{i}次')
if __name__ == '__main__':
    gevent.joinall( # joinall()等待所有的协程都执行结束再退出
        [gevent.spawn(code,'zxw'),
        gevent.spawn(code,'mm')]
    )

# 总结：
#     线程是CPU调度的基本单位，进程是资源分配的基本单位
#     进程、线程、协程对比：
#         进程：切换需要的资源大，效率低
#         线程：切换需要的资源一般，效率一般
#         协程：切换需要的资源小，效率高
#     多线程适合IO密集型操作（文件操作，爬虫），多进程适合CPU密集型操作（科学计算，对视频进行高清解码，计算圆周率）
#     这些都是可以完成多任务的