class Solution(object):
    def climbStairs(self, n):

        def climb(n):
            if n <= 1:
                return 1

            climb = [1, 1]

            i = 2

            while i <= n:
                tmp = climb[1]
                climb[1] = climb[0] + climb[1]
                climb[0] = tmp
                i += 1

            return climb[1]

        return climb(n)
