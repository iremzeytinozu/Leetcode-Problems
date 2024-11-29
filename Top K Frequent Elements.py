class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        # count dict'ini oluşturma için
        for num in nums:
            # Eğer num daha önce sözlükte varsa onun mevcut değerini al. Yoksa 0 al.
            count[num] = 1 + count.get(num,0)
        

        freq = [[] for i in range(len(nums) + 1)]

        # count sözlüğündeki her bir sayı (num) ve bu sayının tekrar sayısını (cnt) alır.
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res