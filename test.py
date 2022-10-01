import time
import datetime
import threading

from kill_thread import kill_thread


def print_time():
    while True:
        time.sleep(1)
        print(datetime.datetime.now())

# 生成启动一个每隔一秒打印当前时间的线程
thread = threading.Thread(target=print_time)
thread.start()

# 十秒后杀死线程
time.sleep(10)
kill_thread(thread)

# 阻塞主线程观察打印时间的线程是否被杀死
input('按任意键终止主线程')