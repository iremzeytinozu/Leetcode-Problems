class Solution(object):
    def findKthLargest(self, nums, k):
        nums = [-num for num in nums]
        count = 0

        heapq.heapify(nums)

        while len(nums) >= 1:
            popped = heapq.heappop(nums)
            count += 1
             
            if k == count:
                return popped * -1