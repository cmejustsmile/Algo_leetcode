# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = list1
        p2 = list2
        p3 = ans = ListNode(0)

        while p1 != None or p2 != None :
            if p1 == None :
                p3.next = ListNode(p2.val)
                p2 = p2.next
            elif p2 == None : 
                p3.next = ListNode(p1.val)
                p1 = p1.next
            else :
                if p1.val < p2.val :
                    p3.next = ListNode(p1.val)
                    p1 = p1.next 
                else :
                    p3.next = ListNode(p2.val)
                    p2 = p2.next

            p3 = p3.next

        return ans.next