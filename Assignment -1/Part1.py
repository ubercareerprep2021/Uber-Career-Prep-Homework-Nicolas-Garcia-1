# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:16:12 2021

@author: nicol
"""

#method 1

#test cases: 
    
#1   s1: asdf, s2: fsda == true
#2   s1: asdf, s2: fsa == false
#3   s1: asdf, s2: fsax == false
#4   s1: asda, s2: dasa == true
#5   s1: aaaa, s2: sadx == false
#6   s1: sadx, s2: aaaa == false

def isStringPermutation (s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    
    for i in s1:
        for j in s2:
            if i not in s2 or j not in s1:
                return False
        
    return True    
        

#method 2

#test cases: 
    
#1   s1: asdf, s2: fsda == true
#2   s1: asdf, s2: fsa == false
#3   s1: asdf, s2: fsax == false
#4   s1: asda, s2: dasa == true
#5   s1: aaaa, s2: sadx == false
#6   s1: sadx, s2: aaaa == false

def isStringPermutation2 (s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    
    for i in s1:
        s1_counter = s1.count(i)
        s2_counter = s2.count(i)
        if s1_counter != s2_counter:
            return False
    return True