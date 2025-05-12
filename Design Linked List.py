class DoublyLinkedList:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.left = DoublyLinkedList(0) # head
        self.right = DoublyLinkedList(0) # tail
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1
        

    def addAtHead(self, val):
        node, next, prev = DoublyLinkedList(val), self.left.next, self.left

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val):
        node, next, prev = DoublyLinkedList(val), self.right, self.right.prev

        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

        
    def addAtIndex(self, index, val):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur:
            node, next, prev = DoublyLinkedList(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev
        

    def deleteAtIndex(self, index):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right:
            next, prev = cur.next, cur.prev
            prev.next = next
            next.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)