# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        predecessor = None
        
        while curr:
            temp = curr.next
            curr.next = predecessor
            predecessor = curr
            curr = temp

        return predecessor