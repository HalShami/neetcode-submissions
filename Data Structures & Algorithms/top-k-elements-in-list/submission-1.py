class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make dict with unique value as key and no. of occurences as value
        #put every key, value pair in a list & sort based on the value
        #pop k values and add to new list
        dictionary = {}
        for value in nums:
            if value in dictionary.keys():
                dictionary[value] += 1
            else:
                dictionary[value] = 1

        values_list = []
        for value in dictionary.keys():
            values_list.append([value, dictionary[value]])
        
        values_list.sort(key = lambda values_list: values_list[1])

        ret_list = []
        for i in range(k):
            ret_list.append(values_list.pop()[0])
        return ret_list