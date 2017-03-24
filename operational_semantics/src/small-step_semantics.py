# -*- coding: utf-8 -*-

#small-step semantics

class Number:
  def __init__(self, value):
    self.value = value
    self.reducible = False
  def __str__(self):
    return '«%s»' % self.str()
  def __repr__(self):
    return '«%s»' % self.str()
  def str(self):
    return str(self.value)


class Add:
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.reducible = True
  def __str__(self):
    return '«%s»' % self.str()
  def __repr__(self):
    return '«%s»' % self.str()
  def str(self):
    return '%s + %s' % (self.left.str(), self.right.str())
  def reduce(self):
    if self.left.reducible:
      return Add(self.left.reduce, self.right)
    elif self.right.reducible:
      return Add(self.left, self.right.reduce)
    else:
      return Number(self.left.value + self.right.value)


class Multiply:
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.reducible = True
  def __str__(self):
    return '«%s»' % self.str()
  def __repr__(self):
    return '«%s»' % self.str()
  def str(self):
    return '%s * %s' % (self.left.str(), self.right.str())
  def reduce(self):
    if self.left.reducible:
      return Add(self.left.reduce, self.right)
    elif self.right.reducible:
      return Add(self.left, self.right.reduce)
    else:
      return Number(self.left.value * self.right.value)


if __name__ == "__main__":
  exp = Add(Number(2),Add(Number(2), Number(3)))
  print('exp is %s' % exp)
  print(exp.reducible)
  exp = exp.reduce #なぜ "<bound method Add.reduce of «2 + 2 + 3»>" になるのか…
  print(exp.reducible)
  exp
