def sum_in_range(lst):
    return sum((x for x in lst if 827 <= x <= 999)) if any((827 <= x <= 999 for x in lst)) else 0