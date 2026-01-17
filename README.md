# testclaude

![CI](https://github.com/astriker/testclaude/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/astriker/testclaude/branch/master/graph/badge.svg)](https://codecov.io/gh/astriker/testclaude)

A simple Python calculator library with pytest tests.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from src.calculator import add, subtract, multiply, divide

add(2, 3)       # 5
subtract(5, 3)  # 2
multiply(3, 4)  # 12
divide(10, 2)   # 5.0
```

## Testing

```bash
pytest
```
