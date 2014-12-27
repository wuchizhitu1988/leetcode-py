# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        curA, curB = headA, headB

        while curA != curB:
            curA = curA.next
            curB = curB.next
            
            if curA is None and curB is None:
                return None
            
            if curA is None:
                curA = headB
            
            if curB is None:
                curB = headA
            
        return curA
            
        
        
