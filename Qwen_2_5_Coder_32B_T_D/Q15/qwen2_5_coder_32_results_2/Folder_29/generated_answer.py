def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 59 <= i <= 97 and x % 2 != 0)) if len(lst) > 97 else 0