"Сложность О(1)"
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q, n  = [root],[]
        t = [root.val]
        while (q):
            out = q.pop(0)
            if out.left:
                n.append(out.left)
            if out.right:
                n.append(out.right)
            if q == [] and n:
                s = 0
                for i in n:
                    s += i.val
                t.append(s/len(n))
                q, n = n, q
        return t