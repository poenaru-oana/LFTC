class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self.items = [list() for _ in range(size)]

    def get_size(self):
        return self.size

    def hash(self, key):
        if (type(key) == str):
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size
        return key % self.size

    def contains(self, entry):
        hashValue = self.hash(entry)
        return any(item == entry for item in self.items[hashValue])

    def add(self, item):
        hash_value = self.hash(item)

        if not self.contains(item):
            self.items[hash_value].append(item)
        return hash_value

    def get(self, key):
        hash_value = self.hash(key)
        for item in self.items[hash_value]:
            if item.key == key:
                return item.value
        return None

    def toString(self):
        String = ""
        for index, list in enumerate(self.items):
            for entry in list:
                String = String + f"{entry}        - at hashed value -       {index} \n "

        return String