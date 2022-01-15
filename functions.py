def myAll(func, iterable):
    return all(func(x) for x in iterable)