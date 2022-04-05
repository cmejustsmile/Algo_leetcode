# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        pp = head
        cnt = 0 # total counts of the list
        while pp != None:
            cnt = cnt+1
            pp = pp.next
        
        N = cnt - n # index from the start
        pp = head
        prev = None
        idx = 0
        
        while pp != None:
            if idx == N:
                if prev == None:
                    head = pp.next
                else:
                    prev.next = pp.next
                return head
            prev = pp
            pp = pp.next
            idx=idx+1
        
        return head
        