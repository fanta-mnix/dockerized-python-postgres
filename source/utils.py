def flatten(xs):
    import itertools
    return itertools.chain(*xs)


def flatmap(func, xs):
    return flatten(map(func, xs))


def map_values(func, dictionary):
    return {key: func(value) for key, value in dictionary.items()}


def as_generator(iterator):
    return (x for x in iterator)
