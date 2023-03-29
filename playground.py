def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# * makes a tuple

print(add(1, 4, 12, 5, 7, 8))


# ** makes a dict
def calculate(**kwargs):
    print(kwargs)
