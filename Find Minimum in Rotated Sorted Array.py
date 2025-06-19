class Solution(object):
    def findMin(self, nums):
        result = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            medium = (left + right) // 2
            result = min(result, nums[medium])

            if nums[medium] >= nums[left]:
                left = medium + 1

            else:
                right = medium - 1

        return result