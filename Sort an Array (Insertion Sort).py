class Solution(object):
    def sortArray(self, nums):

        for i in range(1, len(nums)):
            j = i - 1

            while j >= 0 and nums[j + 1] < nums[j]:        
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp
                j -= 1

        return nums