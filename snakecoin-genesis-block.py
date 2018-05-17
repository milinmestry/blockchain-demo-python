import datetime as date

def create_genesis_block():
  # manually construct a Block with some default values.
  return Block(0, date.datetime.now(), "Genesis Block", "0")
