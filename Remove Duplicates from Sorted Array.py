class Solution(object):
    def removeDuplicates(self, nums):

        if not nums:
            return 0

        k = 0

        for index in range(1, len(nums)):
            if nums[index] != nums[k]:
                k += 1
                nums[k] = nums[index]
            else:
                continue

        return k + 1
