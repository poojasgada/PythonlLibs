'''
Created on Mar 27, 2014

@author: psgada

This code generates permutations without repetitions. Just keep adding the permutations to the set.

Not sure if this is a right approach. Need a way to optimize it.
'''

import sys

perm_set = set()

def gen_permutations(strn_list, indx):

    if indx == len(strn_list):
        perm_set.add(''.join(strn_list))
        return

    for i in range(indx, len(strn_list)):
        strn_list[i], strn_list[indx] = strn_list[indx], strn_list[i]
        gen_permutations(strn_list, indx+1)
        strn_list[indx], strn_list[i] = strn_list[i], strn_list[indx]


def get_input():

    strn = sys.stdin.readline().strip()

    strn_list = list(strn)

    gen_permutations(strn_list, 0)

    print perm_set

get_input()