# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:18:11 2021

@author: nicol
"""

#test cases: 
    
#1    inputArray: [1, 2, 3, 4, 5], targetSum: 5 == [(1, 4), (2, 3)]
#2    inputArray: [1, 2, 3, 4, 5], targetSum: 1 == []
#3    inputArray: [1, 2, 3, 4, 5], targetSum: 7 == [(2, 5), (3, 4)]


def pairsThatEqualSum(inputArray: list, targetSum: int):
    newList = []
    inputArray.sort() 
    
    if targetSum % 2 != 0:
        for duplicate in inputArray:
            count = inputArray.count(duplicate)
            if count % 2 == 0:
                inputArray.remove(duplicate)  #rid of duplicates in odd targetSum
    
    for i in range(len(inputArray)):
        
        for j in range(i, len(inputArray)):
            
            if inputArray[i] + inputArray[j] == targetSum and i != j:
                newTuple = (inputArray[i], inputArray[j])
                newList.append(newTuple)
    
    return newList
            
    
    
print(pairsThatEqualSum([1, 2, 3, 4, 5], 5))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 1))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 7))

        