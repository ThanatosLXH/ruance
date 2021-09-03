#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 22:43
# @Author  : LXH
# @File    : duojincheng.py

# import os,time
# from multiprocessing import Pool
#
# def worker(arg):
#     print("子进程开始执行>>> pid={},ppid={},编号{}".format(os.getpid(),os.getppid(),arg))
#     time.sleep(0.5)
#     print("子进程终止>>> pid={},ppid={},编号{}".format(os.getpid(),os.getppid(),arg))
#
# def main():
#     print("主进程开始执行>>> pid={}".format(os.getpid()))
#     ps=Pool(5)
#     for i in range(10):
#         # ps.apply(worker,args=(i,))          # 同步执行
#         ps.apply_async(worker,args=(i,))  # 异步执行
#
#     # 关闭进程池，停止接受其它进程
#     ps.close()
#     # 阻塞进程
#     ps.join()
#     print("主进程终止")
#
# if __name__ == '__main__':
#     main()


# import os,time
# from multiprocessing import Process
#
# def worker():
#     print("子进程执行中>>> pid={0},ppid={1}".format(os.getpid(),os.getppid()))
#     time.sleep(2)
#     print("子进程终止>>> pid={0}".format(os.getpid()))
#
# def main():
#     print("主进程执行中>>> pid={0}".format(os.getpid()))
#
#     ps=[]
#     # 创建子进程实例
#     for i in range(3):
#         p=Process(target=worker,name="worker"+str(i),args=())
#         ps.append(p)
#
#     # 开启进程
#     for i in range(3):
#         ps[i].start()
#
#     # 阻塞进程
#     for i in range(3):
#         ps[i].join()
#
#     print("主进程终止")
#
# if __name__ == '__main__':
#     main()

#
# import threading
# import time
#
#
# def main(name):
#     print('线程%s 开始' % name)
#     time.sleep(5)
#     print('线程%s 结束' % name)
#
#
# if __name__ == '__main__':
#     threads = []
#     # thread_name = ['1', '2', '3']
#     for name in range(2):
#         t = threading.Thread(target=main, args=(name,))
#         t.start()
#         threads.append(t)
#     for thread in threads:
#         thread.join()

import time

def time_it(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('用时:{}秒'.format(end-start))
    return inner

@time_it
def func1():
    time.sleep(2)
    print("Func1 is running.")

# if __name__ == '__main__':
func1()