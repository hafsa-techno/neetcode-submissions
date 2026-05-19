class NodeList:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.buckets = [None] * self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        curr = self.buckets[index]
        while (curr):
            if (curr.key == key):
                curr.value = value
                return
            curr = curr.next
        node = NodeList(key, value)
        node.next = self.buckets[index]
        self.buckets[index] = node

    def get(self, key: int) -> int:
        index = key % self.size
        curr = self.buckets[index]
        while (curr):
            if (curr.key == key):
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        curr = self.buckets[index]
        if (curr and curr.key == key):
            self.buckets[index] = curr.next
            return
        while (curr and curr.next):
            if (curr.next.key == key):
                curr.next = curr.next.next
                return
            curr.next = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)