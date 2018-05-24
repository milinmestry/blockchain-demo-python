import datetime as date
from snakecoin_block import Block

def create_genesis_block():
  # manually construct a Block with some default values.
  return Block(0, date.datetime.now(), {
    "proof-of-work": 9, "transactions": None
  }, "0")
