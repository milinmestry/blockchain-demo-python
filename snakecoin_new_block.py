import datetime as date
from snakecoin_block import Block

def next_block(lastBlock):
  thisIndex = lastBlock.index + 1
  thisTimestamp = date.datetime.now()
  thisData = "Hey! I'm new Block " + str(thisIndex)
  thisHash = lastBlock.hash

  return Block(thisIndex, thisTimestamp, thisData, thisHash)