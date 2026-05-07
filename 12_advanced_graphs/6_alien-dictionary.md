# Alien Dictionary

**Difficulty:** Hard
**Category:** Advanced Graphs

## Links
- [LeetCode](https://leetcode.com/problems/alien-dictionary/)
- [NeetCode](https://neetcode.io/problems/alien-dictionary)

## Description
You're given a list of words from an alien language that uses the same 26 letters as English, but the alphabetical order of these letters is different and unknown to you.
The words are claimed to be sorted in dictionary order according to this alien alphabet. Your task is to:
Verify if the claim is valid
: Check if the given word order can actually correspond to some valid alphabetical ordering of letters. If not, return an empty string
""
.
Recover the alien alphabet
: If the ordering is valid, determine what the alphabetical order of letters must be in this alien language and return it as a string containing all unique letters that appear in the words, sorted according to the alien alphabet's rules.
Key Points:
The words should follow lexicographic ordering based on the alien alphabet (like how words are ordered in a dictionary)
You need to deduce the relative order of letters by comparing adjacent words in the list
If there are multiple valid orderings possible, return any one of them
If the given arrangement is impossible (contradicts itself), return
""
Example of Invalid Input:
If you have words like
["abc", "ab"]
, this would be invalid because in any alphabet, "abc" cannot come before "ab" in dictionary order (a longer word with the same prefix must come after the shorter word).
Example of Deducing Order:
If you have words
["wrt", "wrf"]
, you can deduce that
't'
comes before
'f'
in the alien alphabet since these words differ at the third position and "wrt" comes before "wrf".

> **Note:** This problem description was sourced from algo.monster as the problem is premium on LeetCode.
