from typing import List
from typing import DefaultDict
from typing import Deque


class Solution:
    def climbStairs(self, n: int) -> int:

        # recursive
        def dfsRec(num: int) -> int:
            if num == 1:
                return 1
            if num == 2:
                return 2
            return dfsRec(num-2) + dfsRec(num-1)

        # memoization (Bottom Down)
        def dfsMem(num: int, memoisation: dict[int, int]):
            if num in memoisation:
                return memoisation[num]
            memoisation[num] = dfsMem(num-1, memoisation) + \
                dfsMem(num-2, memoisation)

            return memoisation[num]

        # recursive bottom - up

        # init empty array of size x

        # dynamic step, the amount of path to from prev-2 + prev-1 = curr

        if n <= 2:
            return n

        dp = [0] * (n)  # dp = [0,0,...,0]

        dp[0], dp[1] = 1, 2
        for i in range(2, n):  # why
            dp[i] = dp[i-2] + dp[i-1]

        return dp[-1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def recurion(i: int):
            if i >= len(cost):
                return 0
            return cost[i] + min(recurion(i+1), recurion(i+2))
        # return min(recurion(0), recurion(1))

        # mem
        def rec(i: int, mem: dict[int, int]) -> int:
            if i >= len(cost):
                return 0
            if i in mem:
                return mem[i]

            mem[i] = cost[i] + min(rec(i+1), rec(i+2))

            return mem[i]
        # return min(rec(0, {1: 1, 2: 2}), rec(1, {1: 1, 2: 2}))

        # Dynamic Programming
        n = len(cost)
        nAdd1 = n+1
        dp = [0] * nAdd1
        for i in range(2, n+1):
            # dp = total cost to get (ne i) there cost = cost of i
            dp[i] += min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        # backwards going doing min m

        # With memory
        n = len(nums)
        # dp = [0] * n

        # if len(nums) == 1:
        #     return nums[-1]
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])

        # i = n-1
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # start = 1 if nums[0] >= nums[1] else 2
        # for i in range(start, n):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # return dp[-1]

    # dp without memory
        start = 1 if nums[0] >= nums[1] else 2
        for i in range(start, n):
            temp = max(nums[i+1],pre)

    # def numDecodings(self, s: str) -> int:
    #     if s == '0':
    #         return 0

    #     def dfs (l:int,r:int)->int:
    #         num = int(s[l:r])
    #         if l > len(s) or r>= len(s):
    #             return 1
    #         if num < 1 or num > 26:
    #             return 0# need to remove by amount of len code
            
    #         return dfs(l,r+2)+dfs(l+1,r+1)
    
    #     return dfs(0,1)   
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def dfs(index: int) -> int:
            # Base Case 1: Successfully reached the end of the string
            if index == n:
                return 1

            # Base Case 2: Current character is '0', cannot decode
            if s[index] == '0':
                return 0

            # --- Calculate ways ---

            # Choice 1: Decode single digit (s[index])
            # This is always possible if s[index] != '0' (checked above)
            ways = dfs(index + 1)

            # Choice 2: Decode two digits (s[index:index+2])
            # Check if there are enough characters left AND if the 2-digit number is valid (10-26)
            if index + 1 < n:
                # Check for leading zero is implicitly handled by the range 10-26
                two_digit_num = int(s[index : index + 2])
                if 10 <= two_digit_num <= 26:
                    ways += dfs(index + 2) # Add ways from the two-digit choice

            # Return the total ways calculated for this index
            return ways

        # Start the recursion from the beginning of the string
        # Handle empty string case explicitly if needed, though constraints say length >= 1
        if not s:
             return 0
        return dfs(0)
 
        
            
            
            

sol = Solution()
res = sol.numDecodings("226")
print(res)
