def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[:3]) if i <= 2 and x % 2 == 0))