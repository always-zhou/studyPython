# 四十一、线程

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