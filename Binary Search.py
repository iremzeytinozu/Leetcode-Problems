class Solution(object):
    def search(self, nums, target):

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target > nums[mid]:
                low = mid + 1

            elif target < nums[mid]:
                high = mid - 1

            else:
                return mid

        return -1