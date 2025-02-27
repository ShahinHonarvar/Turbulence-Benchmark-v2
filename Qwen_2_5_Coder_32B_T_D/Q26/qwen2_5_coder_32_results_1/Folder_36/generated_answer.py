def sum_in_range(lst):
    return sum((x for x in lst if 465 <= x <= 927)) if any((465 <= x <= 927 for x in lst)) else 0