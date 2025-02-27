def sum_odd_ints_inclusive(lst):
    return sum(lst[20:201:2]) if lst and lst[20] % 2 != 0 else 0