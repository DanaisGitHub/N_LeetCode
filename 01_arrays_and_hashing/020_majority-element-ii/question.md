# Majority Element II

**Difficulty:** Medium
**Category:** Arrays & Hashing

## Links
- [LeetCode](https://leetcode.com/problems/majority-element-ii)
- [NeetCode](https://neetcode.io/problems/majority-element-ii)

## Description
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

## Examples

### Example 1
Input: nums = [3,2,3]
Output: [3]

### Example 2
Input: nums = [1]
Output: [1]

### Example 3
Input: nums = [1,2]
Output: [1,2]

## Constraints
- 1 <= nums.length <= 5 * 104
- -109 <= nums[i] <= 109

## Follow-up
- Could you solve the problem in linear time and in O(1) space?

## Hints
- Think about the possible number of elements that can appear more than ⌊ n/3 ⌋ times in the array.
- It can be at most two. Why?
- Consider using Boyer-Moore Voting Algorithm, which is efficient for finding elements that appear more than a certain threshold.
