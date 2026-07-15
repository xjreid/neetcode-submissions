class MyHashMap:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.val = value

    def __init__(self):
        self.buckets = [[] for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        place = hash(key) % 1000
        for Node in self.buckets[place]:
            if Node.key == key:
                Node.val = value
                return
        self.buckets[place].append(MyHashMap.Node(key, value))


    def get(self, key: int) -> int:
        place = hash(key) % 1000
        for Node in self.buckets[place]:
            if Node.key == key:
                return Node.val
        return -1

    def remove(self, key: int) -> None:
        place = hash(key) % 1000
        for i in range(len(self.buckets[place])):
            if self.buckets[place][i].key == key:
                self.buckets[place].pop(i)
                return;


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)