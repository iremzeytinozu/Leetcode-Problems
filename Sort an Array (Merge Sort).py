class Solution(object):
    def sortArray(self, nums):
        def mergeSort(nums, start, end):

            if start >= end:
                return nums

            mid = (end + start) // 2

            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid , end)

            return nums

        def merge(nums, start, mid, end):
            left = nums[start: mid + 1]
            right = nums[mid + 1: end + 1]

            y = 0
            z = 0
            index = start

            while y < len(left) and z < len(right):

                if left[y] < right[z]:
                    nums[index] = left[y]
                    y += 1

                else:
                    nums[index] = right[z]
                    z += 1

                index += 1

            while y < len(left):
                nums[index] = left[y]
                y += 1
                index += 1

            while z < len(right):
                nums[index] = right[z]
                z += 1
                index += 1

        mergeSort(nums, 0, len(nums) - 1)   
        return nums 

        