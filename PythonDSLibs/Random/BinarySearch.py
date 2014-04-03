'''
Created on Mar 31, 2014

@author: psgada
'''
def binary_search(arr, low, high, data):

    mid = (low + high) / 2

    if low > high:
        return False

    if arr[mid] == data:
        return True

    if arr[mid] > data:
        return binary_search(arr, low, mid-1, data)

    if arr[mid] < data:
        return binary_search(arr, mid+1, high, data)


print binary_search([1,2,3,4],0,3,2)
print binary_search([1,2,3,4],0,3,5)
print binary_search([1,2,3,4,5],0,4,2)
print binary_search([1,2,3,4,5],0,4,7)
print binary_search([1],0,0,1)
print binary_search([1],0,0,2)
print binary_search([],0,-1,2)