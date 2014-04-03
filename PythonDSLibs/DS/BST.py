'''
Created on Mar 29, 2014

@author: psgada
'''
import sys
import Queue

'''
Write unittest module to test the individual modules of the Binary search tree class
'''

'''
Define a binary tree node class
A node of a binary search tree contains a left pointer which points to left subtree,
a right pointer which points to right subtree and
a data value which can be associated to the node

'''

class Node:
    def __init__(self, node_val):
        self.right = None
        self.left = None
        self.data = node_val


'''
 Define a binary search tree class
 To start with the binary tree does not have nodes
 Binary search tree has the following methods
 1. Insert node into binary search tree
 2. Search for node in a binary search tree
 3. Print elements of the binary search tree in preorder, postorder, inorder
 4. Print elements of the binary search tree level by level
 5. Size of the binary search tree
 6. Max Depth of the binary search tree
 7. Min Depth of the binary search tree
 8. Minimum value of the binary search tree
 9. Maximum value of the binary search tree
 10. Has path sum of given value
 11. Print all the paths of a binary search tree
 12. Mirror of a BST
 13. Is BST or not - Using min and max values
'''

class Tree:
    def __init__(self):
        self.root = None


#Use this method to insert elements into the binary search tree
    def insert(self, cur_node, new_val):
        if self.root == None:
            self.root = Node(new_val)

        else:
            if new_val < cur_node.data:
                if cur_node.left is None:
                    cur_node.left = Node(new_val)
                else:
                    self.insert(cur_node.left, new_val)

            else:
                if cur_node.right is None:
                    cur_node.right = Node(new_val)
                else:
                    self.insert(cur_node.right, new_val)

        return


#Use this method to print the elements of the binary search tree in inorder
    def print_inorder(self, cur_node):

        if cur_node is not None:
            self.print_preorder(cur_node.left)
            print cur_node.data
            self.print_preorder(cur_node.right)


#Use this method to print the elements of the binary search tree in preorder
    def print_preorder(self, cur_node):
        if cur_node is not None:
            print cur_node.data
            self.print_preorder(cur_node.left)
            self.print_preorder(cur_node.right)


#Use this method to print the elements of the binary search tree in postorder
    def print_postorder(self, cur_node):
        if cur_node is not None:
            self.print_preorder(cur_node.left)
            self.print_preorder(cur_node.right)
            print cur_node.data


