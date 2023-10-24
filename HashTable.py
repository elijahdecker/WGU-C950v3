
class HashTable:
    def __init__(self, initial_length = 10):
        self.map = []
        for i in range(initial_length):
            self.map.append([])
    def create_hash(self, key):
        hash_value = hash(key) % len(self.map)
        return hash_value

    def insert(self, key, value):
        bucket = self.create_hash(key)
        bucket_list = self.map[bucket]

        for i in range(len(bucket_list)):
            if bucket_list[i][0] == key:
                bucket_list[i][1] = value
                return
        bucket_list.append([key, value])

    def search(self, key):
        bucket = self.create_hash(key)
        bucket_list = self.map[bucket]

        for i in range(len(bucket_list)):
            if bucket_list[i][0] == key:
                value = bucket_list[i][1]
                print(value)
                return
        print("nothing")

