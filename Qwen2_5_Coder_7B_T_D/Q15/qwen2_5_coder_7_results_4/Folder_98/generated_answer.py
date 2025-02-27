def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[:7]) if i <= 6 and x % 2 != 0))