# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = ptr2 = head
        index = -1

        while ptr2!=None:
            
            ptr1 = ptr1.next
            if ptr1==None:
                return False
            if ptr2.next==None:
                return False
            ptr2 = ptr2.next.next
           
            
            
           
            
            if(ptr1 == ptr2):     
                return True
        return False
        
            