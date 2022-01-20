class Node:
    def __init__(self):
        self.item = None
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None

    def push(self, item):
        oldtop = self.top
        self.top = Node()
        self.top.item = item
        self.top.next = oldtop

    def pop(self):
        item = self.top.item
        self.top = self.top.next
        return item

class Queue:
    def __init__(self):
        self.q = Stack()
        

    def isempty(self):
        return self.q.isempty()

    def enqueue(self, item):
        self.q.push(item)

    def dequeue(self):
        if not self.q.isempty():
            listCopy = Stack()
            while not self.q.isempty():
                listCopy.push(self.q.pop())
            popval = listCopy.pop()
            self.q = Stack()
            while not listCopy.isempty():
                self.q.push(listCopy.pop())
            return popval
        else:
            return None

def main():
   q = Queue()

   command = input()
   while len(command) > 0:
      print(command + ":", end="")
      if command[0] == 'a': # add
         item = command.split()[1]
         q.enqueue(int(item));
      elif command[0] == 'r': # remove
         print(q.dequeue(), end="");
      else:
         print("Unknown command!")
      print(" _" if q.isempty() else " *")
      command = input()
   print()

if __name__ == "__main__":
   main()