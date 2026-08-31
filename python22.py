#BUILT IN MODULES IN PYTHON
print("""
MODULES IN PYTHON : consider a module to be the same as a code library

a file containing a set of functions you want to include in your application

EXAMPLES OF PYTHON MODULES:
1. math
2.random
3.os
4.time

python modules provide reusability """)

print(help('modules'))

print("\n we are gonna learn only 4 modules in this file\n")

#MATH MODULE 

import math
print(math.factorial(5))
print(math.pi)
print(math.e)
print(math.ceil(3.2))
#4
print(math.ceil(3.0))
print(math.floor(2.3))
#2
print(math.floor(2.9))

#RANDOM MODULE
import random

random.randint(1,100)

print(random.randint(1,100))
a=(1,2,3,4,5)
#random.shuffle((a))
print(a)

#TIME MODULE
import time
print(time.time())
#number of seconds passed since 1st of january

print(time.ctime())
print("HELLO")
time.sleep(2)
#after 2 seconds next code execute
print("prime")

#OS MODULE

import os
a=os.getcwd()
#current working directory
print(a)

b=os.listdir()
#list all files in the directory including the current
print(b)