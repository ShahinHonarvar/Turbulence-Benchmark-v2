def sum_odd_ints_inclusive(lst):
    return sum((x for x in lst[527:539] if x % 2 != 0)) if len(lst) > 538 else 0