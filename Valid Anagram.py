class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Python'un collections modülünde bulunan bir araçtır. 
        # Bir stringdeki her harfi ve harflerin sayısını bir tür "sözlük" (dictionary) yapısıyla saklar.
        return Counter(s) == Counter(t)