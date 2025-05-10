class Solution(object):
    def calPoints(self, operations):
        result = []

        for op in operations:
            if op == 'C':
                result.pop()
            elif op == 'D':
                result.append(2 * result[-1])
            elif op == '+':
                result.append(result[-1] + result[-2])
            else:
                result.append(int(op))

        return sum(result)
