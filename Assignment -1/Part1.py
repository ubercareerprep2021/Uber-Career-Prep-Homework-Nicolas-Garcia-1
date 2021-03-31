# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:16:12 2021

@author: nicol
"""

#go thru first string
#check against second string for each letter
#remove letter once found

#test cases: 
    
#1   s1: asdf, s2: fsda == true
#2   s1: asdf, s2: fsa == false
#3   s1: asdf, s2: fsax == false

def isStringPermutation (s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if i not in s2:
            return False
        
    return True    
        
        
print(isStringPermutation('asdf', 'fsda'))
print(isStringPermutation('asdf', 'fsa'))
print(isStringPermutation('asdf', 'fsax'))
print(isStringPermutation('asda', 'dasa'))            
    
