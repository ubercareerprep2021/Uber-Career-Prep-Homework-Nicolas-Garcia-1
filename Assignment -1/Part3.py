# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:00:14 2021

@author: nicol
"""

#don't know how to implement it into class or how to use __int__   
list1 = [1, 2, 3]

def Push(integer: int):
    list1.insert(0, integer)
    
def Pop():
    list1.pop(0)
    
def Top():
    return list1[0]

def isEmpty():
    return len(list1) == 0
        
def Size():
    return len(list1)
    
print(Size())
