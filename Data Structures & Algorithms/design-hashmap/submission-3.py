class MyHashMap:

    def __init__(self):
        self.map = []
        

    def put(self, key: int, value: int) -> None:
        index_to_update = next((i for i, (k, _) in enumerate(self.map) if k == key), None)
        if index_to_update is not None:
            self.map[index_to_update] = (key, value)
        else:
            self.map.append((key, value))

    def get(self, key: int) -> int:
        return next((item[1] for item in self.map if item[0] == key), -1)
        

    def remove(self, key: int) -> None:
        index_to_remove = next((i for i, (k, _) in enumerate(self.map) if k == key), None)
        if index_to_remove is not None:
            self.map.pop(index_to_remove)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)