# Reorder List

**Difficulty:** Medium
**Category:** Linked List

## Links
- [LeetCode](https://leetcode.com/problems/reorder-list/)
- [NeetCode](https://neetcode.io/problems/reorder-linked-list)

## Description
You are given the head of a singly linked-list. The list can be represented as:
Reorder the list to be on the following form:
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Examples

### Example 1
L0 → L1 → … → Ln - 1 → Ln

### Example 2
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

### Example 3
Input: head = [1,2,3,4]
Output: [1,4,2,3]

**Images:**
- ![Example 3](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

### Example 4
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

**Images:**
- ![Example 4](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

## Constraints
- The number of nodes in the list is in the range [1, 5 * 104].
- 1 <= Node.val <= 1000
