# Valid Parenthesis String

**Difficulty:** Medium
**Category:** Greedy

## Links
- [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/)
- [NeetCode](https://neetcode.io/problems/valid-parenthesis-string)

## Description
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:

## Examples

### Example 1
Input: s = "()"
Output: true

### Example 2
Input: s = "(*)"
Output: true

### Example 3
Input: s = "(*))"
Output: true

## Constraints
- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'.

## Hints
- Use backtracking to explore all possible combinations of treating '*' as either '(', ')', or an empty string. If any combination leads to a valid string, return true.
- DP[i][j] represents whether the substring s[i:j] is valid.
- Keep track of the count of open parentheses encountered so far. If you encounter a close parenthesis, it should balance with an open parenthesis. Utilize a stack to handle this effectively.
- How about using 2 stacks instead of 1? Think about it.
