#O(n) linear time in size of list

import random
from random import *

class rand:
    gen = Random()

def random_number_insertion(length):
    lis = [0] * length
    for i in range(length):
        lis[i] = rand.gen.randint(1,6)
    return lis

