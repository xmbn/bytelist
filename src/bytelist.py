#######################################
# bytelist class for Micropython
# Provides new features including pop and a size limit
# Author: Chris Ekstroem
#######################################

__version__ = '2024-09-24'

class bytelist(bytearray):

  def __init__(self, value, max_length=None):
    # initialize with a value and an optional maximum length
    # value can be anything that a built-in bytearray can accept
    # max must be an integer
    self.max_length = max_length # store the max length for use in other functions
    super().__init__(value) # creates a bytearray from the built-in type
    self.trim() # keeps the list length at max if initialization results in a longer array
  
  def pop(self):
    # removes the oldest item in the list and returns its value
    if len(self) > 0: # check first if there is a value to remove
      value = self[0] # store the value to return later
      self[:] = self[1:] # slice the list starting with the second item in the list
      return value # return the removed value
    return None # if the list had no items return nothing
    
  def trim(self):
    # removes any items at the beginnign of the list that are not within the max_length
    if self.max_length is not None: # check first if max_length is set
      self[:] = self[-self.max_length:] # slice the list returning only last items in the max_length window
  
  def append(self, value):
    # adds an item but also performs a trim
    super().append(value) # add item to the bytearray
    self.trim() # limit the list size
