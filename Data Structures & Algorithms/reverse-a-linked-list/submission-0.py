# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pred = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = pred
            

            pred = curr
            curr = temp
            # pred = pred.next
            # curr = temp
            # temp = temp.next

        return pred