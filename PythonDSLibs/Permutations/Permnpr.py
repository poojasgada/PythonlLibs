'''
Created on Mar 27, 2014

@author: psgada

calculate npr permutations
'''

import sys

perm_set = set()

def gen_permutations(strn_list, indx, r):

    if indx == r + 1:
        perm_set.add(''.join(strn_list[0:r]))
        return

    for i in range(indx, len(strn_list)):
        strn_list[i], strn_list[indx] = strn_list[indx], strn_list[i]
        gen_permutations(strn_list, indx+1, r)
        strn_list[indx], strn_list[i] = strn_list[i], strn_list[indx]


def get_input():

    strn = sys.stdin.readline().strip()

    strn_list = list(strn)

    r = 3

    gen_permutations(strn_list, 0, r)

    print len(perm_set)
    print perm_set

get_input()