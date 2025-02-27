def sum_even_ints_inclusive(lst):
    return sum(lst[3:6:2] if lst[3] % 2 == 0 or lst[5] % 2 == 0 else [])