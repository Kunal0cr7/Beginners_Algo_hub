//Code contributed by Priyanshu_6497
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data, nonce):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data) + str(nonce)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", 0, calculate_hash(0, "0", int(time.time()), "Genesis Block", 0))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0
    hash = calculate_hash(index, previous_block.hash, timestamp, data, nonce)

    while not hash.startswith('0000'):  # Proof of Work: Finding a hash with four leading zeros
        nonce += 1
        hash = calculate_hash(index, previous_block.hash, timestamp, data, nonce)

    return Block(index, previous_block.hash, timestamp, data, nonce, hash)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Number of blocks to add to the chain
num_blocks_to_add = 5

# Add blocks to the blockchain
for i in range(num_blocks_to_add):
    new_data = f"Data for Block {i+1}"
    new_block = create_new_block(previous_block, new_data)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Block #{new_block.index} has been added to the blockchain!")
    print(f"Hash: {new_block.hash}\n")
