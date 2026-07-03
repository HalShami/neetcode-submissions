class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort the characters
        #place in set
        #check if sorted string is in dict

        StringSet = set()
        StringSet.add("".join(sorted(s)))
        if ("".join(sorted(t))) in StringSet:
            return True
        else:
            return False
        
