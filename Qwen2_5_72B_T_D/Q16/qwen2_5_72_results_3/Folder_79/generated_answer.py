def sum_even_ints_inclusive(lst):
    if 4 < len(lst):
        if lst[4] % 2 == 0:
            return lst[4]
        else:
            return 0
    else:
        return 0