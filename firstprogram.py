# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:58:45 2020

@author: givaratk
"""

print("Hello World!!")

N = input("How many times do you want to print ? \n")
N = int(N)
for index in range(1,N+1):
    print("Happy Birthday Saina !!!")
    
N = input("I can find sum of numbers upto N. Please type N and press Enter")
N = int(N)
Sum = 0
for index in range(1,N+1):
    Sum = Sum + index
print("Sum =", Sum)


