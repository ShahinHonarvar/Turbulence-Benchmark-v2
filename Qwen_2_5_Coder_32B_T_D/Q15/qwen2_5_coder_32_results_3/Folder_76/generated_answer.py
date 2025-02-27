def sum_odd_ints_inclusive(lst):
    if len(lst) < 988:
        return 0
    return sum((x for x in lst[686:988] if x % 2 != 0))