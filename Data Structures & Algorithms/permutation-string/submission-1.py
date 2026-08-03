class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Goal: Identify if there is a contiguous permutation of s1 in s2

        #logic:
        # slidiingWindowLength = len(s1)
        #   check each possible window of length len(s1) in s2 for permutations

        # permutation checking logic:
        #   sort characters and check if they match after sorting both

        slidingWindowLength = len(s1)

        for index in range(len(s2)-slidingWindowLength+1):
            if self.checkPermutation(s2[index:(index+slidingWindowLength)], s1):
                return True
        return False
    
    def checkPermutation(self, s2_substring, s1):
        sorted_s2 = "".join(sorted(s2_substring))
        sorted_s1 = "".join(sorted(s1))

        if sorted_s2 == sorted_s1:
            return True
        else:
            return False

            
