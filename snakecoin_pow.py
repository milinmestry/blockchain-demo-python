from flask import Flask
from flask import request
from snakecoin_block import Block
from snakecoin_blockchain import blockchain

import datetime as date
import json

node = Flask(__name__)

# blockchain

# Class blockchain definition

minerAddress = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

# Store the transactions that this node has in the list
thisNodeTransactions = []

def proof_of_work(lastProof):
  # Create a variable that will used to find our next proof of work

  incrementor = lastProof + 1

  # Keep incrementing the incrementor until it's equal to a number
  # divisible by 9 and the proof of work of the previous block in the chain
  while not(incrementor % 9 == 0 and incrementor % lastProof == 0):
    incrementor += 1

  # once that number is found, we can return it as
  # our proof of work
  return incrementor

@node.route('/mine', methods=['GET'])
def mine():
  # Get the last proof of work
  lastBlock = blockchain[len(blockchain) - 1]
  lastProof = lastBlock.data['proof-of-work']

  # Find the proof of work for the current blocked mined
  # Note: Program will hang here until a new proof of work is found
  proof = proof_of_work(lastProof)

  # Once we find a valid proof of work, we know we can mine a block so
  # we reward miner by adding a transaction
  thisNodeTransactions.append(
    {"from": "Network", "to": minerAddress, "amount": 1}
  )

  # Now we can gather the data needed to create a new block
  newBlockData = {
    "proof-of-work": proof,
    "transactions": list(thisNodeTransactions)
  }

  newBlockIndex = lastBlock.index + 1
  newBlockTimestamp = thisTimestamp = date.datetime.now()
  lastBlockHash = lastBlock.hash


  # Empty transactions list
  thisNodeTransactions[:] = []

  # Now create the new block
  minedBlock = Block(
    newBlockIndex,
    newBlockTimestamp,
    newBlockData,
    lastBlockHash
  )

  blockchain.append(minedBlock)

  # let client know we mined a block
  return json.dumps({
    "index": newBlockIndex,
    "timestamp": str(newBlockTimestamp),
    "data": newBlockData,
    "hash": lastBlockHash
  }) + "\n"

node.run(debug = True)