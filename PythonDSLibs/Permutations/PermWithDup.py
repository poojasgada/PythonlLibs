'''
Created on Mar 27, 2014

@author: psgada

The code below generates permutations of a string, which contains duplicates
'''

import sys

def gen_permutations(strn_list, indx):

    if indx == len(strn_list):
        print ''.join(strn_list)
        return

    for i in range(indx, len(strn_list)):
        strn_list[i], strn_list[indx] = strn_list[indx], strn_list[i]
        gen_permutations(strn_list, indx+1)
        strn_list[indx], strn_list[i] = strn_list[i], strn_list[indx]


def get_input():

    strn = sys.stdin.readline().strip()

    strn_list = list(strn)

    gen_permutations(strn_list, 0)

get_input()