# Use this method to print a tree level by level
# Need to find a better way to terminate
    def print_bst_by_level(self):
        bst_q = Queue.Queue()
        level_list = []

        if self.root is None:
            print "Tree is empty"
            return

        bst_q.put(self.root)
        bst_q.put('*')

        while not bst_q.empty():
            cur_node = bst_q.get()

            if cur_node is None:
                break

            # When we find a '*', we have finished examining all the nodes at a level
            if cur_node == '*':
                if len(level_list) == 0:
                    break

                print level_list
                level_list = []
                bst_q.put('*')

            else:
                # Append all the nodes at a level to the list
                level_list.append(cur_node.data)

                if cur_node.left is not None:
                    bst_q.put(cur_node.left)
                if cur_node.right is not None:
                    bst_q.put(cur_node.right)


    # Use this method to search for the element in a binary search tree
    def search_bst(self, cur_node, search_val):
        if cur_node is None:
            return False

        if cur_node.data == search_val:
            return True
        elif cur_node.data > search_val:
            return self.search_bst(cur_node.left, search_val)
        else:
            return self.search_bst(cur_node.right, search_val)


    # Use this method to print the size i-e the number of nodes that are present in a binary search tree
    def size_bst(self, cur_node):

        if cur_node is None:
            return 0
        else:
            return 1 + self.size_bst(cur_node.left) + self.size(cur_node.right)


    #Use this method to find the maximum depth or height of the binary search tree
    def max_depth_bst(self, cur_node):
        if cur_node is None:
            return 0

        return max( 1 + self.max_depth_bst(cur_node.left), 1 + self.max_depth_bst(cur_node.right))


    #Use this method to find the min depth of the binary search tree
    def min_depth_bst(self, cur_node):
        if cur_node is None:
            return 0

        return min(1 + self.min_depth_bst(cur_node.left), 1 + self.min_depth_bst(cur_node.right))


    # Use this method to find the minimum value of a binary search tree
    def min_value_bst(self, cur_node):
        if cur_node is None:
            return "Tree is emtpy"

        if cur_node.left is None:
            return cur_node.data
        else:
            return self.min_value_bst(cur_node.left)


    # Use this method to find the maximum value of a binary search tree
    def max_value_bst(self, cur_node):
        if cur_node is None:
            return "Tree is empty"

        if cur_node.right is None:
            return cur_node.data
        else:
            return self.max_value_bst(cur_node.right)


    # Use this method to find if there a path in the tree, which sums up to the given value
    def path_sum_bst(self, cur_node, cur_path, path_sum_value):

        new_cur_path = list(cur_path)

        if cur_node is None:
            return False

        else:
            new_cur_path.append(cur_node)

        if cur_node.left is None and cur_node.right is None:
            cur_path_sum_value = 0

            for node in new_cur_path:
                cur_path_sum_value += node.data

            if cur_path_sum_value == path_sum_value:
                for path_node in new_cur_path:
                    print path_node.data,
                return True
            else:
                return False

        else:
            return (self.path_sum_bst(cur_node.left, new_cur_path, path_sum_value) | self.path_sum_bst(cur_node.right, new_cur_path, path_sum_value))


    # Use this method to print all the paths from root in a binary search tree
    def print_paths_bst(self, cur_node, cur_path):
        new_cur_path = list(cur_path)

        if cur_node is None:
            return
        else:
            new_cur_path.append(cur_node)

        if cur_node.left is None and cur_node.right is None:

            for path_node in new_cur_path:
                print path_node.data,

            print ""
        else:
            self.print_paths_bst(cur_node.left, new_cur_path)
            self.print_paths_bst(cur_node.right, new_cur_path)


    #Use this method to get a tree which is the mirror of a binary search tree
    def mirror_bst(self, cur_node):
        if cur_node is None:
            return

        else:
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            self.mirror_bst(cur_node.left)
            self.mirror_bst(cur_node.right)

    def is_bst(self, cur_node):
        print "Is this a BST or not"


    #Use this method to find if a tree is binary search tree or not
    def is_bst_minmax(self, cur_node):

        if cur_node is None:
            return True

        if cur_node.left is not None and self.max_value_bst(cur_node.left) > cur_node.data:
            return False

        if cur_node.right is not None and self.min_value_bst(cur_node.right) < cur_node.data:
            return False

        return self.is_bst_minmax(cur_node.left) and self.is_bst_minmax(cur_node.right)


# This main module needs to be replaced wit unittest module
def main():

    t = Tree()
    t.insert(t.root, 4)
    t.insert(t.root, 3)
    t.insert(t.root, 5)
    t.insert(t.root, 2)
    t.insert(t.root, 1)
    t.insert(t.root, 8)
    t.insert(t.root, 7)
    t.insert(t.root, 9)
    t.insert(t.root, 3.5)
    t.insert(t.root, 4.5)
    t.insert(t.root, 10)
    t.insert(t.root, 11)
    t.insert(t.root, 12)


    #t.print_preorder(t.root)



    search_val = 11
    if t.search_bst(t.root, search_val):
        print "%s is found in the BST" %(search_val)
    else:
        print "%s is not found in the BST" %(search_val)

    print t.max_depth_bst(t.root)
    print t.min_depth_bst(t.root)

    print t.min_value_bst(t.root)

    print t.max_value_bst(t.root)

    print t.path_sum_bst(t.root, [], 10)
    print t.path_sum_bst(t.root, [], 25)
    print t.path_sum_bst(t.root, [], 10.5)
    print t.path_sum_bst(t.root, [], 40)
    print t.path_sum_bst(t.root, [], 13.5)
    print t.path_sum_bst(t.root, [], 24)


    print t.print_paths_bst(t.root, [])
    t.print_bst_by_level()

    t.mirror_bst(t.root)
    t.print_bst_by_level()
main()


