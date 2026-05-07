# Design Add And Search Words Data Structure

**Difficulty:** Medium
**Category:** Tries

## Links
- [LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- [NeetCode](https://neetcode.io/problems/design-word-search-data-structure)

## Description
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
Example:

## Examples

### Example 1
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

## Constraints
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 2 dots in word for search queries.
- At most 104 calls will be made to addWord and search.

## Hints
- You should be familiar with how a Trie works. If not, please work on this problem: <a href="https://leetcode.com/problems/implement-trie-prefix-tree/">Implement Trie (Prefix Tree)</a> first.
