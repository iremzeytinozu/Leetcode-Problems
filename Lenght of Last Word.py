class Solution(object):
    def lenghtOfLastWord(self, s):
        array = s.split()
        return len(array[-1])
    


class Solutions(object):
    def lengthOfLastWord(self, s):

        lenght = 0

        i = len(s) - 1 # su -1'i araştır "indeksleme için kullanılan -1 diye"

        while i >= 0 and s[i] == ' ':
            i -= 1

        while i >= 0 and s[i] != ' ':
            lenght += 1
            i -= 1

        return lenght

