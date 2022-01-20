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

    def __str__(self):
        tmp_str = ""
        ptr = self.head
        print(ptr != None)
        while ptr != None:
            tmp_str += " " + str(ptr.item) # Spent ages trying to fix bug ... had = stat +=
            ptr = ptr.next
            if ptr == self.head:
                tmp_str += " xx Loop xx"
                break
                
        return tmp_str

def detect_loop(lst):
    head = lst.head
    val = True
    while not lst.head == None:
        lst.head = lst.head.next
        if head == lst.head:
            val = False
            break
    return ((not (lst.is_empty())) and (not val))

import sys

def make_ll(line):
    items = line.strip().split()

    ll = LinkedList()

    for item in items:
        ll.add(item)

    return ll

def make_long_list():
    lst = [x for x in range(1, 3000, 10)]
    ll = LinkedList()
    for item in lst:
        ll.add(item)

    return ll

def add_head_loop(lst):
    # Add a loop to this list. Normally a bad thing ... here it is just to test the student program
    if lst.head != None: # Need at least one item for a loop
        if lst.head.next == None:
            lst.head.next = lst.head
        else:
            ptr = lst.head
            while ptr.next != None:
                ptr = ptr.next

            ptr.next = lst.head

def main():

    lists = []
    for line in sys.stdin:
        # Create two versions of this LinkedList
        no_loop = make_ll(line) # one normal list
        loop = make_ll(line)    # one with a loop
        add_head_loop(loop)     # ... need to add the loop

        # Add these two lists
        lists.append(no_loop)
        lists.append(loop)

    # Add a couple of long lists to the tests
    ll = make_long_list()
    lists.append(ll)

    ll = make_long_list()
    add_head_loop(ll)
    lists.append(ll)

    # add an empty list to the mix
    lists.append(LinkedList())

    # Test the students function against all these lists
    for lst in lists:
        print("Loop" if detect_loop(lst) else "Noop", lst)


if __name__ == "__main__":
    main()