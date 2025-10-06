#Program to find power set of a set

import math;

def printpowerset(set,SetSize):
    #Find total elements possible in power set
    powersetsize = (int)(math.pow(2,SetSize))
    outer = 0,
    inner = 0,

    for outer in range(0,powersetsize):
        for inner in range(0,SetSize):
            #Check if inner bit in outer is set if set then print inner element from set
            
            if ((outer & (1 << inner)) > 0):
                print(set[inner],end=" ")
            print()

size = 