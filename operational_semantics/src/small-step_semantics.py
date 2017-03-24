#small-step semantics

class Number:
  def __init__(self, value):
    self.value = value

class Add:
  def __init__(self, left, right):
    self.left = left
    self.right = right

class Multiply:
  def __init__(self, left, right):
    self.left = left
    self.right = right
