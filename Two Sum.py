class Solution(object):
    def twoSum(self, nums, target):

        hashMap = {} # num : index
        
        for index, num in enumerate(nums):
            diff = target - num

            if diff in hashMap:
                return [hashMap[diff], index]

            hashMap[num] = index

        return