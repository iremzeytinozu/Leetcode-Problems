class Solution(object):
    def singleNumber(self, nums):
        
        single_number = []

        for num in nums:
            if num not in single_number:
                single_number.append(num)
            else:
                single_number.remove(num)

        return single_number.pop()
        