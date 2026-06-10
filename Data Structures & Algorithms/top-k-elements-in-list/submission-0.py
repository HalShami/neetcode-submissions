class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #keep counter for each unique value in the array through a dictionary. Then loop through the keys in the dictionary and check the value of each key (unique_num). Return the keys with the three highest values

        count_dict = {}

        for num in nums:
            if num in count_dict.keys():
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        print(count_dict)
        pair_list = []
        for value in count_dict.keys():
            pair_list.append([value, count_dict[value]])
        pair_list.sort(key = lambda pair_list: pair_list[1])
        
        ret_list = []
        
        for i in range(k):
            ret_list.append(pair_list.pop()[0])
        return ret_list