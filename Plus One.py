class Solution(object):
    def plusOne(self, digits):

        for i in range(len(digits) - 1, -1, -1):
            """
            ilk -1 listenin uzunluğu 0'dan başlamadığından dolayı indekse odaklı yapılmış bir şey eksi bir yani
            ortadaki -1 döngünün nerede duracağını belirtir. döngü 0 dahil olmak üzere çalışır ama -1'e yani son indekse ulaştığında durur
            sonuncu -1 ise döngünün artan sırada değil azalan sırada ilerlemesini sağlar.yani0'dan -1'e kadar ilerleyecekti artık -1'den 0'a kadar ilerleyecek gibi
            """

            if digits[i] < 9:
                digits[i] += 1
                return digits

            else:
                digits[i] = 0

        return [1] + digits