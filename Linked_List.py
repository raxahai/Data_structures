class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None

    def add_node_at_beginning(self,data):
        n = node(data)
        if self.head == None:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def add_node_at_last(self,data):
        n = node(data)
        head = self.head
        if self.head == None:
            self.head = n
        else:
            while head.next != None:
                head = head.next
            head.next = n

    def add_node_at_middle(self,data):
        n = node(data)
        head = self.head
        n.next = head.next
        head.next = n

    def show(self):
        head = self.head
        while head != None:
            print(head.data)
            head = head.next
