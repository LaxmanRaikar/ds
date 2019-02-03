from utilities.utility import Queue
a=Queue()
for i in range(10):
    a1=a.enqueue(i)
    a.dequeue()
a.show()

