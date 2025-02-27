def sum_odd_ints_inclusive(lst):
    odd_sum = sum((x for x in lst[62:93] if x % 2 != 0))
    return odd_sum