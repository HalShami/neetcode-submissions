class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Two Sum Approach:
        #1. Sort
        #2. For every value:
        #       l = value_index+1
        #       r = last_value
        #       if nums[l] + nums[r] + value > 0:
        #           r -= 1
        #       elif nums[l] + nums[r] + value < 1:
        #           l += 1
        #       elif nums[l] + nums[r] + value == 0:
        #           tempList = sorted([nums[1], nums[r], value])
        #           numsSet.add(tuple(x) for x in tempList)
        #3. finalList = [(list(x) for x in numsSet)]


        nums.sort()
        numsSet = set()
        for index, value in enumerate(nums):
            l = index+1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] + value > 0:
                    r -= 1
                elif nums[l] + nums[r] + value < 0:
                    l += 1
                elif (nums[l] + nums[r] + value) == 0:
                    tempList = sorted([nums[l], nums[r], value])
                    numsSet.add(tuple(tempList))
                    r -= 1
        finalList = [list(x) for x in numsSet]
        return finalList

