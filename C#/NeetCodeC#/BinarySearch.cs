using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NeetCodeC_ {
    static class BinarySearch {

        public static int Search(int[] nums, int target) {
            // do a binary search
            int l, r, m;
            l = 0;
            r = nums.Length - 1;

            while (r >= l) {
                m = (l + r) / 2;
                if (target == nums[m]) return m;
                if (target > nums[m]) l = m + 1; // can't be m so step over m( you make the circle smaller 
                if (target < nums[m]) r = m - 1;
            }
            return -1;
        }

        public static bool SearchMatrix(int[][] matrix, int target) {
            // firstly you need to find which row it is in

            int ROWS, COLS, l, r, m, foundRow = -1, lRowValue, rRowValue;
            COLS = matrix[0].Length;
            ROWS = matrix.Length;
            l = 0;
            r = ROWS - 1;

            while (l <= r) {
                m = (l + r) / 2;
                lRowValue = matrix[m][0]; // don't think m ever goes to 0
                rRowValue = matrix[m][COLS - 1];

                if (target >= lRowValue && target <= rRowValue) { foundRow = m; break; }

                if (target > lRowValue && target > rRowValue) l = m + 1;

                if (target < lRowValue && target < rRowValue) r = m - 1;

            }

            if (foundRow == -1) return false;

            

            // Now just normal binary search with foundRow
            l = 0;
            r = COLS - 1;

            while (l <= r) {
                m = (l + r) / 2;

                if (target == matrix[foundRow][m]) return true;

                if (target > matrix[foundRow][m]) l = m + 1; // shorten the window//never null out

                if (target < matrix[foundRow][m]) r = m - 1;

            }

            return false;




        }
    }
}
