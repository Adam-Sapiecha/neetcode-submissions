class MyHashSet:

    def __init__(self):
        self.zestaw = set()

    def add(self, key: int) -> None:
        self.zestaw.add(key)

    def remove(self, key: int) -> None:
        if key in self.zestaw:
            self.zestaw.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.zestaw


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)