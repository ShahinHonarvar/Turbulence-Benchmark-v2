def sum_even_ints_inclusive(lst):
    if len(lst) < 100:
        return 0
    return sum((x for x in lst[91:100] if x % 2 == 0))