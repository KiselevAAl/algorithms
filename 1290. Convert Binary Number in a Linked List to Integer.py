"Сложность О(N)"
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        res = (0)
        while head:
            res = res * 2 + head.val
            head = head.next
        return res