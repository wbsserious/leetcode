# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def findnumber(head):
            i=0
            while head:
                i+=1
                head=head.next
            # print (i)
            return i
        number=findnumber(head)
        dummy=ListNode(0,head)
        cur=dummy
        # print dummy.next
        for i in range(1,number-n+1):
            # print("11111111111111111111")
            cur=cur.next
            # print(cur)
            # print dummy.next
        # print("22222222222222222222")
        cur.next=cur.next.next
        # print dummy.next
        return dummy.next