def all_even_ints_inclusive(lst):
    return [n for i, n in enumerate(lst) if i >= 50 and i <= 200 and (n % 2 == 0)]