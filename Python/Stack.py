from typing import List
class Solution:
    ## Brute force Solution
    def dailyTemperaturesBruteForce(self, temperatures: List[int]) -> List[int]:
        res = []
        i = 0
        for i in range(len(temperatures)):
            
            numToBigger = 0
            for j in range(i,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    numToBigger = j-i
                    break
            
            res.append(numToBigger)
            
        return res
    
    def generateParenthesis(self, n: int) -> List[str]:
        res:List[List[str]]=[]
        
        def dfs(i:int,currBrack:str):
            if i >= n:
                for j in range(len(currBrack),n*2):
                    currBrack += ')'
                
                res.append(currBrack)
                return
            # open
            currBrack +='('
            dfs(i+1,currBrack)
            currBrack+=')'
            dfs(i+1,currBrack)
            
            
        
        dfs(0,"")
        return res
            
            
            # close
            
                
            
    
    
solutionInit = Solution()
print(solutionInit.generateParenthesis(3))
                
            
