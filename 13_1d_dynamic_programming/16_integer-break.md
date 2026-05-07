# Integer Break

**Difficulty:** Medium
**Category:** 1-D Dynamic Programming

## Links
- [LeetCode](https://leetcode.com/problems/integer-break/)
- [NeetCode](https://neetcode.io/problems/integer-break)

## Description
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
Return the maximum product you can get.

## Examples

### Example 1
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

### Example 2
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

## Constraints
- 2 <= n <= 58

## Hints
- There is a simple O(n) solution to this problem.
- You may check the breaking results of <i>n</i> ranging from 7 to 10 to discover the regularities.
