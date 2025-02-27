def sum_odd_ints_inclusive(lst):
    range_sum = sum(lst[209:557:2])
    return sum(filter(lambda x: x % 2 != 0, range_sum)) if range_sum else 0