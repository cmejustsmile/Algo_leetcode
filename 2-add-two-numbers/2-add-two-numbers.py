# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        carry = 0
        p1 = l1
        p2 = l2
        sflag = True
        
        while p1 != None or p2 != None:
            if p1 == None :
                sum = p2.val + carry
            elif p2 == None :
                sum = p1.val + carry
            else:
                sum = p1.val + p2.val + carry

            if sum >= 10:
                carry = 1
                sum -= 10
            else:
                carry = 0
            
            if sflag == True:
                sflag = False
                ans = pres = ListNode(0, None)
            else:
                pres = ListNode(0, None)
                prev.next = pres
           
            pres.val = sum
            prev = pres

            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next


        # carry 가 남는 경우
        if carry == 1:
            pres = ListNode(0, None)
            prev.next = pres
            pres.val = 1
        else:
            p = None

        return ans