class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #one loop:
        #If in hashset return false. If not in hashset, place. If loop ends return true

        hashset = set()
        for value in nums:
            if value in hashset:
                return True
            else:
                hashset.add(value)
        return False