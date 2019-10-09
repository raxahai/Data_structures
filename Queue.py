size = int(input("what size array do u need?"))
front = 0
tail = 0
array = [None] * size

def Enqueue(element):
    global tail
    if tail > size - 1:
        print("Queue Overflow")
    else:
        array[tail] = element
        tail += 1

def Dequeue():
    global front
    if front == 0:
        print("Queue Underflow")
    else:
        del array[front]
        front += 1