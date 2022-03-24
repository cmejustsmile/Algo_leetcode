# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pa = ans = ListNode()
        p1 = list1
        p2 = list2
        
        while p1 != None or p2 != None:
            if p1 == None:
                pa.next = p2
                break
            elif p2 == None:
                pa.next = p1
                break
            else:
                if p1.val < p2.val:
                    pa.next = p1
                    while p1.next != None and p1.next.val < p2.val:
                        p1 = p1.next
                    pa = p1
                    p1 = p1.next
                else:
                    pa.next = p2
                    while p2.next != None and p2.next.val <= p1.val:
                        p2 = p2.next
                    pa = p2
                    p2 = p2.next
            
        return ans.next