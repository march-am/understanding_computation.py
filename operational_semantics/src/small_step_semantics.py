# -*- coding: utf-8 -*-
#small-step semantics

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
    self.reducible = False

  def str(self):
    return str(self.value)


class Add(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.reducible = True

  def str(self):
    return '{} + {}'.format(self.left.str(), self.right.str())

  def reduce_exp(self, environment):
    if self.left.reducible:
      return Add(self.left.reduce_exp(environment), self.right)
    elif self.right.reducible:
      return Add(self.left, self.right.reduce_exp(environment))
    else:
      return Number(self.left.value + self.right.value)


class Multiply(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.reducible = True

  def str(self):
    return '{} * {}'.format(self.left.str(), self.right.str())

  def reduce_exp(self, environment):
    if self.left.reducible:
      return Add(self.left.reduce_exp(environment), self.right)
    elif self.right.reducible:
      return Add(self.left, self.right.reduce_exp(environment))
    else:
      return Number(self.left.value * self.right.value)


class Boolean(Expression):
  def __init__(self, value):
    self.value = value
    self.reducible = False

  def str(self):
    return str(self.value)


class LessThan(Expression):
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.reducible = True

  def str(self):
    return '{} < {}'.format(self.left.str(), self.right.str())

  def reduce_exp(self, environment):
    if self.left.reducible:
      return LessThan(self.left.reduce_exp(environment), self.right)
    elif self.right.reducible:
      return LessThan(self.left, self.right.reduce_exp(environment))
    else:
      return Boolean(self.left.value < self.right.value)


class Variable(Expression):
  def __init__(self, name):
    self.name = name
    self.reducible = True

  def str(self):
    return str(self.name)

  def reduce_exp(self, environment):
    return environment[self.name]


class DoNothing(Statement):
  def __init__(self):
    self.reducible = False

  def __eq__(self, other):
    return isinstance(self, type(DoNothing()))

  def str(self):
    return 'Do-Nothing'


class Assign(Statement):
  def __init__(self, name, expression):
    self.name = name
    self.expression = expression
    self.reducible = True

  def str(self):
    return '{} = {}'.format(self.name, self.expression.str())

  def reduce_exp(self, environment):
    if self.expression.reducible:
      return [Assign(self.name, self.expression.reduce_exp(environment)), environment]
    else:
      # updateすると元配列を破壊するのでdictコンストラクタで新しいdictを返す
      return [DoNothing(), dict(environment.items() + [(self.name, self.expression)])]


class If(Statement):
  def __init__(self, condition, consequence, alternative):
    self.condition = condition
    self.consequence = consequence
    self.alternative = alternative
    self.reducible = True

  def str(self):
    return 'If ({}) {{ {} }} else {{ {} }}'.format(self.condition, self.consequence, self.alternative)

  def reduce_exp(self, environment):
    if self.condition.reducible:
      return [If(self.condition.reduce_exp(environment), self.consequence, self.alternative), environment]
    else:
      if self.condition == Boolean(True):
        return [self.consequence, environment]
      elif self.condition == Boolean(False):
        return [self.alternative, environment]


class Machine:
  def __init__(self, statement, environment):
    self.statement = statement
    self.environment = environment

  def step(self):
    self.statement, self.environment = self.statement.reduce_exp(self.environment)

  def run(self):
    while self.statement.reducible:
      print('{}, {}'.format(self.statement, self.environment))
      self.step()
    print('{}, {}'.format(self.statement, self.environment))
