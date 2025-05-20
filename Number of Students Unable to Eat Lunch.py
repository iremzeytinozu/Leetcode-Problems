class Solution(object):
    def countStudents(self, students, sandwiches):
        res = len(students)

        cnt = {}

        for s in students:
            if s not in cnt:
                cnt[s] = 0
            cnt[s] += 1

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res

        return res
        