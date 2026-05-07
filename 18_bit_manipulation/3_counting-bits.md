# Counting Bits

**Difficulty:** Easy
**Category:** Bit Manipulation

## Links
- [LeetCode](https://leetcode.com/problems/counting-bits/)
- [NeetCode](https://neetcode.io/problems/counting-bits)

## Description
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

## Examples

### Example 1
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

### Example 2
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

## Constraints
- 0 <= n <= 105

## Hints
- You should make use of what you have produced already.
- Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
- Or does the odd/even status of the number help you in calculating the number of 1s?
