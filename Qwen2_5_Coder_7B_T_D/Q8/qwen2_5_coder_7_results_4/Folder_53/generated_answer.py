def all_even_ints_exclusive(arr):
    return [x for i, x in enumerate(arr) if i > 100 and i < 101 and (x % 2 == 0)]