# Network Delay Time

**Difficulty:** Medium
**Category:** Advanced Graphs

## Links
- [LeetCode](https://leetcode.com/problems/network-delay-time/)
- [NeetCode](https://neetcode.io/problems/network-delay-time)

## Description
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

## Examples

### Example 1
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

### Example 2
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

### Example 3
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

**Images:**
- ![Example 3](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

## Constraints
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

## Hints
- We visit each node at some time, and if that time is better than the fastest time we've reached this node, we travel along outgoing edges in sorted order.  Alternatively, we could use Dijkstra's algorithm.
