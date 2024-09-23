class Solution(object):
    def twoSum(self, numbers, target):
        
        dict = {}

        for i, number in enumerate(numbers): # enumerate: hem i hem number'ı alıyor

            if target - number in dict:
                return([dict[target - number], i])
            
            elif number not in dict:
                dict[number] = i