class Solution:
    def isPalindrome(self, s: str) -> bool:
        #approach: 
        #1. strip all non-alphanumeric characters
        #2. use two-pointer to check if character on left == right while left index < r

        cleaned = ("".join(char for char in s if char.isalnum())).lower()
        l = 0
        r = len(cleaned)-1

        while l < r:
            print(cleaned[l])
            print(cleaned[r])
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        return True
