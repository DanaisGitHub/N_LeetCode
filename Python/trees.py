from collections import deque
from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # for every node you're about to put into quue

        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            currQueue = queue.popleft()
            
            tempStore = currQueue.left
            currQueue.left = currQueue.right
            currQueue.right = tempStore
            
            if currQueue.left:
                queue.append(currQueue.left)
            if currQueue.right:
                queue.append(currQueue.right)
          
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkIsSame(root2:Optional[TreeNode],subRoot2:Optional[TreeNode])->bool:
            queues = deque()
            res2 = True
            if root and subRoot:
                queues.append((root2,subRoot2))
            while queues and res2:
                currRoot,currSubRoot = queues.popleft()
                
                if currRoot.val != currSubRoot.val:
                    res2 = False
                    break


                if currRoot.left and currSubRoot.left:
                    queues.append((currRoot.left,currSubRoot.left))
                if currRoot.right and currSubRoot.right:
                    queues.append((currRoot.right,currSubRoot.right))
                
                if (currRoot.left or currSubRoot.left)and not (currRoot.left and currSubRoot.left):
                    res2 = False 
                    break
                if (currRoot.right or currSubRoot.right) and not (currRoot.right and currSubRoot.right):
                    res2 = False
                    break
    
            return res2
        
        q = deque()
        res = False
        if root:
            q.append(root)
        while (q and not res) == True:
            currQ = q.popleft()
            if currQ.val == subRoot.val:
                res = checkIsSame(currQ,subRoot)
                print(res)
            
            if currQ.left:
                q.append(currQ.left)
            if currQ.right:
                q.append(currQ.right)

        return res
    
    def checkIsSame(self, root2:Optional[TreeNode],subRoot2:Optional[TreeNode])->bool:
            queues = deque()
            res2 = True
            if root and subRoot:
                queues.append((root2,subRoot2))
            while queues and res2:
                currRoot,currSubRoot = queues.popleft()
                
                if currRoot.val != currSubRoot.val:
                    res2 = False
                    break


                if currRoot.left and currSubRoot.left:
                    queues.append((currRoot.left,currSubRoot.left))
                if currRoot.right and currSubRoot.right:
                    queues.append((currRoot.right,currSubRoot.right))
                
                if (currRoot.left or currSubRoot.left)and not (currRoot.left and currSubRoot.left):
                    res2 = False 
                    break
                if (currRoot.right or currSubRoot.right) and not (currRoot.right and currSubRoot.right):
                    res2 = False
                    break
    
            return res2
        
        

                
            