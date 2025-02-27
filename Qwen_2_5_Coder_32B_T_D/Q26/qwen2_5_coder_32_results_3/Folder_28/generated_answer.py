def sum_in_range(lst):
    return sum([x for x in lst if 10 <= x <= 97]) if any((10 <= x <= 97 for x in lst)) else 0