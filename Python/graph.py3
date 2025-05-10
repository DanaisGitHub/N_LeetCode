from typing import List
from typing import Tuple
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowMax, colMax = len(grid), len(grid[0])
        movements = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        islands = 0

        def dfs(currRow: int, currCol: int) -> None:

            if min(currCol, currRow) < 0 or currCol >= colMax or currRow >= rowMax:
                return
            if grid[currRow][currCol] == '0':
                return

            grid[currRow][currCol] = '0'

            for (ri, ci) in movements:
                dfs(currRow+ri, currCol+ci)

        for r in range(rowMax):
            for c in range(colMax):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        return islands

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # same as before
        # adhog search through the graph until we find an island
        # once we find an island, dfs find all/only that island
        # as you do add 1 to count, and take max of currCount and maxCount

        maxCount = 0
        rowMax, colMax = len(grid), len(grid[0])
        movements = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(currRow: int, currCol: int, count: int) -> int:
            # base cases
            # out of bounds
            if min(currCol, currRow) < 0 or currCol >= colMax or currRow >= rowMax:
                return 0
            if grid[currRow][currCol] == 0:
                return 0

            grid[currRow][currCol] = 0

            for (ri, ci) in movements:
                count = max(count, dfs(currRow+ri, currCol+ci, count+1))
            return count

        for r in range(rowMax):
            for c in range(colMax):
                if grid[r][c] == 1:
                    maxCount = max(maxCount, dfs(r, c, 1))

        return maxCount

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        INF = 2147483647
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        COLUMNS, ROWS = len(grid[0]), len(grid)
        q: deque = deque()
        if grid:
            q.append((grid[0][0], 0, 0))

        def bfsFrom0(cord: Tuple[int, int]):
            bfsQ = deque()
            r, c = cord
            bfsQ.append((grid[r][c], r, c, 0))
            visited = set()

            while bfsQ:
                currNodeValFun, r, c, i = bfsQ.popleft()

                grid[r][c] = min(grid[r][c], i) if grid[r][c] != 0 else 0
                visited.add((r, c))

                for x, y in directions:
                    newR, newC = r+x, c+y
                    if min(newR, newC) < 0 or newR >= ROWS or newC >= COLUMNS or (newR, newC) in visited or grid[newR][newC] == -1:
                        continue  # don't put through
                    bfsQ.append((grid[newR][newC], newR, newC, i+1))

        # find a 0
        for i in range(ROWS):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfsFrom0((i, j))

        print(grid)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = -1
        if not grid or len(grid) == 0:
            return -1

        def bfs(cord: Tuple[int, int],):
            movement = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            r, c = cord
            i = 0
            q = deque()
            q.append((r, c, i))
            counter = 0

            while q:
                r, c, i = q.popleft()
                grid[r][c] = 3
                counter = i

                for r2, c2 in movement:
                    grid[r][c] = 3
                    newR, newC = r+r2, c+c2
                    if min(newR, newC) < 0 or newR >= ROWS or newC >= COLS or grid[newR][newC] == 0 or grid[newR][newC] == 3:
                        continue
                    q.append((newR, newC, i+1))

            return counter

        is2 = False
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    is2 = True
                    res = bfs((i, j))

        if not is2:
            print("hello")
            return -1 if is2 else 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    print("helo")
                    return -1

        return res

    #  your main error is you answered the wrong question
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # need to define what end looks like
        # pacific = (...n,0) or (0,...m)
        # atlantic = (n,...m) or (...n,m)
        # to find if, could add tuples into set
        # for each do edge perform dfs or bfs

        pacificSet, atlanticSet = set(), set()
        pacificList, atlanticList = [], []
        ROWS, COLS = len(heights), len(heights[0])
        movements = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # stupdily you made false = ... and true = 0
        def addEndPoints(nCord: Tuple[int:bool], mCord: Tuple[int:bool], theSet: set, theList: List[int]) -> None:
            endN, nBool = nCord
            endM, mBool = mCord

            startN = 0 if not nBool else endN-1
            startM = 0 if not mBool else endM-1

            for n in range(startN, endN):
                for m in range(startM, endM):
                    theSet.add((n, m))
                    theList.append((n, m))

        addEndPoints((ROWS, False), (1, True), pacificSet, pacificList)
        addEndPoints((1, True), (COLS, False), pacificSet, pacificList)
        addEndPoints((ROWS, False), (COLS, True), atlanticSet, atlanticList)
        addEndPoints((ROWS, True), (COLS, False), atlanticSet, atlanticList)

        # for each position you need to see if path exsits to other set

        def dfs(pos: Tuple[int, int], endGoalSet: set, visited: set()) -> bool:
            r, c = pos
            visited.add((r, c))

            if (r, c) in endGoalSet:
                return True

            for movR, movC in movements:
                newR, newC = r+movR, c+movC
                if min(newR, newC) < 0 or newR >= ROWS or newC >= COLS or (newR, newC) in visited:
                    return False
                if heights[r][c] < heights[newR][newC]:
                    return False
                return False or dfs((newR, newC), endGoalSet, visited)
        res = []
        for x, y in pacificSet:
            if dfs((x, y), atlanticSet, set()):
                res.append([x, y])

        for x, y in atlanticSet:
            if dfs((x, y), pacificSet, set()):
                res.append([x, y])

        return res

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create adj list#

        adjList = {}

        for key, value in edges:
            if key in adjList:
                adjList[key].append(value)
            else:
                adjList[key] = [value]

            if value in adjList:
                adjList[value].append(key)
            else:
                adjList[value] = [key]

        print(adjList)

        # what makes a valid tree,
        # can't have any loops
        # all nodes must be connected, no free nodes

    # init
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList: dict[int, List[int]] = {}
        visted = set()

        for preReq, course in prerequisites:
            if not preReq in adjList:
                adjList[preReq] = []
            if not course in adjList:
                adjList[course] = []
            adjList[preReq].append(course)

        def dfs(key: int) -> bool: # dfs for each element in the key
            if key in visted: # 
                return False
            if adjList[key] == []:
                return True

            visted.add(key)  # Will only contain 1 element aka key

            for course in adjList[key]:
                cycle = not dfs(course)
                if cycle:
                    return False
            
            visted.remove(key)
            
            adjList[key] = [] # clear all children so (almost like dynamic programming)
            
            return True
            
        for postReq, preReq in prerequisites:
            if not dfs(postReq):
                return False
        
        return True


grid = [[1,4],[2,4],[3,1],[3,2]]
x = Solution.validTree(0, 5, grid)
print(x)
