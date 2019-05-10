# Tutorial-annotations-pyte-hints-live-84
Tutorial made from 'Live de Python #84 -Type Hints e anotações de funções' (Eduardo Mendes) by Marcus Mariano 

---

## Introduction

Tutorial for annotations with python.

All files run in pipenv environment.

Packages

- builtins
    - typing

Dev-packages

- mypy
- monkeytype

---

## Installation

```sh

pipenv install --dev

```

---

## How to Run

```sh

python exemplo_1.py

```
---

## Tests

### MyPy 

Code for exemplo_2.py
```sh
'1' + 1
```


```sh
mypy exemplo_2.py
```
Got an error

```sh
exemplo_2.py:12: error: Unsupported operand types for + ("str" and "int")
```


### MonkeyType

Create monkeytype.sqlite3

```sh

monkeytype run exemplo_4.py

```

Run monkeytype.sqlite3 from stub

```sh

monkeytype stub minha_lib

```

Create stub file from monkeytype

```sh

monkeytype stub minha_lib > stub.pyi

```

Apply monkeytype annotations in an stub file

```sh

monkeytype apply minha_lib

```

---

## License

Code and documentation are available according to the GNU GENERAL PUBLIC LICENSE Version 3 (see [LICENSE](https://www.gnu.org/licenses/gpl.html)).
