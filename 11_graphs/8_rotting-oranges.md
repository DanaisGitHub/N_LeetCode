# Rotting Oranges

**Difficulty:** Medium
**Category:** Graphs

## Links
- [LeetCode](https://leetcode.com/problems/rotting-oranges/)
- [NeetCode](https://neetcode.io/problems/rotting-fruit)

## Description
You are given an m x n grid where each cell can have one of three values:
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

## Examples

### Example 1
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

### Example 2
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

### Example 3
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

**Images:**
- ![Example 3](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.
