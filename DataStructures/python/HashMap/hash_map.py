#!/home/mhyde/vEnvs/py36/bin/python

class HashMap:
    def __init__(self, array_size=None):
        self.array_size = array_size
        self.array = [None for _ in range(array_size)]

    def assign(self, key, data):
        idx = self.compressed_hash(self.hash_code(key))
        curr_data = self.array[idx]

        if curr_data == None or curr_data[0] == key:
            self.array[idx] = [key, data]
            return

        collisions = 1

        while curr_data[0] != key:
            temp_hash_idx = self.compressed_hash(self.hash_code(key, collisions))
            curr_data = self.array[temp_hash_idx]

            if curr_data == None or curr_data[0] == None:
                self.array[temp_hash_idx] = [key, data]
                return

            collisions += 1

        return

    def retrieve(self, key):
        idx = self.compressed_hash(self.hash_code(key))
        expected_return = self.array[idx]

        if expected_return is None:
            return None

        if expected_return[0] == key:
            return expected_return[1]

        collisions = 1

        while expected_return[0] != key:
            idx = self.compressed_hash(self.hash_code(key, collisions))
            expected_return = self.array[idx]

            if expected_return is None:
                return None

            if expected_return[0] == key:
                return expected_return[1]

            collisions += 1

    def hash_code(self, key, collisions=0):
        '''
        Method takes the key as a user-desired input,
        encodes it into bytes, then adds the sum of the
        bytes. This way, any key of any data type can
        be stored and manipulated to Hash Map Functional
        Standards.
        '''
        key_to_bytes = key.encode()
        hash_code = sum(key_to_bytes)
        return hash_code + collisions

    def compressed_hash(self, hash_code):
        '''
        The Hash Code method could theoretically return
        any value. This compressor method returns the
        remainder of the hash code when divided by the
        size of the hash map. This ensures that each
        key can exist within the length of the hash map.
        '''
        return hash_code % self.array_size

if __name__ == '__main__':
    my_hashmap = HashMap(4)
    
    keys = ['Motor Comm', 'Peripheral Comm', 'Serial Comm', 'Master Comm']
    data = ['/dev/ttyUSB0', 'ttyUSB1', 'ttyUSB2', 'ttyUSB3']

    for i in range(len(keys)):
        my_hashmap.assign(keys[i], data[i])
    
    print(my_hashmap.array)