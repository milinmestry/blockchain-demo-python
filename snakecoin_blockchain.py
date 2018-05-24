from snakecoin_genesis_block import create_genesis_block
# from snakecoin_new_block import next_block

# create the blockchain and add the genesis block
blockchain = []
blockchain.append(create_genesis_block())
previousBlock = blockchain[0]


# How many blocks we need to add to the chain after genesis block
# numberOfBlocks = 20

# Add blocks to the chain
# for i in range(numberOfBlocks):
#   blockToAdd = next_block(previousBlock)
#   blockchain.append(blockToAdd)
#   previousBlock = blockToAdd

#   # Tell everyone about it
#   print "Block #{} has been added to the blockchain!".format(blockToAdd.index)
#   print "Hash: {}".format(blockToAdd.hash)
#   print "previousHash: {}\n".format(blockToAdd.previousHash)
