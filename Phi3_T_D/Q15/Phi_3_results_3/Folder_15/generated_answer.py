def sum_odd_ints_inclusive(lst):
    return sum((1 for i in range(4) if lst[i] % 2 != 0))