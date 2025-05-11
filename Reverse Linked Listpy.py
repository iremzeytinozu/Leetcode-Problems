# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):

        prev, curr = None, head

        while curr:
            nxt = curr.next # ilk önceki node'u tut
            curr.next = prev # curr.next'i önceki node'a bağla
            prev = curr # önceki node'u güncelle
            curr = nxt # curr'ı bir sonraki node'a geç
        # döngü bittiğinde, prev son node'u gösterir
        # ve başı döndürmek için onu döndürüyoruz

        return prev        