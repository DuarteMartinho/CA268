#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these functions are called methods "A method is a function that is stored as a class attribute"
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

    def count(self):
        head = self.head
        i = 0
        while not head == None:
            head = head.next
            i += 1
        return i

    def contains(self, item):
        head = self.head
        i = 0
        while not head == None:
            Listitem = head.item
            head = head.next
            if Listitem == item:
                return True
            i += 1
        return False

    def after(self, item):
        head = self.head
        i = 0
        nextItem = False
        while not head == None:
            Listitem = head.item
            head = head.next
            if nextItem:
                return Listitem
            if Listitem == item:
                nextItem = True
            i += 1
        return None

import sys

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    tests = [] # list of the results of the tests
    
    ll = LinkedList()

    # Check that it works for an empty list    
    tests.append(ll.after("") == None)  # Each test should be True

    # Check that the item doesn't exist before it is added    
    for item in items:
        tests.append(ll.after(item) == None)
        ll.add(item)
    
    print(tests)
    items.reverse()
    for i in range(len(items) - 1):
        print(items[i], items[i + 1], ll.after(items[i]), items[i+1])
        tests.append(ll.after(items[i]) == items[i+1])
        
    print("All Good" if all(tests) else str(tests))

if __name__ == "__main__":
    main()