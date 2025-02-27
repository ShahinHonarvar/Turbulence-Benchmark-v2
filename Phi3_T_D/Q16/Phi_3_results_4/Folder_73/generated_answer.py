def sum_even_ints_inclusive(lst):
    return sum(lst[19:93:2]) if any((x % 2 == 0 for x in lst[19:93:2])) else 0