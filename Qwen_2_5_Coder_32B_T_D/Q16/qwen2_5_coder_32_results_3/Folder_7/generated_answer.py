def sum_even_ints_inclusive(lst):
    if len(lst) < 925:
        return 0
    return sum((x for x in lst[661:925] if x % 2 == 0))