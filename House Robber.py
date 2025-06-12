class Solution(object):
    def rob(self, nums):
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2