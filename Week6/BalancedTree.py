class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)

def make_list(lst):
    left = []
    right = []
    sortedlist = sorted(lst)
    left.append(sortedlist.pop(len(lst)//2))
    if len(sortedlist)>0:
        right.append(sortedlist[:len(lst)//2])
        right.append(sortedlist[len(lst)//2:])
        while len(left) != len(lst):
            if right[0] != []:
                left.append(right[0][len(right[0])//2])
                popped = right.pop(0)
                right.append(popped[:len(popped)//2])
                right.append(popped[len(popped)//2+1:])
            else:
                right.pop(0)
    return left

import random

def main():
    random.seed(0)
    
    for length in [1, 2, 3, 4, 7, 8, 15, 16, 31, 32, 50, 100]:
        # Make a random lst
        lst = random.sample(range(length), length)

        # Use the students function to arramge the list
        new_list = make_list(lst) # get the student's lst

        # Make sure they have the same elements
        if sorted(lst) != sorted(new_list):
            print("You have somehow changed the elements of the list. You are only supposed to change the order.")
        else:
            # Create a BST
            tree = BST()
            # and add in the elements from the list
            for element in new_list:
                tree.add(element)
            # Show the lst
            print(lst)
            # And some data ... the height, the count and whether or not balanced.
            # print(tree.max_height(), tree.count(), tree.is_balanced())

if __name__ == "__main__":
    main()