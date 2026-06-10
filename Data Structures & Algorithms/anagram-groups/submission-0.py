class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for word in list:
        #   if sorted_word not in dictionary.keys():
        #       dictionary[sorted_word] = [word]
        #   else:
        #       dictionary[sorted_word].append(word)

        #ret_list = []
        #for group in dictionary.keys():
        #    ret_list.append(group)

        dictionary = {}
        def sort_func(word):
            return "".join(sorted(word))

        for word in strs:
            if sort_func(word) not in dictionary.keys():
                dictionary[sort_func(word)] = [word]
            else:
                dictionary[sort_func(word)].append(word)
        ret_list = []
        
        for group in dictionary.keys():
            ret_list.append(dictionary[group])

        return ret_list