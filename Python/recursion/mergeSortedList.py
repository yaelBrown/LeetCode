# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1: return l2
        if not l2: return l1

        def _merge(l1, l2):
          if 

        if l1.val < l2.val: 
          l1.next = _merge(l1.next, l2)
          return l1
        else: 
          l2.next = _merge(l2.next, l1)
            



      