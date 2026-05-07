# Number of Connected Components In An Undirected Graph

**Difficulty:** Medium
**Category:** Graphs

## Links
- [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- [NeetCode](https://neetcode.io/problems/number-of-connected-components-in-an-undirected-graph)

## Description
You are given a graph with
n
nodes labeled from
0
to
n-1
. The graph is represented by an integer
n
(the number of nodes) and an array
edges
, where each element
edges[i] = [ai, bi]
indicates that there is an undirected edge connecting nodes
ai
and
bi
.
Your task is to find and return the total number of connected components in the graph.
A connected component is a group of nodes where there is a path between any two nodes in the group, and these nodes are not connected to any other nodes outside the group. In other words, it's a maximal set of nodes that are all reachable from each other through the edges.
For example, if you have 5 nodes
(0, 1, 2, 3, 4)
and edges
[[0,1], [2,3]]
, there would be 3 connected components:
Component 1: nodes
{0, 1}
(connected by an edge)
Component 2: nodes
{2, 3}
(connected by an edge)
Component 3: node
{4}
(isolated node with no edges)

> **Note:** This problem description was sourced from algo.monster as the problem is premium on LeetCode.
