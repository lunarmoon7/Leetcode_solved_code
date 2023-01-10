# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        ret = ListNode()
        dummy = ret
        while head:
            heapq.heappush(heap, head.val)
            head = head.next
        
        while heap:
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next
        return ret.next
        