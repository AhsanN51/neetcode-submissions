# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        k=0
        while cur:
            cur=cur.next
            k+=1
        d=k-n+1
        cur=head
       # print(d,n)
        if d==1:
            if cur.next == None:
               # print("treg")
                return None
            else:
                head=head.next
               # print("treg2")
                return head
        elif d==k:
           # print("last")
            while cur.next.next != None:
                cur=cur.next
            cur.next=None
            return head
        else:
            for i in range(d-2):
                cur=cur.next
            cur.next=cur.next.next
            return head