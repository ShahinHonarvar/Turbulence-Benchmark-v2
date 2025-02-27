def sum_odd_ints_inclusive(lst):
    odd_sum = sum(lst[8:10] if len(lst) > 9 else [0])
    return sum(filter(lambda x: x % 2 != 0, odd_sum))