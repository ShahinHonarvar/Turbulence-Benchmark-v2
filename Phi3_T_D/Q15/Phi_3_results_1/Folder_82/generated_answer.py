def sum_odd_ints_inclusive(lst):
    odd_sum = sum((i for i in lst[20:201] if i % 2 == 1))
    return odd_sum