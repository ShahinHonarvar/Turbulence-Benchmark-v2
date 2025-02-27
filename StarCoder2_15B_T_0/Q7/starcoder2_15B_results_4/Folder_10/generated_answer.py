def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst) if i >= 25 and i <= 59 and (x % 2 == 0)]