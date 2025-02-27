def sum_in_range(lst):
    total = sum((x for x in lst if 5 <= x <= 9))
    return total