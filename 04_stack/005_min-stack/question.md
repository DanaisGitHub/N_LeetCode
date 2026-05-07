# Min Stack

**Difficulty:** Medium
**Category:** Stack

## Links
- [LeetCode](https://leetcode.com/problems/min-stack/)
- [NeetCode](https://neetcode.io/problems/minimum-stack)

## Description
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
You must implement a solution with O(1) time complexity for each function.

## Examples

### Example 1
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

## Constraints
- -231 <= val <= 231 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 104 calls will be made to push, pop, top, and getMin.

## Hints
- Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)
