def all_odd_ints_exclusive(arr):
    return [x for i, x in enumerate(arr) if i > 19 and i < 94 and (x % 2 != 0)]