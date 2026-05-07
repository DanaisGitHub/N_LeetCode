# Word Search II

**Difficulty:** Hard
**Category:** Tries

## Links
- [LeetCode](https://leetcode.com/problems/word-search-ii/)
- [NeetCode](https://neetcode.io/problems/search-for-word-ii)

## Description
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Examples

### Example 1
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)

### Example 2
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)

## Constraints
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 104
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.

## Hints
- You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
- If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: <a href="https://leetcode.com/problems/implement-trie-prefix-tree/">Implement Trie (Prefix Tree)</a> first.
