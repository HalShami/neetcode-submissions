class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # merge sort
        # def merge(array1, array2):
        #     array3 = []
        #     while len(array1) > 0 and len(array2) > 0:
        #         if array1[0] > array2[0]:
        #             array3.append(array2[0])
        #             array2.pop(0)
        #         else:
        #             array3.append(array1[0])
        #             array3.pop(0)
        #     while len(array1) > 0:
        #         array3.append(array1[0])
        #         array1.pop(0)
        #     while len(array2) > 0:
        #         array3.append(array2[0])
        #         array2.pop(0)
        #     return array3

        # def mergeSort(array):
        #     if len(array) == 1:
        #         return false
            
        #     midArray = int(len(array)/2)
        #     array1 = array[:midArray]
        #     array2 = array[midArray:]

        #     return merge(array1, array2)
        
        # mergeSort(nums)

        # once the array is sorted, set x to 999999 then: loop through every 
        # value in the array, check if value = x. (If true, return true) 
        # (if false, continue), then set x to value, loop again. Once the 
        #loop ends, return False.

        x = 9999999

        for value in sorted(nums):
            if value == x:
                return True
            else:
                x = value
        return False
        
