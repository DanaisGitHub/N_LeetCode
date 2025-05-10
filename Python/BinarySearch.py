from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix),len(matrix[0])

        l,r = 0,ROWS-1
        row = -1

        while l<r:
            #mid = l+(r-l // 2) # don't think it's correct
            mid = l+r // 2

            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][COLS-1] < target:
                l = mid + 1
            else:
                row = mid
                break
        
        if row == -1:
            return False

        l,r = 0,COLS-1
        col = -1

        while l<r:
            #mid = l+(r-l // 2) # don't think it's correct
            mid = l+r // 2
            print(mid,l,r)

            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                col = mid
                break
    
        if col == -1:
            print(col)
            return False

        return True



        

        

print(Solution.searchMatrix(0,[[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))