class Solution:
    def solveNQueens(self, n):
        self.res = 0
        self.extend(n, perm=[])
        return self.res

    def can_be_extended_to_solution(self, perm):
        i = len(perm) - 1
        for j in range(i):
            if i - j == abs(perm[i] - perm[j]):
                return False
        return True

    def extend(self, n, perm):

        if len(perm) == n:
            for r in range(len(perm)):
                self.res += 1/n

        for k in range(n):
            if k not in perm:
                perm.append(k)
                if self.can_be_extended_to_solution(perm):
                    self.extend(n, perm)
                perm.pop()


x = Solution()
p = x.solveNQueens(8)
print(round(p))
