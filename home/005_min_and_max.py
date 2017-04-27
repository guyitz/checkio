def max(*args, **kwargs):
    """

    >>> max([1, 2, 0, 3, 4])
    4
    >>> max(2.2, 5.6, 5.9, key=int)
    5.6
    >>> max(3, 2)
    3

    :param args:
    :param kwargs:
    :return:
    """
    sort_func = kwargs.get('key', lambda x: x)
    if len(args) == 1:
        args = args[0]
    max_arg = None
    for elem in args:
        if max_arg is None or sort_func(elem) > sort_func(max_arg):
            max_arg = elem
    return max_arg


def min(*args, **kwargs):
    """
    >>> min(3, 2)
    2
    >>> min("hello")
    'e'
    >>> min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1])
    [9, 0]
    >>> min(range(-10,10))
    -10
    >>> min(abs(i) for i in range(-10, 10))
    0

    :param args:
    :param kwargs:
    :return:
    """

    sort_func = kwargs.get('key', lambda x: x)
    if len(args) == 1:
        args = args[0]
    min_arg = None
    for elem in args:
        if min_arg is None or sort_func(elem) < sort_func(min_arg):
            min_arg = elem
    return min_arg
