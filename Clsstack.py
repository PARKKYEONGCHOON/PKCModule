
class stack:
    def __init__(self):
        self.stlst = []

    def isEmpty(self):
        if len(self.stlst) == 0:
            return True
        else:
            return False
        
    def push(self, data):
        
        self.stlst.append(data)
        
    def pop(self):
        if self.isEmpty():
            pass
        else:
            self.stlst.pop()
            
    def top(self):
        if self.isEmpty():
            pass
        else:
            return self.stlst[-1]
    
# Singly Linked Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def push(self, data):
        new_node = Node(data)
        # push된 데이터는 head를 가리킨다.
        new_node.next = self.head
        # head는 top 데이터가 된다.
        self.head = new_node

    def top(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.head.data    