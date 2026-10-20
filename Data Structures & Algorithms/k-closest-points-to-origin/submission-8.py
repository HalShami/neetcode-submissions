import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #goal: return k points with smallest distance to origin. 

        #implementation: build min-PQ using distance of points as weight. 

        def distance(point):
            return ((point[0]**2)+(point[1]**2))

        PQ = []

        for point in points:
            heapq.heappush(PQ, (distance(point), point))
        
        retList = []
        for i in range(k):
            retList.append(heapq.heappop(PQ)[1])

        return retList
