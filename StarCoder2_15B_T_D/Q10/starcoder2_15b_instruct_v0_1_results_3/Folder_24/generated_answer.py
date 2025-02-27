def all_odd_ints_exclusive(integers):
    return [x for i, x in enumerate(integers) if i % 2 == 1 and 13 < i < 66]