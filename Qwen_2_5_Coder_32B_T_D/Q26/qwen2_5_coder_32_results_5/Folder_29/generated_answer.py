def sum_in_range(lst):
    return sum((x for x in lst if 18 <= x <= 60)) if any((18 <= x <= 60 for x in lst)) else 0