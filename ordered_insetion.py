import random
from random import *

class rand:
    gen = Random()

def switch(lis,index):
    temp = lis[index]
    lis[index] = lis[index + 1]
    lis[index + 1] = temp

def ordered_insertion(lis,value):
    index = len(lis) -1 
    lis.append(value)
    while index >= 0 and lis[index] > value:
        switch(lis,index)
        index -= 1
#O(n) linear time in size of list
