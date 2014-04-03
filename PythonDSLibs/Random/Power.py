'''
Created on Mar 31, 2014

@author: psgada
'''
def power_func(a, b):

    if b == 0:
        return 1
    if b == 1:
        return a

    resultby2 = power_func(a, b/2)

    if b % 2 == 0:
        return resultby2 * resultby2

    return a * resultby2 * resultby2

print power_func(2,0)
print power_func(2,1)
print power_func(2,2)
print power_func(2,4)
print power_func(2,5)
