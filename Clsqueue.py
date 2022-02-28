
class queue:
    def __init__(self):
        self.qlst = []

    def isEmpty(self):
        if len(self.qlst) == 0:
            return True
        else:
            return False
        
    def enqueue(self, data):
        
        self.qlst.append(data)
        
    def dequeue (self):
        if self.isEmpty():
            pass
        else:
            tmpData = self.qlst[0]
            self.qlst = self.qlst[1:]
            return tmpData
        
    def front(self):
        
        if self.isEmpty():
            pass
        else:
            return self.qlst[0]
        
    def back(self):
        if self.isEmpty():
            pass
        else:
            return self.qlst[-1]
    


# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False

    def enqueue(self, data):
        new_node = Node(data)

        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            dequeued = self.front
            self.front = self.front.next

        # front가 None이 되면 큐가 비었다는 뜻이므로 rear도 None
        if self.front is None:
            self.rear = None
        return dequeued

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.front.data