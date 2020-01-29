#O(1) constant time

import random
from random import *

class rand:
    gen = Random()

def switch(lis):
    index = rand.gen.randint(0,len(lis)-2)
    temp = lis[index]
    lis[index] = lis[index+1]
    lis[index + 1] = temp

def switch_random(lis):
    index1 = rand.gen.randint(0,len(lis)-1)
    index2 = rand.gen.randint(0,len(lis)-1)
    temp = lis[index1]
    lis[index1] = lis[index2]
    lis[index2] = temp