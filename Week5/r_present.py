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

    def count_even(self, head='NotDefined', i=0):
        if head == 'NotDefined':
            head = self.head
        if not head == None:
            if head.item % 2 == 0:
                i += 1
            head = head.next
            return self.count_even(head, i)
        else:
            return i
        
    def is_present(self, item, head='NotDefined'):
        if head == 'NotDefined':
            head = self.head
        if not head == None:
            if head.item == item:
                return True
            head = head.next
            return self.is_present(item, head)
        else:
            return False


