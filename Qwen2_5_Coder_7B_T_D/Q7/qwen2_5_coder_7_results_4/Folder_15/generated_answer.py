def all_even_ints_inclusive(arr):
    return [x for i, x in enumerate(arr) if 0 <= i <= 3 and x % 2 == 0]