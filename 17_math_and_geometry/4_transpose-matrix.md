# Transpose Matrix

**Difficulty:** Easy
**Category:** Math & Geometry

## Links
- [LeetCode](https://leetcode.com/problems/transpose-matrix)
- [NeetCode](https://neetcode.io/problems/transpose-matrix)

## Description
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

## Examples

### Example 1
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)

### Example 2
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)

## Constraints
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 1000
- 1 <= m * n <= 105
- -109 <= matrix[i][j] <= 109

## Hints
- We don't need any special algorithms to do this. You just need to know what the transpose of a matrix looks like. Rows become columns and vice versa!
