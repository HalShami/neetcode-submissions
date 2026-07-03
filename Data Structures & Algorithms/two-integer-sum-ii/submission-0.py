class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #if sorted or not sorted you can use the complement implementation:
        #store every num in a dictionary where key = num and value = index
        #loop over every num and check if the complement is in the dictionary. If it is, return the index of current num and complement
        #time complexity: O(n). Space: O(alot). Dictionary trades memory for space. Idk but it is not O(1). For this problem we are constrained to O(1)

        #Since it is a sorted list we can use two-pointers so that we don't use any additional space.
        #Naive implementaiton: nested for loop to look for complement O(n^2)
        #optimized implementation: 
        #   start left pointer and right pointers at both ends of list.
        #   If sum < target move left pointer up.
        #   If sum > target move right pointer down
        #   If sum == target return indices

        l = 0
        r = len(numbers)-1
        numSum = 0

        while l < r:
            numSum = numbers[l] + numbers[r]
            if numSum < target:
                l += 1
            if numSum > target:
                r -= 1
            if numSum == target:
                return [l+1, r+1]
