def sum_odd_ints_inclusive(lst):
    if len(lst) < 73:
        return 0
    return sum((x for x in lst[31:73] if x % 2 != 0))