class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return: indices of 2 elements in list nums that add to target. 
        #two indices cannot be the same index. return as list

        #approaches:
        # - for every element iterate through every element and check if the sums == target. If they do, return indices in list. Time complexity: O(n^2)
        # - can't think of more efficient approach


        for index, element in enumerate(nums):
            for index2, element2 in enumerate(nums):
                if index2 != index:
                    if (element + element2) == target:
                        output = [index2, index]
        return output