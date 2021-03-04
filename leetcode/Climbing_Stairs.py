class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            print(a,b)
            a, b = b, a + b
        return a