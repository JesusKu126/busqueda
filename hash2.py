import hashlib

class StudentHashTable:
    def __init__(self):
        self.table = {}

    def _hash(self, key):
        return hashlib.sha256(key.encode()).hexdigest()

    def insert(self, name, student_id):
        hashed_name = self._hash(name)
        self.table[hashed_name] = student_id

    def retrieve(self, name):
        hashed_name = self._hash(name)
        return self.table.get(hashed_name, None)

    def remove(self, name):
        hashed_name = self._hash(name)
        if hashed_name in self.table:
            del self.table[hashed_name]
            return True
        return False

# Ejemplo de uso
hash_table = StudentHashTable()
hash_table.insert("Alice", "ID001")
hash_table.insert("Bob", "ID002")
hash_table.insert("Charlie", "ID003")

print(hash_table.retrieve("Alice"))    # Output: ID001
print(hash_table.retrieve("Bob"))      # Output: ID002
print(hash_table.retrieve("Charlie"))  # Output: ID003
print(hash_table.retrieve("David"))    # Output: None

hash_table.remove("Bob")
print(hash_table.retrieve("Bob"))      # Output: None

