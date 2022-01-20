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

    def is_present(self, item, head='NotDefined'):
        if head == 'NotDefined':
            head = self.head
        if not head == None:
            if head.item == item:
                return True
            head = head.next
            return self.count_even(self, item, head)
        else:
            return False
        
    def largest(self, head='NotDefined', largest='NotDefined'):
        if head == 'NotDefined':
            head = self.head
            largest = head.item
        if not head == None:
            if head.item > largest:
                largest = head.item
            head = head.next
            return self.largest(head, largest)
        else:
            return largest
        
    def duplicates(self, head='NotDefined'):
        if head == 'NotDefined':
            head = self.head
            return self.duplicates(head)
        if head == None:
            return False
        elif head.next != None and head.item == head.next.item:
            return True
        else:
            return self.duplicates(head.next)

import sys
def main():
    # Create a list for the tests
    tests = []
    
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items] # Create an array of nums from the strings
    
    ll = LinkedList()

    # Add each number to the list
    for num in nums:
        ll.add(num)
    
    print(ll.largest(), max(nums))
    # call the students function
    tests.append(ll.largest() == max(nums)) # First test ... compare students function to max
    
    # Keep reducing the list, comparing the largest of the reduced list to the remiaining numbers.
    count = 1
    while count == len(nums):
        ll.remove() # Remove one element from the list
        # Compare the largest of this list with the remaining numbers
        tests.append(ll.largest() == max(nums[count:]))
        count += 1
        
    if all(tests):
        print("All tests passed!")
    else:
        for i in range(len(tests)):
            if not tests[i]:
                print("test " + str(i) + " failed.")

if __name__ == "__main__":
    main()