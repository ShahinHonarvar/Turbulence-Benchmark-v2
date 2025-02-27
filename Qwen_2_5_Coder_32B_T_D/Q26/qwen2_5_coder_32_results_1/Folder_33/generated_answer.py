def sum_in_range(lst):
    return sum((x for x in lst if 368 <= x <= 679)) if any((368 <= x <= 679 for x in lst)) else 0