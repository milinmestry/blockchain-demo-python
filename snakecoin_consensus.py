from snakecoin_blockchain import blockchain

# Store the url data of every
# other node in the network
# so that we can communicate
# with them
peerNodes = []

@node.route('/blocks', methods=['GET'])
def get_blocks():
  chainToSend = blockchain

  # convert our blocks into dictionaries so that we can send
  # them as JSON objects later
  for block in chainToSend:
    blockIndex = str(block.index)
    blockTimestamp = str(block.timestamp)
    blockData = str(block.data)
    blockHash = block.hash

    block = {
      "index": blockIndex,
      "timestamp": blockTimestamp,
      "data": blockData,
      "hash": blockHash
    }

    # send our chain to whomever requested it
    chainToSend = json.dumps(chainToSend)
    return chainToSend

  def find_new_chains():
    # Get blockchains of every other nodes
    otherChains = []

    for nodeUrl in peerNodes:
      # Get their chains using a GET request
      block = requests.get(nodeUrl + "/blocks").content

      # Convert the json object into python dictionary
      block = json.loads(block)

      # Add it to our list
      otherChains.append(block)

      return otherChains

    def consensus():
      # Get the blocks from other nodes
      otherChains = find_new_chains()

      # If our chain is longest, then we store the longest chain
      longestChain = blockchain

      for chain in otherChains:
        if len(longestChain) < len(chain):
          longestChain = chain

        # If the longest chain wasn't ours, then we
        # set our chain to the longest
        blockchain = longestChain

