'''
Created on Apr 9, 2014

@author: psgada

This is a simple implementation of trie

With all the necessary functions one would implement with a Trie

If you always wondered how autocompletion work, trie will rescue you ! 

In python, you can implement Tries using simple dictionaries

Key - Character of the string
Value - Dictionary which contains all the key value pairs of the Children trie nodes

Implementing Trie cannot get easier than this!

Functions Included in this library

1. Inserting a string into the Trie
2. Searching for a string in the Trie
3. Given a prefix, find all the matches - Basically autocomplete!
'''

import sys

class Trie:
    def __init__(self):
        self.root = {}
        self.auto_match = []
        
    def insert(self, str):
        if str == None:
            return
        
        #Lets start inserting from the root
        cur_trie_node = self.root
        
        for str_char in str:
            if cur_trie_node.has_key(str_char):
                cur_trie_node = cur_trie_node[str_char]
            else:
                cur_trie_node[str_char] = {}
                cur_trie_node = cur_trie_node[str_char]
        
        cur_trie_node['\0'] = {}
        
        
    def search(self, str):
        if str == None:
            return False
        
        cur_trie_node = self.root
        
        for str_char in str:
            if cur_trie_node.has_key(str_char):
                cur_trie_node = cur_trie_node[str_char]
            
            else:
                return False
            
        if cur_trie_node.has_key('\0'):
            return True
        else:
            return False
        
    # Some autocomplete action   
    def autocomplete_matches(self, str):
        self.auto_match = []
        
        if str == None:
            self.auto_match = []
        
        cur_trie_node = self.root
        
        for str_char in str:
            if cur_trie_node.has_key(str_char):
                cur_trie_node = cur_trie_node[str_char]
            else:
                self.auto_match.append("No Matches")
        
        #Only the given string matched
        if cur_trie_node.has_key('\0'):
            self.auto_match.append(str)

        else:
            self.get_matches(cur_trie_node, str)
        
        
    #Recursively drill down to find all our matches    
    def get_matches(self, cur_trie_node, str):
        
        if cur_trie_node.has_key('\0'):
            self.auto_match.append(str)
        
        else:
            
            cur_str = str
            
            for key_val in cur_trie_node.keys():
                self.get_matches(cur_trie_node[key_val], cur_str+key_val)


# This is a test module to test all the above trie functions
# Ideally, one should use unittest
def main():
    
    t = Trie()
    
    t.insert("hell")
    t.insert("help")
    t.insert("head")
    print t.root
    
    print t.search("help")
    print t.search("held")
   
    t.autocomplete_matches("he")
    print t.auto_match
    
    t.insert("doom")
    t.insert("dark")
    print t.root
    
    t.autocomplete_matches("d")
    print t.auto_match
    
    t.autocomplete_matches("doo")
    print t.auto_match
    
main()