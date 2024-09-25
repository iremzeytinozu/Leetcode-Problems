class Solution(object):
    def longestCommonPrefix(self, strs):
        
        first = strs[0]

        for i in range(len(first)):
            for second in strs[1:]:
                if (i == len(second) or second[i] != first[i]):
                    return first[0:i]

        return first