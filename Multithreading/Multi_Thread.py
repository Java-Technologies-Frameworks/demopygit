from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

# 2 threads t1,t2 . internally start method will call to run ()

t1.start()
sleep(0.2)
t2.start()

# we are asking Main tharead to wait t1 and t2 '
t1.join()
t2.join()
print("Bye")
# execution starts from Main Thread
# 2 threads coming to CPU at the same time, so collision happens
