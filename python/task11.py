import random

class RandomizedSet:

    def __init__(self, lst=None):
        self.lst = []
    def insert(self, val: int) -> bool:
        lst = self.lst
        for i in lst:
            if i == val:
                return False
        lst.append(val)
        return True
    def remove(self, val: int) -> bool:
        lst = self.lst
        for i in range(len(lst)):
            if lst[i] == val:
                lst.pop(i)
                return True
        return False

    def getRandom(self) -> int:
        lst = self.lst
        return random.choice(lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()