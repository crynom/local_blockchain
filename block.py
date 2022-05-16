import datetime
from hashlib import sha256


class Block:
    def __init__(self, data, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = f'{self.time_stamp}{self.data}{self.previous_hash}{self.nonce}'
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        print(f'''
        timestamp: {self.time_stamp}
        contents: {self.data}
        current hash: {self.generate_hash()}
        previous hash: {self.previous_hash}''')
        