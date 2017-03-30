# -*- coding: utf-8 -*-
# big-step semantics

class Expression:
  def __str__(self):
    return '«{}»'.format(self.str())
  def __repr__(self):
    return '«{}»'.format(self.str())
  def __eq__(self, other):
    if other is None or type(self) != type(other): return False
    return self.__dict__ == other.__dict__


class Statement(Expression):
  pass


class Number(Expression):
  def __init__(self, value):
    self.value = value

  def str(self):
    return str(self.value)

  def evaluate(self, environment):
    return self


class Boolean(Expression):
  def __init__(self, value):
    self.value = value

  def str(self):
    return str(self.value)

  def evaluate(self, environment):
    return self


class Variable(Expression):
  def __init__(self, name):
    self.name = name

  def str(self):
    return str(self.name)

  def evaluate(self, environment):
    return environment[self.name]


class Add(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def str(self):
    return '{} + {}'.format(self.left.str(), self.right.str())

  def evaluate(self, environment):
    return Number(self.left.evaluate(environment).value + self.right.evaluate(environment).value)


class Multiply(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def str(self):
    return '{} * {}'.format(self.left.str(), self.right.str())

  def evaluate(self, environment):
    return Number(self.left.evaluate(environment).value * self.right.evaluate(environment).value)


class LessThan(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def str(self):
    return '{} < {}'.format(self.left.str(), self.right.str())

  def evaluate(self, environment):
    return Boolean(self.left.evaluate(environment).value < self.right.evaluate(environment).value)



class DoNothing(Statement):
  def __eq__(self, other):
    if other is None or type(self) != type(other): return False

  def str(self):
    return 'Do-Nothing'

  def evaluate(environment):
    return environment


class Assign(Statement):
  def __init__(self, name, expression):
    self.name = name
    self.expression = expression

  def str(self):
    return '{} = {}'.format(self.name, self.expression.str())

  def evaluate(self, environment):
    return dict(environment.items() + [(self.name, self.expression.evaluate(environment))])


class If(Statement):
  def __init__(self, condition, consequence, alternative):
    self.condition = condition
    self.consequence = consequence
    self.alternative = alternative

  def str(self):
    return 'If ({}) {{ {} }} else {{ {} }}'.format(self.condition.str(), self.consequence.str(), self.alternative.str())

  def evaluate(self, environment):
    cond = self.condition.evaluate(environment)
    if cond == Boolean(True):
      return self.consequence.evaluate(environment)
    elif cond == Boolean(False):
      return self.alternative.evaluate(environment)


class Sequence(Statement):
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def str(self):
    return '{}; {}'.format(self.first.str(), self.second.str())

  def evaluate(self, environment):
    return self.second.evaluate(self.first.evaluate(environment))


class While(Statement):
  def __init__(self, condition, body):
    self.condition = condition
    self.body = body

  def str(self):
    return 'While ({}) {{ {} }}'.format(self.condition.str(), self.body.str())

  def evaluate(self, environment):
    cond = self.condition.evaluate(environment)
    if cond == Boolean(True):
      return self.evaluate(self.body.evaluate(environment))
    elif cond == Boolean(False):
      return environment
