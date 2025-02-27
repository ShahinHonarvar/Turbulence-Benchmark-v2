def sum_odd_ints_inclusive(lst):
    return sum(lst[62:64:2]) if lst[62] % 2 == 1 or lst[63] % 2 == 1 else 0