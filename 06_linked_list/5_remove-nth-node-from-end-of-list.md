# Remove Nth Node From End of List

**Difficulty:** Medium
**Category:** Linked List

## Links
- [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [NeetCode](https://neetcode.io/problems/remove-node-from-end-of-linked-list)

## Description
Given the head of a linked list, remove the nth node from the end of the list and return its head.

## Examples

### Example 1
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

### Example 2
Input: head = [1], n = 1
Output: []

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

### Example 3
Input: head = [1,2], n = 1
Output: [1]

**Images:**
- ![Example 3](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

## Constraints
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

## Follow-up
- Could you do this in one pass?

## Hints
- Maintain two pointers and update one with a delay of n steps.
