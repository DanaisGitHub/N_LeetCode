class Recursion_With_String:
    def reverseAString(self, string: str) -> str:
        # eg given hello you return olleh
        # you would take then substring of the strnigs until you reach ""
        #

        if string == "" or not string:
            return ""

        return self.reverseAString(string[1:]) + string[0]

    def isPalindrome(self, string: str) -> bool:
        # how to recursivly see if something is Palindromic

        # see if the first and last values equal, if so

        if len(string) <= 1:
            return True

        # at this point the only base case = true so we either trigger base case or don't
        if string[0] == string[-1]:
            boolean: bool = self.isPalindrome(string[1:-1:1])
            return boolean  # returns

        return False

    def decimalToBinary(self, decimal: int, binary: str) -> str:
        if decimal == 0:
            return binary  # when you solved the whole hing return binary
        binary = f"{decimal % 2}{binary}"
        return self.decimalToBinary(decimal//2, binary)

    def sumOfNaturalNumbers(self, num: int) -> int:
        if num == 0:
            return num

        return num + self.sumOfNaturalNumbers(num - 1)


class DivideAndConquer:
    def binarySearch(self, nums: list[int], target: int) -> bool:
        def realSearch(l: int, r: int) -> bool:  # r is now EXCLUSIVE
            if l >= r:
                return False
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                return realSearch(mid + 1, r)
            else:
                return realSearch(l, mid)
        
        return realSearch(0, len(nums))  # Proper exclusive bound
    
    def fib(self,num:int)->int:
        if num == 0:
            return 0
        if num == 1:
            return 1
        
        return self.fib(num-1) + self.fib(num-2)
    
    
    
# class LinkedList:
#     def reverseALinkedList(self,head)
    
    # -> ->
    # prev,node
    # temp = node.next
    # node.next = prev
    
    













solver = DivideAndConquer()
result = solver.fib(10)
print(result)
