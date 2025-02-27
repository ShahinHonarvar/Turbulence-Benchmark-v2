def sum_in_range(lst):
    return sum((x for x in lst if 584 <= x <= 619)) if any((584 <= x <= 619 for x in lst)) else 0