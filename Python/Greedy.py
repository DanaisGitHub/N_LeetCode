from typing import List
from collections import Counter


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        i = 0
        while i < len(nums)-1:
            endJump = min(len(nums)-1, i+nums[i])
            maxJumpI = (-1, -1)  # index, jump
            for j in range(i+1, endJump+1):
                if j == len(nums)-1:
                    return jumps+1
                tempMaxJumpI = (j, nums[j])  # index + jump
                maxJumpI = maxJumpI if (maxJumpI[0]+maxJumpI[1]) >= (
                    tempMaxJumpI[0]+tempMaxJumpI[1]) else (tempMaxJumpI[0], tempMaxJumpI[1])
            i = maxJumpI[0]
            jumps += 1

        return jumps

    def jumpRec(self, nums: List[int]) -> int:
        def dfs(i: int, jumps: int) -> int:
            if i == len(nums)-1:
                return jumps
            if nums[i] == 0:
                return float('inf')
            end = min(len(nums)-1, nums[i]+i)
            minJumps = float('inf')
            for j in range(i+1, end+1):
                # Find min jump for this round of jumps
                minJumps = min(minJumps, dfs(j, jumps + 1))

            return minJumps
        return dfs(0, 0)

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counter = Counter(hand)
        hand.sort()

        for num in hand:
            if not counter[num]:
                continue
            for i in range(num, num+groupSize):
                if counter[i] <= 0:
                    return False
                counter[i] -= 1
        return True

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 0 :
            return False
        if len(triplets) == 1:
            target == triplets[1]

        removeArray = []
        for i in range(len(triplets)):
            for j in range(len(triplets[i])):
                if triplets[i][j] > target[j]:
                    removeArray.append(i)
                    break

        removeArray.sort(reverse = True)

        for index in removeArray:
            triplets.pop(index)
        
        if len(triplets) == 0 :
            return False
        if len(triplets) == 1:
            return target == triplets

        maxArray = triplets[0]
        for i in range(len(triplets)):
            for j in range(len(triplets[i])):
                maxArray[j] = max(maxArray[j],triplets[i][j])

        return target == maxArray
        

        


solver = Solution()
result = Solution().mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5])
print(result)
