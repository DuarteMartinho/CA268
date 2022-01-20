#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None
#  cat dog pig ability babysit pat bun
    def append(self, item):
        if self.head == None:
            self.head = Node(item, self.head)
        else:
            newHead = Node(item, None)
            lst = []
            while not self.head == None:
                newItem = self.head.item
                self.head = self.head.next
                lst.append(newItem)
            for listItem in reversed(lst):
                newHead = Node(listItem, newHead)
            self.head = newHead
        
    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + " "
            ptr = ptr.next
        return tmp_str

import sys

def main():
    # Read data from input
    line = sys.stdin.readline()
    items = line.strip().split()
    
    ll = LinkedList()
    ll.append("o")
    if str(ll) != "o ":
        print("Doesn't work for one element")
    ll = LinkedList()

    for item in items:
        ll.add(item)
        
    print(str(ll))
    ll.append("xxx")
    print(str(ll))

    ll = LinkedList()

    # create the list using append 
    for item in items:
        ll.append(item)
    print(str(ll))
    
if __name__ == "__main__":
    main()