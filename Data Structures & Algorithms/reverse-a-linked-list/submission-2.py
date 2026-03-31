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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        # since we're reversing the LL, we want the first predecessor to point to None
        pred = None
        
        # the current node will then be the first node so that we can iterate through it
        curr = head
        
        while curr:
            # temporary node is the next so that we dont lose the chain between them
            temp = curr.next
            # set the current next pointer BACKWARDS!
            curr.next = pred

            # now progress the pointers:
            # set pred now equal to the node ahead of it
            pred = curr
            # and then set curr equal to the node ahead of it 
            curr = temp
            # pred = pred.next
            # curr = temp
            # temp = temp.next

        return pred
        '''