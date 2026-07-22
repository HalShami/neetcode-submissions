class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #goal: find length of longest substring without duplicate characters

        #implementation:
        #   1. initialize left and right pointers of window of continuous characters
        #   2. move right pointer as long as no duplicates. 
        #       If character is a duplicate, record length of substring and set left pointer to position of right pointer

        #Invariant: while r < len(s)

        l = 0
        r = 1
        max_length = 0
        if not s:
            return 0
        if len(s) == 1:
            return 1
        while r < len(s):
            if self.checkWindowForDuplicates(l, r, s):
                r += 1
                max_length = max((r-l), max_length)
            else:
                max_length = max((r - l), max_length)
                l += 1
                r = l + 1
        return max_length

            

    def checkWindowForDuplicates(self, l, r, s):
        seenChars = set()
        for characterIndex in range(l, r+1):
            if s[characterIndex] not in seenChars:
                seenChars.add(s[characterIndex])
                continue
            else:
                return False
        return True
