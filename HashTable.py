
class HashTable:
    def __init__(self, initial_length = 10):
        self.map = []
        for i in range(initial_length):
            self.map.append([])
    # Time: O(1)
    # Space: O(1)
    def create_hash(self, key):
        hash_value = hash(key) % len(self.map)
        return hash_value

    # Time: O(n)
    # Space: O(n)
    def insert(self, key, value):
        bucket = self.create_hash(key)
        bucket_list = self.map[bucket]

        for i in range(len(bucket_list)):
            if bucket_list[i][0] == key:
                bucket_list[i][1] = value
                return
        bucket_list.append([key, value])

    # Time: O(n)
    # Space: O(n)
    def search(self, key):
        bucket = self.create_hash(key)
        bucket_list = self.map[bucket]

        for i in range(len(bucket_list)):
            if bucket_list[i][0] == key:
                value = bucket_list[i][1]
                return value
        # TODO: add a null return-ish thing
