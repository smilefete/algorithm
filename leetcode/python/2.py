#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
'''
Q
新建另外的对象是为了保持参数的原始性，有没有这个必要？
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        ll=result
        carry=0
        ll1=l1
        ll2=l2
        while ll1 is not None and ll2 is not None:
            ll.next=ListNode(ll1.val+ll2.val+carry)
            ll=ll.next
            carry=ll.val/10
            ll.val%=10
            ll1=ll1.next
            ll2=ll2.next
        ll3=ll1 if ll1 is not None else ll2
        while ll3 is not None:
            ll.next=ListNode(ll3.val+carry)
            ll=ll.next
            carry=ll.val/10
            ll.val%=10
            ll3=ll3.next
        if carry==1:
            ll.next=ListNode(1)
        return result.next


