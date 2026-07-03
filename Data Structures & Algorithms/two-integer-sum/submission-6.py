class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #approach: 
        #1. Make a dictionary with every value (Key = num, value = index) - O(N)
        #2. For value in loop if complement (target - value) in dictionary.keys(): return [index, dict[value]]

        dictionary = {}

        for index, value in enumerate(nums):
            dictionary[value] = index
        for index, value in enumerate(nums):
            if ((target-value) in dictionary.keys()) and (index != dictionary[target-value]):
                return [index, dictionary[target-value]]