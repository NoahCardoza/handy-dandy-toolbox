# Python

```py
def pipe(val, *fns):
    """Pipe `val` through functions"""
    for fn in fns:
        val = fn(val)
    return val


def find(key, value, iterable, default=None):
    """Find an object in a list by a key/val pair match."""
    return next((item for item in iterable if item[key] == value), default)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
```
