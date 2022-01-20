class Stack:
#
#  Stack ADT has three methods: is_empty, push and pop.
#
   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]

def check_brackets(line):
    # print('================================================================')
    stack = Stack()
    check_brackets = True
    for c in line:
        # print(c, stack.is_empty())
        if c == ')' and not stack.is_empty():
            # print('check )')
            val = stack.pop()
            if c == val:
                check_brackets = False
                break
        elif c == ')' and stack.is_empty():
            check_brackets = False
            break
        elif c == '(':
            # print('added (' )
            stack.push(c)
    if (not stack.is_empty()):
        check_brackets = False
    return (check_brackets)


check_brackets("()")
check_brackets(")(")
check_brackets("hello(goo(d)bye)")
check_brackets("hello(goo(d)bye))")