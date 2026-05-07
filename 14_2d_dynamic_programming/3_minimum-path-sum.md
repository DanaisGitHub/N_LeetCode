# Minimum Path Sum

**Difficulty:** Medium
**Category:** 2-D Dynamic Programming

## Links
- [LeetCode](https://leetcode.com/problems/minimum-path-sum/)
- [NeetCode](https://neetcode.io/problems/minimum-path-sum)

## Description
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

## Examples

### Example 1
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

### Example 2
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200
