#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:18:15 2018
EE 381 Fall 2018 Project 1
@author: Tony Le

Brief programs for determining summary statistics of inputted data written below
"""

L = [] #Empty list for data
v = 1  # initalized boolean var

print("You'll be prompted to enter nonnegative integers. \n")
print('When you want to stop enter ten word stop.')

while v == 1:
        try:
            l = int(input('Enter a nonnegative integer. '))
            L.append(l)
        except ValueError:
            print('Input terminated. ')
            print('\n')
            v = 0;
            
print('You inputted the numbers listed: ')
print(L)

#---------------------------------------------
#Below is calculation of mean

s = sum(L) #Sum of list L
N = len(L) #Number of elements in L
mean = s/N #Arithemetic Average of L

print('The mean of the numbers is ,',mean,'.')
print('\n')

#---------------------------------------------
#Below is the calculation of the median
#The numbers need to be sorted
L.sort()
#Relevant if the numbers of elements is odd or even
if N%2 == 0: #Number of elements is even
    m1 = (N/2) 
    m2 = (N/2) + 1 #The two middle positions
    
    m1 = int(m1)
    m2 = int(m2) #Cast to int
    
    m1 = m1 - 1
    m2 = m2 - 1 #Correct one off error
    
    median = (L[m1] + L[m2])/2
    
else: #odd case
    m = (N + 1)/2
    m = int(m) - 1
    median = (L[m])
    
print('The median of the numbers is ' ,median, '.')
print('\n')
#---------------------------------------------1
#Below is the program to find mode
from collections import Counter
c= Counter(L) #creates tuples list (element, frequency)
freq = c.most_common() #most common method
max_occur = freq[0][1] #The largest frequency assigned to max_occur
if max_occur !=1:
    modes = []
    for m in freq:
        if m[1] == max_occur: #looking for all frequencies the same as max_occur
            modes.append(m[0])
    print('The mode(s) are ', modes,'.')
else:
    print('There is no mode.')
print('\n'
      )
#---------------------------------------------
#Below is the calculations of the range

highest = max(L)
lowest = min(L)
Range = highest - lowest
print('The range is ',Range,'.')
print('\n')
#---------------------------------------------
#Below is the calculation of variance
S = 0 #initial value of accumulator
for n in L:
    x = (n - mean)**2
    S = S + x
variance = S/N
print('The variance is ', variance,'.')
print('\n')
#---------------------------------------------
#Below is the calculation of the standard deviation
import math #required for sqrt
standard_deviation = math.sqrt(variance) #Calculates standard deviation
print('The standard deviation is ', standard_deviation, '.')