# Binary Tree Level Order Traversal

**Difficulty:** Medium
**Category:** Trees

## Links
- [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [NeetCode](https://neetcode.io/problems/level-order-traversal-of-binary-tree)

## Description
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Examples

### Example 1
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

### Example 2
Input: root = [1]
Output: [[1]]

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

### Example 3
Input: root = []
Output: []

**Images:**
- ![Example 3](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

## Constraints
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

## Hints
- Use a queue to perform BFS.
