class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #approach: sort the intervals by their start, then by their end.
        #Then: for every interval, check preceding interval. If overlapping, merge two intervals and modify list in place by replacing those two with one interval. Then move on to next sublist and repeat this process. 

        #we forgot to sort

        intervals = sorted(intervals, key = lambda x: x[0])

        def overlapping(interval1, interval2):
            #if left bound of interval 2 is <= right bound of interval 1, overlapping.

            if interval2[0]<=interval1[1]:
                return True
            else:
                return False

        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval2[1], interval1[1])]

        # for index, interval in enumerate(intervals[1:]):
        #     if overlapping(intervals[index], intervals[index-1]):
        #         intervals[index-1] = merge(intervals[index-1], intervals[index])
        #         intervals.pop(index)

        # return intervals


        #the issue is that we are mutating the list while looping through it. This is a bad idea. Let's make a new list and add merged to it and then check the last value in that list for the prev value.
        merged = [intervals[0]]

        for interval in intervals[1:]:
            #check if can be merged with prev value from merged list
            if overlapping(merged[-1], interval):
                merged[-1] = merge(merged[-1], interval)
            else:
                merged.append(interval)

        return merged

        