def myAll(func, iterable):
    return all(func(x) for x in iterable)


def filterStudents(func, iterable):
    return list(filter(func, iterable))