def sum_in_range(lst):
    result = sum((x for x in lst if 3 <= x <= 4))
    return result