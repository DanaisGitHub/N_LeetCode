# Construct Binary Tree From Preorder And Inorder Traversal

**Difficulty:** Medium
**Category:** Trees

## Links
- [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [NeetCode](https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal)

## Description
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## Examples

### Example 1
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

### Example 2
Input: preorder = [-1], inorder = [-1]
Output: [-1]

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

## Constraints
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.
