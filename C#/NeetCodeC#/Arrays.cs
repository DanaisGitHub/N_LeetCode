using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Runtime.ExceptionServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace NeetCodeC_ {
    class Arrays {
        public static bool hasDuplicate(int[] nums) {
            // A Few ways to solve 1:
            // has maps, if it exsits // greater than 2 return false else return true
            Dictionary<int, int> dictMap = new Dictionary<int, int>();
            foreach (int num in nums) {
                if (dictMap.ContainsKey(num)) return true;
                dictMap.Add(num, 1);
            }
            return false;
            // time complexity  = O(n) n=len
            // space = O(n)

        }
        public static bool IsAnagram(string s, string t) {
            //sort both strings and see if there equal
            //if (s.Length != t.Length) {
            //    return false;
            //}
            //char[] sChar = s.ToCharArray();
            //char[] tChar = t.ToCharArray();
            //Array.Sort(sChar);
            //Array.Sort(tChar);
            //int i = 0;
            //for (i = 0; i < sChar.Length; i++) {
            //    if (sChar[i] != tChar[i]) {
            //        return false;
            //    }
            //}
            //return true;


            // Make hashset and see if it's equal
            // union  contains every element
            // intersetction contains
            // 
            if (s.Length != t.Length) {
                return false;
            }

            Dictionary<char, int> sDictMap = new Dictionary<char, int>();
            Dictionary<char, int> tDictMap = new Dictionary<char, int>();

            int i;

            for (i = 0; i < s.Length; i++) {
                sDictMap[s[i]] = sDictMap.GetValueOrDefault(s[i], 0) + 1;
                tDictMap[t[i]] = tDictMap.GetValueOrDefault(s[i], 0) + 1;

            }

            bool count = sDictMap.Count == tDictMap.Count;
            bool sLeftOvers = sDictMap.Except(tDictMap).Any();// A not B, any = any existy 


            return count && sLeftOvers;




            // THERE ANOTHER SOLUTION USING THE ALPHABET

        }

        public static int[] twoSum(int[] nums, int target) {
            // turn nums into dict and do target - num == 
            // may be more than 1 nums in nums
            Dictionary<int, int> dictMap = new();
            int i;
            foreach (int num in nums) {
                dictMap[num] = dictMap.GetValueOrDefault(num, 0) + 1;


            }

            foreach (int num in nums) {
                dictMap[num]--;

                if (dictMap.ContainsKey(target - num) && dictMap[target - num] - 1 > 0) {
                    return (target - num) > num ? new int[] { num, target - num } : new int[] { target - num, num };
                }
                dictMap[num]++;
            }
            return [];

        }

        public static List<List<string>> GroupAnagrams(string[] strs) {
            Console.WriteLine($" ----------- FUNCTION START  ----------- ");
            List<List<string>> res = new();
            Dictionary<string, List<string>> dictMap = new();


            foreach (string str in strs) {
                int[] alpha = new int[26]; // all values = 0


                foreach (char s in str) {
                    alpha[s - 'a']++;
                }

                string strAlpha = string.Join(",", alpha); // when you join as string 10 and 01 look the same
                if (!dictMap.ContainsKey(strAlpha)) {
                    dictMap.Add(strAlpha, new List<string>());
                }
                Console.WriteLine(strAlpha);
                dictMap[strAlpha].Add(str);

            }

            foreach (KeyValuePair<string, List<string>> anagrams in dictMap) {
                Console.WriteLine($"[{anagrams}] = {string.Join(",", anagrams.Value)}");
            }



            foreach (KeyValuePair<string, List<string>> anagrams in dictMap) {

                res.Add(anagrams.Value);
            }
            Console.WriteLine($" ----------- FUNCTION END  ----------- ");

            return res;

        }

        public static string Encode(IList<string> strs) {
            string res = "";

            foreach ( string s in strs) {
                int num = s.Length;
                res += $"{num}#{s}";
            }

            return res;
        } 

        public static List<string> Decode(string s) {
            if (s == "") {
                return new List<string>();
            }
            List<string> res = new List<string>();

            int i=0;
            int endNum = i;
            do {
                endNum = i;
                while (s[endNum] !='#') {
                    endNum++;
                    
                }
                int nextWordLength = int.Parse(s.Substring(i,endNum - i));
                int end = nextWordLength;
               
                Console.WriteLine(s.Substring(endNum+1, end));
                
                res.Add(s.Substring(endNum+1 , end));
                i += nextWordLength + (endNum - i)+1;
            } while (i < s.Length);

            return res;
        } 

        public static int[] ProductExceptSelf(int[] nums) {
            // pre/post fix sums
            //[1, 2, 8, 48]
            //[48,48,24,6]

            //[48,24,12,8]

            // prefix product

            int[] prefix = new int[nums.Length];
            int[] postfix = new int[nums.Length];
            int[] res = new int[nums.Length];

            int i;
            prefix[0] = 1;
            for (i=1; i < nums.Length; i++) {
                prefix[i] = nums[i-1] * prefix[i - 1];
            }
            postfix[nums.Length - 1] = 1;
            for (i = nums.Length-2; i >= 0; i--) {
                postfix[i] = nums[i+1] * postfix[i + 1];
            }

            for (i = 0; i < nums.Length; i++) {
                res[i] = prefix[i] * postfix[i];
            }

            // product of everything / divide itself
            return res;

        } //TODO:

        public static bool IsValidSudoku(char[][] board) {

            // checking each row!

            const int ROWS = 9;
            const int COLS = 9;
            HashSet<char> hashSet;

            int i ,j,endX,endY;
            for (i = 0; i < COLS; i++) { // Checking each row
                hashSet = new();
                for (j = 0; j < ROWS; j++) {
                    if (board[j][i] == '.'){
                        continue;
                    }
                    if (hashSet.Contains(board[j][i])){
                        return false;
                    }
                    hashSet.Add(board[j][i]);
                }
            }

            for (j = 0; j < ROWS; j++) { // Checking each COLS
                hashSet = new();
                for (i = 0; i < COLS; i++) {
                    if (board[j][i] == '.') {
                        continue;
                    }
                    if (hashSet.Contains(board[j][i])) {
                        return false;
                    }
                    hashSet.Add(board[j][i]);
                }
            }

            // now we need to check each square
            // 0-2 , 3-5 , 6-8
            //endX = 3;
            //endY = 3;
            //int startX=0, startY=0;
            //do {
            //    i++
            //    do{
            //        hashSet = new();
            //        if (board[i][j] == '.') {
            //            continue;
            //        }
            //        if (hashSet.Contains(board[i][j])) {
            //            return false;
            //        }
            //        hashSet.Add(board[i][j]);
            //    }

            //    startY += 3;
            //    endY += 3;
            //    startX += 3;
            //    endX += 3;
            //} while (endY < 9);

            return true;

           

        }
    }
}


