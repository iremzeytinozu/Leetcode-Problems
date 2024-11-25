class Solution(object):
    def twoSum(self, numbers, target):
        
        dict = {}

        for i, number in enumerate(numbers): # enumerate: hem i hem number'ı alıyor
            diff = target - number 
            if diff in dict:
                return[dict[diff], i]

            dict[number] = i