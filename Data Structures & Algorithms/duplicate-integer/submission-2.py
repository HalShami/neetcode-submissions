class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            #approaches: 
            #iterate through each element of the array. For each element, iterate through all elements and check if another instance exists. TIme Complexity: O(n^2)
            #sort the elements and iterate through the sorted array while keeping last item in memory. If last_item == item return false. Time Complexity: O(n)
            #sort then convert to a set and check if the two are equal after typecasting set to list. Time complexity: O(n) at best

            #decided approach: no 2. 

            nums.sort()
            
            temp = 99999999999
            for num in nums:
                if num == temp: return True
                temp = num
            return False