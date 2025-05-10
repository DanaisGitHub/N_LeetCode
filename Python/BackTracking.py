from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        permList: List[List[int]] = self.permute(nums[1:])

        res: List[List[int]] = []
        for sPerm in permList:
            for i in range(len(sPerm)+1):
                permCopy = sPerm.copy()
                permCopy.insert(i, nums[0])
                res.append(permCopy)
        return res

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # idea is to back track whilst adding a total,
        # Only once we have reached the leave do we check if total is added
        if not root:
            return False

        def dfs(currNode: Optional[TreeNode], total: int) -> bool:
            if not currNode:  # not how you Id a leaf node
                return False

            # leaf node = no left or right children
            if not currNode.left and not currNode.right:
                return total + currNode.val == targetSum

            leftValues = dfs(currNode.left, total + currNode.val)
            if leftValues:
                return True
            rightValues = dfs(currNode.right, total+currNode.val)
            if rightValues:
                return True

            return False  # Not sure How this effects

        return dfs(root, 0)

    def subSets(self, nums: List[int]) -> List[List[int]]:
        curArray, res = [], []

        def dfs(i: int, curArray: List[int]) -> None:
            # Base case
            # at the end of leaf node
            if i >= len(nums):
                # you add the reference when you alter currArray you will alter answer
                res.append(curArray.copy())
                return  # stop execution

            # makes choice

            # 1 add in the num
            curArray.append(nums[i])
            dfs(i+1, curArray)

            # 2 remove the num
            curArray.pop()
            dfs(i+1, curArray)
        dfs(0, curArray)
        return res

    # what should you do with subsets that
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # if it's unique add it in, if it already exists just different form then
        # remeber the definition of a set (unique values)

        res: List[List[int]] = []
        nums.sort()

        def dfs(i: int, curArray: List[int]):
            # Base case
            if i >= len(nums):
                res.append(curArray.copy())
                return
            # may need another

            # should only create new braches for unique values
            # now great question are we to assume that all first values are unique,
            # I think no move i until i+1 != i
            # if I i =n the do 1

            curArray.append(nums[i])

            dfs(i+1, curArray)
            # for each new i we add but we don't replicate branches for removing braches
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            curArray.pop()
            dfs(i+1, curArray)

        dfs(0, [])
        return res

    def combineOLD(self, n: int, k: int) -> List[List[int]]:
        # lets just do it normal
        res: List[List[int]] = []

        def dfs(i: int, curArr: List[int]):
            if len(curArr) == k:
                res.append(curArr.copy())
                return
            # Just because I remember
            if i >= n+1:  # due to empty array
                return

            # choice to add
            curArr.append(i)
            dfs(i+1, curArr)
            curArr.pop()
            dfs(i+1, curArr)

        dfs(1, [])
        return res
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        # lets just do it normal
        return []
       
       
    def letterCombinations(self, digits: str) -> List[str]:
        return []
        # Cant think of a data strcutre that would allow this
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        return []



fun = Solution()
res = fun.combine(4, 2)
print(res)
