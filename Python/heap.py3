from typing import List
import heapq
import math


class KthLargest:

    # Using a max-heap of size k, the kth element in the heap is the k biggest

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # only keep k elements in the heap

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: x*-1, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            heapq.heappush(stones, -1*abs(x-y))
            print(x, y, abs(x-y), stones)
        return stones[0] * -1

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # So I Need to caluculate
        res = []

        def eculidDistance(x1, y1, x2, y2): return (
            math.sqrt(abs(x1-x2) ** 2 + (abs(y1-y2)) ** 2))

        for point in points:
            point.insert(0, -1*eculidDistance(0, 0, point[0], point[1]))

        heapq.heapify(points)
        print(points)

        while len(points) > k:
            heapq.heappop(points)

        for p in points:
            res.append([p[1], p[2]])

        return res

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[k-1]
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # a bit of sticky one stilll
        # each task must be serated by at n 
        # could label each in 
        return 1
        

    
    
        
    

    
    
        


print(Solution.findKthLargest(0,  [2,3,1,5,4], 2))
