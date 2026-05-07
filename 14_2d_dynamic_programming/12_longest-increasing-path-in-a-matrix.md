# Longest Increasing Path In a Matrix

**Difficulty:** Hard
**Category:** 2-D Dynamic Programming

## Links
- [LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
- [NeetCode](https://neetcode.io/problems/longest-increasing-path-in-matrix)

## Description
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

## Examples

### Example 1
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg)

### Example 2
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg)

### Example 3
Input: matrix = [[1]]
Output: 1

**Images:**
- ![Example 3](https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg)

## Constraints
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 231 - 1
