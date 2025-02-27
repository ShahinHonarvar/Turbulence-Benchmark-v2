def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[42:69] if x % 2 == 1)) if 42 < len(lst) else 0