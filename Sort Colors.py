class Solution(object):
    def sortColors(self, nums):
        
        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1

        i = 0

        for n in range(len(counts)):
            for j in (range(counts[n])):
                nums[i] = n
                i += 1

        return nums