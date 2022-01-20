class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

lst = []
def add_to_queue(head, item):
   while not head == None:
      if head.next == None:
         head = Node(item, head)
         break
      head = head.next
   return head

class LinkedListQueue:
   def __init__(self):
      self.head = None

   def is_empty(self):
      return self.head == None

   def dequeue(self):
      if self.is_empty():
         return None
      else:
         tmp = self.head.item
         self.head = self.head.next
         return tmp

   def enqueue(self, item):
      if self.head == None:
         self.head = Node(item, None)
      else:
         self.head = add_to_queue(self.head, item);


def main():

    lq = LinkedListQueue()
    for x in [3, 4, 5, 6, 7, 8, ]:
      #   print('================================================================')
        lq.enqueue(x)

    while not lq.is_empty():
        print(lq.dequeue())

if __name__ == "__main__":
    main()