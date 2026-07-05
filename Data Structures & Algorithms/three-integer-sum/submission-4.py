class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #implementation: need to convert this into a two sum problem for each number. 

        #two sum implementation we are going for: two pointer. Pre-requisite: sorted list.
        #approach: 
        #1. sort list
        #2. for each number, use two-pointer implementation to find the two numbers that add to current number to sum to zero, if they exist. If they do, sort the numbers and add to set.
        #If they don't, move on to next number.
        #3. take sorted set of tuples and convert into a list. Return the list

        nums.sort()
        numsSet = set()
        for index, value in enumerate(nums):
            l = index + 1
            r = len(nums) - 1
            while l < r:
                if value + nums[l] + nums[r] > 0:
                    r -= 1
                elif value + nums[l] + nums[r] < 0:
                    l += 1
                elif value + nums[l] + nums[r] == 0:
                    temp_list = [value, nums[l], nums[r]]
                    temp_list.sort()
                    numsSet.add(tuple(temp_list))
                    l += 1
                    r -= 1
        retList = [list(x) for x in numsSet]
        return retList
