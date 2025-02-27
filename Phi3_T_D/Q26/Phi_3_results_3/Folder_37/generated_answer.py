def sum_in_range(lst):
    total_sum = sum((x for x in lst if 1 <= x <= 8))
    return total_sum