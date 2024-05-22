class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def retrieve(self, key):
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return True
        return False

hash_table = HashTable(10)
hash_table.insert("manzana", 3)
hash_table.insert("banana", 5)
hash_table.insert("naranja", 2)

print(hash_table.retrieve("manzana"))  
print(hash_table.retrieve("banana"))   
print(hash_table.retrieve("naranja"))  
print(hash_table.retrieve("pera"))    

hash_table.remove("banana")
print(hash_table.retrieve("banana"))   