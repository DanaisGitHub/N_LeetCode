# Implement Stack Using Queues

**Difficulty:** Easy
**Category:** Stack

## Links
- [LeetCode](https://leetcode.com/problems/implement-stack-using-queues/)
- [NeetCode](https://neetcode.io/problems/implement-stack-using-queues)

## Description
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
Implement the MyStack class:
Notes:

## Examples

### Example 1
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

## Constraints
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, top, and empty.
- All the calls to pop and top are valid.
