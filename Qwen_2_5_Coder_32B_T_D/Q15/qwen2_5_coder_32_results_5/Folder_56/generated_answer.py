def sum_odd_ints_inclusive(lst):
    if lst and lst[0] % 2 != 0:
        return lst[0]
    return 0