def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[:10]) if i <= 9 and x % 2 == 0))