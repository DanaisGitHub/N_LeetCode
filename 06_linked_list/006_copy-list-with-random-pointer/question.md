# Copy List With Random Pointer

**Difficulty:** Medium
**Category:** Linked List

## Links
- [LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/)
- [NeetCode](https://neetcode.io/problems/copy-linked-list-with-random-pointer)

## Description
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
Your code will only be given the head of the original linked list.

## Examples

### Example 1
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

**Images:**
- ![Example 1](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

### Example 2
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

**Images:**
- ![Example 2](https://assets.leetcode.com/uploads/2019/12/18/e2.png)

### Example 3
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

**Images:**
- ![Example 3](https://assets.leetcode.com/uploads/2019/12/18/e3.png)

## Constraints
- 0 <= n <= 1000
- -104 <= Node.val <= 104
- Node.random is null or is pointing to some node in the linked list.

## Hints
- Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, ensure you are not making multiple copies of the same node.
- You may want to use extra space to keep old_node ---> new_node mapping to prevent creating multiple copies of the same node.
- We can avoid using extra space for old_node ---> new_node mapping by tweaking the original linked list. Simply interweave the nodes of the old and copied list. For example:
Old List: A --> B --> C --> D
InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
- The interweaving is done using next</b> pointers and we can make use of interweaved structure to get the correct reference nodes for random</b> pointers.
