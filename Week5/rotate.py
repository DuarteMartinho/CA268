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

    def rotate(self):
        # firstItem = self.head.item
        firstItem = self.remove()
        lst = []
        
        while not self.head == None:
            newItem = self.head.item
            self.head = self.head.next
            lst.append(newItem)
        lst.append(firstItem)
        newHead = None
        for listItem in reversed(lst):
            if newHead == None:
                newHead = Node(listItem, None)
            else:
                newHead = Node(listItem, newHead)
        self.head = newHead
        
    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += " " + ptr.item
            ptr = ptr.next
        return tmp_str


import sys

def main():
    # Read data from input
    line = sys.stdin.readline()
    items = line.strip().split()

    # Create the linked list
    ll = LinkedList()

    # add the items to the linked list
    for item in items:
        ll.add(item)

    # print the linked list
    print(str(ll))
    ll.rotate() # rotate it
    print(str(ll)) # print it again

    # create the list using append 
    for i in range(len(items)-1):
        ll.rotate() # Rotate enough times should get back to the original
    print(str(ll))

if __name__ == "__main__":
    main()