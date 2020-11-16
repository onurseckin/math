class Solution:
    def solveNQueens(self, n):
        self.res = []
        self.extend(n, perm=[])
        return self.res

    def can_be_extended_to_solution(self, perm):
        i = len(perm) - 1
        for j in range(i):
            if i - j == abs(perm[i] - perm[j]):
                return False
        return True

    def extend(self, n, perm):
        s = '.' * (n-1)
        solution = []*n
        if len(perm) == n:
            for r in range(len(perm)):
                location = perm[r]
                resStr = s[:location] + "Q" + s[location:]
                solution.append(resStr)
            self.res.append(solution)
            solution = []*n

        for k in range(n):
            if k not in perm:
                perm.append(k)
                if self.can_be_extended_to_solution(perm):
                    self.extend(n, perm)
                perm.pop()


x = Solution()
p = x.solveNQueens(4)
print(p)
