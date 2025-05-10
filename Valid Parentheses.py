class Solution(object):
    def isValid(self, s):
        
        stack = []
        
        for character in s:
            if character in '([{':
                stack.append(character)
            elif character in ')]}':
                if not stack:
                    return False
                top = stack.pop()
                if character == ')' and top != '(':
                    return False
                if character == ']' and top != '[':
                    return False
                if character == '}' and top != '{':
                    return False

        # Eğer stack boşsa, tüm açılış parantezleri kapatılmış demek
        return not stack