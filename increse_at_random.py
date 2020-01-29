#O(1) constant time

import random
from random import *

class rand:
    gen = Random()

def increase_a_random(lis):
    index = rand.gen.randint(0,len(lis)-1)
    lis[index] += 1