def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 21 and i <= 97 and (x % 2 == 0)))