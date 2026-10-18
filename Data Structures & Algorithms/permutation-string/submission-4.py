class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) == 0 and len(s1) == 0:
            return true

        #try different windows of len(s1). Check if that window is permutation of s1, if is permutation, return true

        def isPermutation(str1, str2):
            freqCount = {}
            for char in str1:
                if char in freqCount.keys():
                    freqCount[char] += 1
                else:
                    freqCount[char] = 1
            
            freqCount2 = {}
            for char in str2:
                if char in freqCount2.keys():
                    freqCount2[char] += 1
                else:
                    freqCount2[char] = 1
            
            print(freqCount)
            print(freqCount2)

            if freqCount == freqCount2:
                
                return True
            return False

            
        windowLen = len(s1)

        l = 0
        r = windowLen

        
        for i in range(len(s2)-(windowLen-1)):
            #check if permutation
            IsPermutation = isPermutation(s1, s2[l:r])
            if IsPermutation:
                return True
            #increment
            l += 1
            r += 1
        return False