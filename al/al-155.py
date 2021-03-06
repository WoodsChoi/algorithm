# 最小栈
'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

提示：
pop、top 和 getMin 操作总是在 非空栈 上调用。

'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._minStack = []


    def push(self, x: int) -> None:
        self._stack.append(x)
        if len(self._minStack) == 0:
            self._minStack.append(x)
        else:
            min = self._minStack[-1]
            if x < min:
                self._minStack.append(x)
            else:
                self._minStack.append(min)

    def pop(self) -> None:
        self._stack.pop(-1)
        self._minStack.pop(-1)

    def top(self) -> int:
        return self._stack[-1]


    def getMin(self) -> int:
        return self._minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()