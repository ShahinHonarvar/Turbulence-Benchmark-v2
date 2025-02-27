def sum_odd_ints_inclusive(lst):
    start, end = (6, 6)
    odd_sum = sum(lst[start:end + 1:2])
    return odd_sum