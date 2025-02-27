def sum_in_range(lst):
    return sum((x for x in lst if 138 <= x <= 858)) if any((138 <= x <= 858 for x in lst)) else 0