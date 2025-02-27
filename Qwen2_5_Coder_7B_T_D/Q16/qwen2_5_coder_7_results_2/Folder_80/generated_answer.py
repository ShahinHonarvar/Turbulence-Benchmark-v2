def sum_even_ints_inclusive(arr):
    return sum((x for i, x in enumerate(arr) if 64 <= i <= 66 and x % 2 == 0))