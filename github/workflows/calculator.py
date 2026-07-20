
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
```

### `test_calculator.py`

```python
from calculator import add, subtract, multiply

def test_add():
    assert add(3, 5) == 8

def test_add_negative():
    assert add(-2, 7) == 5

def test_subtract():
    assert subtract(10, 3) == 7

def test_subtract_negative():
    assert subtract(5, 8) == -3

def test_multiply():
    assert multiply(4, 5) == 20

def test_multiply_zero():
    assert multiply(7, 0) == 0
```

### `requirements.txt`

```
pytest==8.3.0
