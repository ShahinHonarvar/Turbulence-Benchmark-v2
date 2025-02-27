def all_neg_ints_exclusive(ints):
    if not isinstance(ints, list) or not all((isinstance(i, int) for i in ints)):
        raise TypeError('The argument must be a list of integers.')

    def is_neg_int(x):
        return x < 0
    return list(filter(is_neg_int, ints[20:35]))