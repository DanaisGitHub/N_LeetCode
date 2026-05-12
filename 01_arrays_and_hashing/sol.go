package main

import (
	"fmt"
	"sort"
	"strings"
)

// 1. Concatenation Of Array
func concatenationOfArray( /* TODO */ ) /* TODO */ {
	// TODO

}

// 2. Contains Duplicate
func containsDuplicate( /* TODO */ ) /* TODO */ {
	// TODO

}

func isAnagram(s string, t string) bool {
	// sort strings into same order & check if it's the same
	// time O(n logn)
	// space O(n)
	order := func(s string) string {
		x := strings.Split(s, "")
		sort.Strings(x)
		return strings.Join(x, "")
	}

	// TODO: cannot use any packages
	orderSol := func(s string, t string) bool {
		s = order(s)
		t = order(t)

		return t == s
	}

	orderSol(s, t)

	// hashtable create one hash table & see if the matches
	hashTableSol := func(s string, t string) bool {
		sTable := map[rune]int{}
		for _, ch := range s {
			_, found := sTable[ch]
			if found {
				sTable[ch]++
				continue
			}
			sTable[ch] = 1
		}

		for _, ch := range t {
			val, found := sTable[ch]
			if !found {
				return false
			}
			sTable[ch]--
			if val < 0 {
				return false
			}

		}

		for _, ch := range s {
			if sTable[ch] != 0 {
				return false
			}

		}
		return true
	}

	return hashTableSol(s, t)

}

// 4. Two Sum
func twoSum(nums []int, target int) []int {
	// simple naive j == target - i
	// time = O(n^2)
	// space = O(n)
	for i, num := range nums {
		r := target - num
		// find if r is in nums && index != i
		for j, num2 := range nums {
			if i == j {
				continue
			}
			// within constraints will always be hit
			if r == num2 {
				if j < i {
					return []int{j, i}
				}
				return []int{i, j}
			}
		}

	}
	return []int{}

}

// 5. Longest Common Prefix
func longestCommonPrefix(strs []string) string {
	// pointer at each str
	// only increment when i for all strs is the same
	// if so next char
	// else return
	if len(strs) == 1 {
		return strs[0]
	}
	findMinWordLen := func(strs []string) int {
		min := len(strs[0])

		for _, str := range strs {
			if min > len(str) {
				min = len(str)
			}
		}
		return min
	}

	minWordLen := findMinWordLen(strs)
	ans := ""
	strsLen := len(strs) - 1

	for i := range minWordLen {

		for j := range strsLen {
			wordA := strs[j]
			wordB := strs[j+1]
			fmt.Printf("wordA = %s\nwordB = %s\n", wordA, wordB)
			fmt.Printf("chars are %s && %s \n", string(wordA[i]), string(wordB[i]))
			if wordA[i] != wordB[i] {
				return ans
			}
			if j == strsLen-1 {
				ans = fmt.Sprint(ans, string(wordA[i]))
			}
		}
	}
	return string(ans)
}

// 6. Group Anagrams
func groupAnagrams( /* TODO */ ) /* TODO */ {
	// TODO

}

// 7. Remove Element
func removeElement( /* TODO */ ) /* TODO */ {
	// TODO

}

// 8. Majority Element
func majorityElement( /* TODO */ ) /* TODO */ {
	// TODO

}

// 9. Design Hashset
// TODO: class design problem

// 10. Design Hashmap
// TODO: class design problem

// 11. Sort An Array
func sortAnArray( /* TODO */ ) /* TODO */ {
	// TODO

}

// 12. Sort Colors
func sortColors( /* TODO */ ) /* TODO */ {
	// TODO

}

// 13. Top K Frequent Elements
func topKFrequentElements( /* TODO */ ) /* TODO */ {
	// TODO

}

// 14. Encode And Decode Strings
// TODO: class design problem

// 15. Range Sum Query 2d Immutable
// TODO: class design problem

// 16. Product Of Array Except Self
func productOfArrayExceptSelf( /* TODO */ ) /* TODO */ {
	// TODO

}

// 17. Valid Sudoku
func validSudoku( /* TODO */ ) /* TODO */ {
	// TODO

}

// 18. Longest Consecutive Sequence
func longestConsecutiveSequence( /* TODO */ ) /* TODO */ {
	// TODO

}

// 19. Best Time To Buy And Sell Stock Ii
func bestTimeToBuyAndSellStockIi( /* TODO */ ) /* TODO */ {
	// TODO

}

// 20. Majority Element Ii
func majorityElementIi( /* TODO */ ) /* TODO */ {
	// TODO

}

// 21. Subarray Sum Equals K
func subarraySumEqualsK( /* TODO */ ) /* TODO */ {
	// TODO

}

// 22. First Missing Positive
func firstMissingPositive( /* TODO */ ) /* TODO */ {
	// TODO

}

func main() {
	//fmt.Println("Uncomment ONE case below to run a problem")
	// switch os.Args[1] { /* or just uncomment one call */
	// fmt.Println(concatenationOfArray([]int{1,2,1}))
	// fmt.Println(containsDuplicate([]int{1,2,3,1}))
	//	fmt.Println(isAnagram("anagram", "nagaram"))
	//fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	//[]string{"flower", "flow", "flight", "fl"}
	fmt.Println(longestCommonPrefix([]string{"onlyOne"}))
	// fmt.Println(groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
	// fmt.Println(removeElement([]int{3,2,2,3}, 3))
	// fmt.Println(majorityElement([]int{3,2,3}))
	// 9. Design Hashset (class design - see problem description)
	// 10. Design Hashmap (class design - see problem description)
	// fmt.Println(sortAnArray([]int{5,2,3,1}))
	// fmt.Println(sortColors([]int{2,0,2,1,1,0}))
	// fmt.Println(topKFrequentElements([]int{1,1,1,2,2,3}, 2))
	// 14. Encode And Decode Strings (class design - see problem description)
	// 15. Range Sum Query 2d Immutable (class design - see problem description)
	// fmt.Println(productOfArrayExceptSelf([]int{1,2,3,4}))
	// fmt.Println(validSudoku([]string{"5", "3", ".", ".", "7", ".", ".", ".", ".", "6", ".", ".", "1", "9", "5", ".", ".", ".", ".", "9", "8", ".", ".", ".", ".", "6", ".", "8", ".", ".", ".", "6", ".", ".", ".", "3", "4", ".", ".", "8", ".", "3", ".", ".", "1", "7", ".", ".", ".", "2", ".", ".", ".", "6", ".", "6", ".", ".", ".", ".", "2", "8", ".", ".", ".", ".", "4", "1", "9", ".", ".", "5", ".", ".", ".", ".", "8", ".", ".", "7", "9"}))
	// fmt.Println(longestConsecutiveSequence([]int{100,4,200,1,3,2}))
	// fmt.Println(bestTimeToBuyAndSellStockIi([]int{7,1,5,3,6,4}))
	// fmt.Println(majorityElementIi([]int{3,2,3}))
	// fmt.Println(subarraySumEqualsK([]int{1,1,1}, 2))
	// fmt.Println(firstMissingPositive([]int{1,2,0}))
	// }
}
