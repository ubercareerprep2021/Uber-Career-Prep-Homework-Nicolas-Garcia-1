# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:00:14 2021

@author: nicol
"""


class Stack:
    
    def __init__(self):
        self.List = []
        
    def Push(self, integer: int):
        self.integer = integer
        self.List.insert(0, integer)
    
    def Pop(self):
        self.List.pop(0)
    
    def Top(self):
        return self.List[0]

    def isEmpty(self):
        return len(self.List) == 0
        
    def Size(self):
        return len(self.List)
    
s = Stack()

s.Push(1)
s.Push(2)
s.Push(5)
print(s.List) #[5, 2, 1]
s.Pop()
print(s.List) #[2, 1]
print(s.Top()) #2
print(s.isEmpty()) #False
print(s.Size()) #2
print()

class Queue:
    
    def __init__(self):
        self.List = []
        
    def Enqueue(self, item):
        self.item = item
        self.List.append(item)
    
    def Dequeue(self):
        self.List.remove(self.List[0])
    
    def Rear(self):
        return self.List[-1]
    
    def Front(self):
        return self.List[0]
    
    def Size(self):
        return len(self.List)
    
    def isEmpty(self):
        return len(self.List) == 0
    
q = Queue()
q.Enqueue('item 1')
q.Enqueue('item 2')
q.Enqueue('item 3')
q.Enqueue(4)
print(q.List) #["item 1", "item 2", "item 3", 4]
q.Dequeue()
print(q.List)#["item 2", "item 3", 4]
print(q.Rear()) #4
print(q.Front()) #"item 2"
print(q.Size()) #3
print(q.isEmpty()) #False