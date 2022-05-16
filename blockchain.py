from block import Block
from vigenere import cvigenere, dvigenere

class Blockchain:
    def __init__(self, viginere = False):
        self.chain = []
        self.proof = []
        self.genesis_block()
        self.viginere = viginere

    def genesis_block(self):
        data = []
        genesis_block = Block(data, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)
        self.proof.append('None')

    def add_block(self, data, password = 'password'):
        previous_hash = (self.chain[len(self.chain)-1]).hash
        if self.viginere:
            new_block = Block(cvigenere(str(data), password), previous_hash)
        else:
            new_block = Block(data, previous_hash)
        new_block.generate_hash()
        proof = self.proof_of_work(new_block)
        if self.validate_chain():
            self.chain.append(new_block)
            self.proof.append(proof)
        else: 
            print("Chain is invalid, block not added")
            return
        return proof, new_block

    def print_blocks(self, password = 'password'):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print(f'\nBlock {i} {current_block}')
            if self.viginere:
                print(f'''
                timestamp: {current_block.time_stamp}
                contents: {dvigenere(str(current_block.data), password)}
                current hash: {current_block.generate_hash()}
                previous hash: {current_block.previous_hash}''')
            else:
                current_block.print_contents()
    
    def print_block(self, block_number, password = 'password'):
        block = self.chain[block_number]
        print(f'\nBlock no. {block_number}: ')
        if self.viginere:
            print(f'''
            timestamp: {block.time_stamp}
            contents: {dvigenere(block.data, password)}
            current hash: {block.generate_hash()}
            previous hash: {block.previous_hash}''')
        else:
            block.print_contents()

    def print_proof(self, block_number):
        proof = self.proof[block_number]
        print(f'Proof of work hash for block no. {block_number}: {proof}')

    def save(self, name = 'blockchain'):
        dump = ''
        with open(f'{str(name)}.csv', 'w') as dumpout:
            for i in range(len(self.chain)):
                dump += f'{i};{self.chain[i].time_stamp};{self.chain[i].data};{self.chain[i].previous_hash};{self.chain[i].hash}\n'
            dumpout.write(dump)
            return dump
    
    def load(self, file):
        with open(file) as loadfrom:
            blocks = loadfrom.readlines()
        for i in range(int(blocks[-1][0])):
            self.add_block('temp')
        for block in blocks:
            split = block.split(';')
            i = int(split[0])
            self.chain[i].time_stamp = split[1]
            self.chain[i].data = split[2]
            self.chain[i].previous_hash = split[3]
            self.chain[i].hash = self.chain[i].generate_hash()
        print(f'Loaded {file} to blockchain')
        return blocks

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if(current.hash != current.generate_hash()):
                print(f"Block no. {i}'s hash does not equal generated hash")
                return False
            if(current.previous_hash != previous.generate_hash()):
                print(f"Block no. {i-1}'s hash got changed")
                return False
        return True
 
    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != "0"*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
      