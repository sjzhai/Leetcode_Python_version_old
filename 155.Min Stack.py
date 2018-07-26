'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

   push(x) -- Push element x onto stack.
   pop() -- Removes the element on top of the stack.
   top() -- Get the top element.
   getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minstack) == 0 or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            if self.stack[-1] == self.minstack[-1]:
                self.minstack = self.minstack[:-1]
            self.stack = self.stack[:-1]

    def top(self): #return
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self): #return
        """
        :rtype: int
        """
        print(self.stack)
        if len(self.stack) == 1:
            return self.stack[0]

        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
###Debug

obj = MinStack()
li1 = ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
li2 = [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]

obj.push(-2)
obj.push(0)
obj.push(-3)
# obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
# print(obj.getMin())
# obj.pop()
# print(obj.getMin())
# obj.pop()
# print(obj.getMin())
# print(obj.top())
# print(obj.getMin())
