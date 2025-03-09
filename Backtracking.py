from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return[[]]
        
        permList:List[List[int]] = self.permute(nums[1:])
        
        res:List[List[int]] = []
        for sPerm in permList:
            for i in range(len(sPerm)+1):
                permCopy = sPerm.copy()
                permCopy.insert(i,nums[0])
                res.append(permCopy)
        return res
    
    # def exist(self, board: List[List[str]], word: str) -> bool:
        

            
                
            
                
                
                
                
                
                
                
                
                
            
            
        
        
        
res = Solution.permute(0,[1,2,3])
print(res)
        