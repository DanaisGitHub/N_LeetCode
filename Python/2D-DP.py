from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        # mem: dict[tuple, int] = {}

        # for x in range(m+1):
        #     for y in range(n+1):
        #         mem[(x, y)] = 0

        # mem[(ROWS-1, COLS-1)] = 1

        # # caching / mem
        # def dfsMem(r: int, c: int) -> int:
        #     if min(r, c) < 0 or r >= ROWS or c >= COLS:
        #         return 0

        #     if (r, c) in mem and mem[(r, c)] != 0:
        #         return mem[(r, c)]

        #     mem[(r, c)] = dfsMem(r+1, c) + dfsMem(r, c+1)

        #     return mem[(r, c)]

        # return dfsMem(0,0)

        # 2d dp

        # [0] * cols = 1 ref repeated ROWS times
        dpGrid: List[List[int]] = [[0] * COLS]*ROWS
        ROWS, COLS = m, n
        dpGrid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for row in dpGrid:
            row[COLS-1] = 1

        dpGrid[-1] = [1] * COLS

        for r in range(ROWS-2, -1, -1):
            for c in range(COLS-2, -1, -1):
                dpGrid[r][c] += dpGrid[r+1][c] + dpGrid[r][c+1]

        return dpGrid[0][0]

    [[6, 5, 4, 3, 2, 1],
     [6, 5, 4, 3, 2, 1],
     [6, 5, 4, 3, 2, 1],
     [1, 1, 1, 1, 1, 1]]


##############################


    def maxProfit(self, prices: List[int]) -> int:

        def calculate(i: int, buyOrSell: bool) -> int:
            if i >= len(prices):
                return 0
            mem: dict[tuple[int, bool], int] = {}

            cooldown: int = calculate(i+1, buyOrSell)

            if buyOrSell:
                # huh? in the buy branch - value of purchase
                buy: int = calculate(i+1, not buyOrSell) - prices[i] if not (i,buyOrSell) in mem else mem[(i,bu)]
                mem[i, buyOrSell] = max(buy, cooldown)
            else:
                sell: int = calculate(i+1, not buyOrSell) + prices[i]
                mem[i, buyOrSell] = max(buy, cooldown)

            return mem

        return calculate(0, True)


prices = [1, 3, 4, 0, 4]
res = Solution.maxProfit(None, prices)
print(res)


from typing import List

class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self,word:str):
    node = self.root
    for char in word:
      if char not in node.children:
        node.children[char] = TrieNode()
      node = node.children[char]
    node.endOfWord = True

  def search(self,word):
    node = self.root
    for char in word:
      if char not in node.children:
        return False
      node = node.children[char]
    return node.endOfWord

      
def ArrayChallenge(strArr):
    target_string = strArr[0]
    dictionary_string = strArr[1]
    varFiltersCg = dictionary_string.split(',') 
    trie = Trie()
    for word in varFiltersCg:
        trie.insert(word)

    n = len(target_string)
    for i in range(1, n):
        word1 = target_string[:i]
        word2 = target_string[i:]
        if trie.search(word1) and trie.search(word2):
            return f"{word1},{word2}"

    return "not possible"

def format_output(output_string, challenge_token):
    combined_string = output_string + 's6fu1omga4c'
    formatted_string = ""
    for i, char in enumerate(combined_string):
        if (i + 1) % 3 == 0:
            formatted_string += "X"
        else:
            formatted_string += char
    return formatted_string
# keep this function call here 
print(format_output(ArrayChallenge(input()),'s6fu1omga4c'))




