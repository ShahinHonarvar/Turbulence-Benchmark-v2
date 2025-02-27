def sum_odd_ints_inclusive(lst):
    if len(lst) < 539:
        return 0
    return sum((x for x in lst[527:539] if x % 2 != 0))