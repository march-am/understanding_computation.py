## p.20~ Small Step Semantics

### p.22 はじめの抽象構文木の構築

```python
Add(
  Multiply(Number(1), Number(2)),
  Multiply(Number(3), Number(4))
)
# => «1 * 2 + 3 * 4»
```

### p.27 式の簡約の実現

```python
expression = Add(
  Multiply(Number(1), Number(2)),
  Multiply(Number(3), Number(4))
)
# => «1 * 2 + 3 * 4»
expression.reducible
expression.reduce_exp()
#...
```

### p.28 仮想機械の実行

```python
Machine(
  Add(
    Multiply(Number(1), Number(2)),
    Multiply(Number(3), Number(4))
  )
).run()
```

## p.29 Boolean, LessThanの実装後のスニペット

```python
Machine(
  LessThan(
    Number(5),
    Add(Number(2), Number(2))
  )
).run()
```

## p.30 環境を入れた機械

```python
Machine(
  Add(Variable('x'), Variable('y')),
  { 'x': Number(3), 'y': Number(4) } # environment
).run()
```

## p.31 代入

```python
statement = Assign('x', Multiply(Number(3), Number(4)))
environment = { 'x': Number(2) }

statement, environment = statement.reduce_exp(environment)
```

## p.34 文の扱える仮想機械

```python
Machine(
  Assign(
    'x',
    Add(Variable('x'), Number(1))
  ),
  { 'x': Number(2) }
).run()
```

## p.35 If/If(else節なし)文

```python
Machine(
  If(
    Variable('x'),
    Assign('y', Number(1)),
    Assign('y', Number(2))
  ),
  { 'x': Boolean(True) }
).run()
```

```python
Machine(
  If(Variable('x'), Assign('y', Number(1)), DoNothing()),
  { 'x': Boolean(False) }
).run()
```

## p.37 シーケンス文

```python
Machine(
  Sequence(
    Assign('x', Add(Number(1), Number(1))),
    Assign('y', Add(Variable('x'), Number(3)))
  ),
  {}
).run()
```

## p.38 While文

```python
Machine(
  While(
    LessThan(Variable('x'), Number(5)),
    Assign('x', Multiply(Variable('x'), Number(1)))
  ),
  { 'x': Number(1) }
).run()
```
