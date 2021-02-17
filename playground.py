#
#   unlimited positional arguments
#
def add(*args):
    print(type(args))
    print(args[1])
    total = 0
    for num in args:
        total += num
    print(total)
    return total


add(1, 2, 3, 4, 5, 6, 7, 8)
