class Solution(object):
    def shuffle(self, nums, n):
        shuffleArray = [0] * (2 * n)  

        for i in range(n):
            shuffleArray[2 * i] = nums[i]       
            shuffleArray[2 * i + 1] = nums[n + i]  

        return shuffleArray