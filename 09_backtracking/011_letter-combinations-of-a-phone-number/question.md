# Letter Combinations of a Phone Number

**Difficulty:** Medium
**Category:** Backtracking

## Links
- [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [NeetCode](https://neetcode.io/problems/combinations-of-a-phone-number)

## Description
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## Examples

### Example 1
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

### Example 2
Input: digits = ""
Output: []

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

### Example 3
Input: digits = "2"
Output: ["a","b","c"]

**Images:**
- ![Example 3](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

## Constraints
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].
