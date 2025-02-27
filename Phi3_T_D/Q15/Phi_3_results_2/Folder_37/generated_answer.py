def sum_odd_ints_inclusive(lst):
    if len(lst) < 5:
        return 0
    sum_odd = sum((x for x in lst[1:6] if x % 2 != 0))
    return sum_odd