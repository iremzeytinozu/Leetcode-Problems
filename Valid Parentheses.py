class Solution(object):
    def isValid(self, s):
        
        close_map = {"(" : ")",
                     "{" : "}",
                     "[" : "]"
                    }
        opens = []

        for symbol in s:

            if symbol in close_map.keys():
                opens.append(symbol)
            
            elif opens == [] or symbol != close_map[opens.pop()]:
                return False

        return opens == [] 