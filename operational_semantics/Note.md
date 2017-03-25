## p.20~ Small Step Semantics

### p.22 はじめの抽象構文木の構築

```Python3
Add(
  Multiply(Number(1), Number(2)),
  Multiply(Number(3), Number(4))
)
```

### p.27 式の簡約の実現

```Python3

expression = Add(
  Multiply(Number(1), Number(2)),
  Multiply(Number(3), Number(4))
)

expression.reducible
expression.reduce_exp()
#...

```


### p.28 仮想機械の実行

```Python3
Machine(
  Add(
    Multiply(Number(1), Number(2)),
    Multiply(Number(3), Number(4))
  )
).run()
```


## p.29 Boolean, LessThanの実装後のスニペット

```Python3
Machine(
  LessThan(
    Number(5),
    Add(Number(2), Number(2))
  )
).run()
```

## p.30 環境を入れた機械

```Python3
Machine(
  Add(Variable('x'), Variable('y')),
  { 'x': Number(3), 'y': Number(4) } # environment
).run()
```