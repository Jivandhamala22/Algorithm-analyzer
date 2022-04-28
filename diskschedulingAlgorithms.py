import time
from tkinter import messagebox
import turtle
import pandas as pd
import numpy as np
from copy import copy

def FCFS(input_data, rwhead):
    
    #initialize to 0
    Sum = 0     
     #set current position = start                
    position = rwhead    
    #creates empty list of name Order       
    Order = []  
     #adds rwhead to end of list Order                
    Order.append(rwhead)   
     #i is the current element in the list(first loop i = 95)     
    for i in input_data:          
        Sum += abs(i-position)      #sum = sum + (distance of current position from next position)
        #set position new position (i)
        position = i            
         #Add i to the end of the list Order
        Order.append(i)        
    return Order, Sum

def SSTF(input_data, rwhead):

    templist = copy(input_data)
    position = rwhead
    highest = max(templist)
    mindiff=abs(rwhead-highest)
    j=highest
    templist.sort()
    Order = []
    Order.append(rwhead)
    Sum = 0
    while len(templist) > 0:
        for i in templist:
                diff= abs(position-i)
                if diff<mindiff:
                    mindiff=diff
                    j=i
        Sum+= abs(position-j)
        position = j
        templist.remove(j)
        Order.append(j)
        mindiff=abs(position-highest)
        j=highest
    return Order, Sum

def SCAN(input_data, rwhead):
    n = len(input_data)
    Order = []
    input_data_tmp=copy(input_data)
    input_data_tmp.sort()
    if rwhead != 0 and rwhead < input_data_tmp[n-1]:
        input_data_tmp.append (0)
    p = len(input_data_tmp)

    i = rwhead - 1
    Order.append(rwhead)
    while i >= 0:
        for j in range(0,p):
            if(input_data_tmp[j] == i):
                Order.append(i)
        i -= 1



    k = rwhead + 1
    while k < 200:
        for l in range(0,n):
            if(input_data[l] == k):
                Order.append(k)
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum

def LOOK(input_data, rwhead):
     # Number of input_datas
    n = len(input_data)                       
    Order = []
    i = rwhead - 1
    Order.append(rwhead)
     # Diskhead moving outward from start position
    while i > 0:                           
        for j in range(0,n): 
             # input_data found                   
            if(input_data[j] == i):  
                 # input_data executed         
                Order.append(i)            
        i -= 1

    k = rwhead + 1
    # Diskhead moving inward from  previous position
    while k < 200:                          
        for l in range(0,n):  
             # input_data found                 
            if(input_data[l] == k):   
                 # input_data executed        
                Order.append(k)            
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        # Calculates total head movement
        Sum += abs(Order[p] - Order[p+1])   
    return Order, Sum


def CSCAN(input_data, rwhead):
    n = len(input_data)
    Order = []
    input_data_tmp=copy(input_data)
    input_data_tmp.sort()
    if rwhead != 0 and rwhead < input_data_tmp[n-1]:
        input_data_tmp.append (0)
    p = len(input_data_tmp)

    i = rwhead - 1
    Order.append(rwhead)
    while i >= 0:
        for j in range(0,p):
            if(input_data_tmp[j] == i):
                Order.append(i)
        i -= 1

    k = 199
    while k > rwhead:
        if(k == 199):
            Order.append(k)
        for l in range(0,n):
            if(input_data[l] == k):
                Order.append(k)
        k -= 1

    Sum = 0
    SortedReq = copy(Order)
    SortedReq.sort()
    for p in range(0,len(Order) - 1):
        if (Order[p] != SortedReq[0]):
            Sum += abs(Order[p] - Order[p+1])
    return Order, Sum

def CLOOK(input_data, rwhead):
     # Number of requests
    n = len(input_data)                           
    Order = []
    i = rwhead - 1
    Order.append(rwhead)
      # Diskhead moving outward from start position
    while i > 0:                              
        for j in range(0,n):    
             # input_data found                    
            if(input_data[j] == i):  
                  # input_data executed             
                Order.append(i)               
        i -= 1

    k = 199
    # Diskhead moving inward from  highest request position
    while k > rwhead:                            
        for l in range(0,n):  
              # input_data found                    
            if(input_data[l] == k):  
                  # input_data executed            
                Order.append(k)               
        k -= 1

    Sum = 0
       # Creates copy of job order
    SortedReq = copy(Order)     
    # Sorts job order from lowest to highest             
    SortedReq.sort()                            
    for p in range(0,len(Order) - 1):   
        # Excludes the circular movement         
        if (Order[p] != SortedReq[0]):  
             # Calculates total head movement       
            Sum += abs(Order[p] - Order[p+1])  
    return Order, Sum
