def sum_odd_ints_inclusive(lst):
    return sum((v for i, v in enumerate(lst[31:35]) if v % 2 != 0))