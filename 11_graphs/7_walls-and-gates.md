# Walls And Gates

**Difficulty:** Medium
**Category:** Graphs

## Links
- [LeetCode](https://leetcode.com/problems/walls-and-gates/)
- [NeetCode](https://neetcode.io/problems/walls-and-gates)

## Description
You have a grid representing a floor plan with rooms, walls, and gates. The grid is an
m x n
matrix where each cell contains one of three values:
-1
represents a wall or obstacle that cannot be passed through
0
represents a gate
2147483647
(which is
2^31 - 1
, also referred to as
INF
) represents an empty room
Your task is to fill each empty room with its shortest distance to the nearest gate. The distance is measured as the minimum number of steps needed to reach a gate from that room, moving only horizontally or vertically (not diagonally).
If an empty room cannot reach any gate because it's blocked by walls, it should remain as
INF
.

> **Note:** This problem description was sourced from algo.monster as the problem is premium on LeetCode.
