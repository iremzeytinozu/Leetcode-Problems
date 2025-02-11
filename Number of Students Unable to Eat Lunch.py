class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        res = len(students) # baslagictaki ogrenci sayisi
        count = Counter(students) # ogrencilerin tercihlerini sayiyor (kac tane 1 kac tane 0)

        for s in sandwiches:
            if count[s] > 0:
                res -= 1
                count[s] -= 1
            else:
                return res

        return res