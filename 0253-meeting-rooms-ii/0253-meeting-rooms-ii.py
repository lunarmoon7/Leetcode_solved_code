class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Ascending Order
        intervals.sort()
        n, heap = len(intervals), []
        
        heapq.heappush(heap, intervals[0][1])
        
        for i in range(1, n):
            if heap[0] > intervals[i][0]:
                heapq.heappush(heap, intervals[i][1])
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i][1])
        return len(heap)
            
        
    
        
        