#
#   unlimited positional arguments
#
def add(*args):
    print("type(args):", type(args))
    print("args[1]:", args[1])
    total = 0
    for num in args:
        total += num
    print("total: ", total)
    return total


add(1, 2, 3, 4, 5, 6, 7, 8)


def calculate(n, **kwargs):
    print("kwargs: ", kwargs)
    for key, val in kwargs.items():
        print(f"{key}:{val}")
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=5, multiply=6)
