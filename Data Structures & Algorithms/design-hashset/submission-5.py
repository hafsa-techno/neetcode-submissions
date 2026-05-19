class NodeList:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size
    def add(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]

        while (curr):
            if (curr.val == key):
                return
            curr = curr.next
        node = NodeList(key)
        node.next = self.buckets[index]
        self.buckets[index] = node

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]
        if (curr and curr.val == key):
            self.buckets[index] = curr.next
        while (curr and curr.next):
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        curr = self.buckets[index]
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False

# index = self._hash(key)
# if (self.buckets[index] is None):
#     node = NodeList(key)
#     self.buckets[index] = node
# else:
#     curr = self.buckets[index]
#     while (curr and curr.next):
#         if (curr.val == key):
#             break
#         curr = curr.next
#     if (curr.val == key):
#         return
#     curr.next = NodeList(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)