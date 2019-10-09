size = int(input("what size array do u need?"))
top = 0
array = [None] * size

def push(element):
    global top
    if top > size - 1:
        print("Stack Overflow")
    else:
        array[top] = element
        top += 1

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        top -= 1
        del array[top]