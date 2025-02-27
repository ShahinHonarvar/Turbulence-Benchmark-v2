def sum_even_ints_inclusive(lst):
    if len(lst) < 69:
        return 0
    return sum((x for x in lst[13:69] if x % 2 == 0))