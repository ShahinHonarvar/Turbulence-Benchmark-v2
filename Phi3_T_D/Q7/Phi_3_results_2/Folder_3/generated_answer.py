def all_even_ints_inclusive(ints):
    start_index, end_index = (62, 92)
    return [x for i, x in enumerate(ints[start_index:end_index + 1]) if x % 2 == 0]