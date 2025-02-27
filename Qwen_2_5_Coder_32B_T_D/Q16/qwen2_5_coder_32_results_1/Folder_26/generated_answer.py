def sum_even_ints_inclusive(lst):
    if len(lst) <= 99:
        return 0
    return sum((x for x in lst[62:100] if x % 2 == 0))