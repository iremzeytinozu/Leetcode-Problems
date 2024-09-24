class Solution(object):
    def isPalindrome(self, x):
        
        if x < 0:
            return False

        if x == 0:
            return True

        originalX = x
        reversedNum = 0

        while x > 0:

            lastDigit = x % 10
            reversedNum = reversedNum * 10 + lastDigit
            x = x // 10

        return reversedNum == originalX