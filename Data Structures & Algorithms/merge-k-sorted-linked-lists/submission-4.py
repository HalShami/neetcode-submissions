# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #I don't get how linkedlists have anything to do with this. But what if we just insert all numbers from all lists into a PQ and then pop them all and put them in a return list

        #edge case 1: no linkedlists in lists.

        #edge case 2: empty linkedlists. 

        #solution for both: return empty ListNode

        if not lists:
            return None

        #check if all ListNodes are empty
        counter = 0
        for listnode in lists:
            if listnode==None:
                counter += 1
        if counter == len(lists):
            return None
        PQ = []
        for sublist in lists:
            curr = sublist
            while curr != None:
                heapq.heappush(PQ, curr.val)
                curr = curr.next

        
        retList = ListNode(heapq.heappop(PQ), None)
        curr = retList
        for i in range(len(PQ)):
            curr.next = ListNode(heapq.heappop(PQ), None)
            curr = curr.next

        return retList
            

        #ohhh I finally get it I'm a dumb ahh. They are not arrays, they are linkedlist nodes. I should learn how to work with linkedlists in python and come back. Or just yolo this and be done with linkedlists?
