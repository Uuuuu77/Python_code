x = input("Number: ")
y = input("Number: ")
sum = x + y
print(sum)
###############################
""" Python threads """
import threading
import time 
import random

class cust_threading(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name
    
    def run(self):
        get_time(self.name)
        print("Threads", self.name, "Execution ends")
    
def get_time(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)

thread1 = cust_threading("1")
thread2 = cust_threading("2")

thread1.start()
thread2.start()

print("Thread 1 alive", thread1.is_alive())
print("Thread 2 alive", thread2.is_alive())

print("Thread 1 name : ", thread1.getName)
print("Thread 2 name : ", thread2.getName)

thread1.join()
thread2.join()

print("Execution ends")