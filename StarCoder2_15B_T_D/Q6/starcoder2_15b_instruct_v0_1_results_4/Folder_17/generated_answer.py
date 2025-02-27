def all_neg_ints_exclusive(ints):
    assert isinstance(ints, list), 'ints must be a list'
    assert all((isinstance(x, int) for x in ints)), 'ints must contain only integers'
    return [x for x in ints[62:96] if x < 0]