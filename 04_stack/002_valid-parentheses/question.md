# Valid Parentheses

**Difficulty:** Easy
**Category:** Stack

## Links
- [LeetCode](https://leetcode.com/problems/valid-parentheses/)
- [NeetCode](https://neetcode.io/problems/validate-parentheses)

## Description
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

## Examples

### Example 1
Input: s = "()"
Output: true

### Example 2
Input: s = "()[]{}"
Output: true

### Example 3
Input: s = "(]"
Output: false

### Example 4
Input: s = "([])"
Output: true

### Example 5
Input: s = "([)]"
Output: false

## Constraints
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

## Hints
- Use a stack of characters.
- When you encounter an opening bracket, push it to the top of the stack.
- When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.
