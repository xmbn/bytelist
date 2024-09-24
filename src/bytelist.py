class bytelist(bytearray):
  def __init__(self, value, max=None):
    self.max = max
    super().__init__(value)
    self.trim()
  def pop(self):
    if len(self) > 0:
      item = self[0]
      self[:] = self[1:]
      return item
    return None
  def trim(self):
    if self.max is not None:
      self[:] = self[-self.max:]
  def append(self, value):
    super().append(value)
    self.trim()
