class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort()
        n, heap = len(intervals), []
        
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                heapq.heapreplace(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        return len(heap)
            
        
    
        
        