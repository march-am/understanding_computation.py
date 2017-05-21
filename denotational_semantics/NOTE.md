##  p.47~ Denotational Semantics

### p.48 式の実装 Number

```Python
Number(5).to_py()
# 'lambda e: 5'
Boolean(False).to_py()
# 'lambda e: False'
```

```Python
la = eval(Number(5).to_py())
print la
# <function <lambda> at 0x10adb7410>
la({})
# 5
la = eval(Boolean(False).to_py())
print la
# <function <lambda> at 0x10ae155f0>
la({})
# False
```

### p.49 式の実装 Variable

```Python
exp = Variable('x')
print exp
# «x»
exp.to_py()
# 'lambda e: e[x]'
la = eval(exp.to_py())
print la
# <function <lambda> at 0x10dd6b410>
la({ 'x': 7 })
# 7
```

### p.50 式の実装 Add/LessThan

```Python
Add(Variable('x'), Number(1)).to_py()
# "lambda e: (lambda e: e['x'])(e) + (lambda e: 1)(e)"
LessThan(Add(Variable('x'), Number(1)), Number(3)).to_py()
# "lambda e: (lambda e: (lambda e: e['x'])(e) + (lambda e: 1)(e))(e) < (lambda e: 3)(e)"
```

#### 検算

```Python
environment = { 'x': 3 }
print environment
# {'x': 3}
la = eval(Add(Variable('x'), Number(1)).to_py())
print la
# <function <lambda> at 0x10c8926e0>
la(environment)
# 4
la = eval(
  LessThan(Add(Variable('x'), Number(1)), Number(3)).to_py()
)
print la
# <function <lambda> at 0x10c834410>
la(environment)
# False
```

### p.51 文の実装 Assign

```Python
statement = Assign('y', Add(Variable('x'), Number(1)))
print statement
# «y = x + 1»
statement.to_py()
# "lambda e: dict(e.items() + [(y, (lambda e: (lambda e: e['x'])(e) + (lambda e: 1)(e))(e))])"
la = eval(statement.to_py())
print la
# <function <lambda> at 0x1085fc410>
la({ 'x': 3 })
# {'y': 4, 'x': 3}
```

### p.52 文の実装 While

```Python
statement = While(
  LessThan(Variable('x'), Number(5)),
  Assign('x', Multiply(Variable('x'), Number(3)))
)
# «while (x < 5) { x = x * 3 }»
statement.to_py()
# "lambda e: inline_while(lambda e: (lambda e: e['x'])(e) < (lambda e: 5)(e), lambda e: dict(e.items() + [('x', (lambda e: (lambda e: e['x'])(e) * (lambda e: 3)(e))(e))]), e)"
la = eval(statement.to_py())
print la
# <function <lambda> at 0x1064275f0>
la({ 'x': 1 })
# {'x': 9}
```
