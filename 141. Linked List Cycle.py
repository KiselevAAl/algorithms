"Сложность O(log n)"
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        q1 = q2 = head
        while q2 and q2.next:
            q1 = q1.next
            q2 = q2.next.next
            if q1 == q2:
                return True

        return False