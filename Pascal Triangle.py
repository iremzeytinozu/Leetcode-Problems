class Solution(object):
    def generate(self, numRows):
        
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        prevRows = self.generate(numRows - 1)

        # numRows uzunluğunda bir liste oluştur ve bu listenin tüm elemanlarını 1 ile doldur
        newRow = [1] * numRows

        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]

        prevRows.append(newRow)
        return prevRows