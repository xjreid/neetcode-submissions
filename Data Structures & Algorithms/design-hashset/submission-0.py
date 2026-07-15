class MyHashSet:

    def __init__(self):
        self.buckets = [None] * 1000;

    def add(self, key: int) -> None:
        place = hash(key) % 1000
        if self.buckets[place] is None:
            self.buckets[place] = [key]
        else:
            if not key in self.buckets[place]:
                self.buckets[place].append(key)

    def remove(self, key: int) -> None:
        place = hash(key) % 1000
        if not self.buckets[place] is None:
            if key in self.buckets[place]:
                self.buckets[place].remove(key)

    def contains(self, key: int) -> bool:
        place = hash(key) % 1000
        if not self.buckets[place] is None:
            if key in self.buckets[place]:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)