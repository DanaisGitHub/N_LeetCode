# Kth Smallest Element In a Bst

**Difficulty:** Medium
**Category:** Trees

## Links
- [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [NeetCode](https://neetcode.io/problems/kth-smallest-integer-in-bst)

## Description
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

## Examples

### Example 1
Input: root = [3,1,4,null,2], k = 1
Output: 1

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

### Example 2
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

## Constraints
- The number of nodes in the tree is n.
- 1 <= k <= n <= 104
- 0 <= Node.val <= 104

## Follow-up
- If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

## Hints
- Try to utilize the property of a BST.
- Try in-order traversal. (Credits to @chan13)
- What if you could modify the BST node's structure?
- The optimal runtime complexity is O(height of BST).
