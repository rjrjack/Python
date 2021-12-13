
        # If you put an asterisk in the parameter list, then all parameters after
        # the asterisk must be keyvalue parameters
def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(1, 2, c=3, d=4)

        # not allowed:
# foo(1, 2, 3, 4)

        # arguments after variable-count arguments must be keyword arguments
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)
foo(8, 9, 10, last=50)


def foo(*args, **kwargs):
    print()
    for arg in args:
        print(arg)
    print(kwargs)
foo(8, 9, 10, last=50)

        # This is the same as above, except using x and xx.
        # use args and kwargs for documentation purposes
def foo(*x, **xx):
    print()
    for x in x:
        print(x)
    print(xx)
foo(8, 9, 10, last=50)