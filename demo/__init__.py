def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def foo(total, param, ls):
    l = len(ls)
    if l == 0:
        return total / l + param

def bounded_integer(collection):
    a = len(collection)
    # Note that we do not support Python's comparison chains yet. See DBD-423
    if 1 < a and a < 3:
        return 1 / (a - 2)


def bounded_index_variable(x):
    ls = [1, 2, 3]
    i = len(x)
    if i >= 3:
        return ls[i]
    

def redundant_condition():
    i = len(x)
    if i > 0:
        if i > 10:
            ...
