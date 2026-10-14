class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1=l1
        c2=l2
        s=c=0
        r=ListNode()
        c3=r
        while c1 or c2 or c:
            #print("st",c1.val,c2.val)
            n1=c1.val if c1 else 0
            n2=c2.val if c2 else 0
            s=n1 + n2
            t=(s+c)
            n=t%10
            c3.next=ListNode(n)
            c=t//10
            c1=c1.next if c1 else None
            c2=c2.next if c2 else None
            c3=c3.next
            #print("ed",c1.val,c2.val)
        return r.next