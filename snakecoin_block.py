import hashlib as hasher

class Block(object):
  def __init__(self, index, timestamp, data, previousHash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previousHash = previousHash
    self.hash = self.hash_block()

  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) +
      str(self.timestamp) +
      str(self.data) +
      str(self.previousHash))
    return sha.hexdigest()