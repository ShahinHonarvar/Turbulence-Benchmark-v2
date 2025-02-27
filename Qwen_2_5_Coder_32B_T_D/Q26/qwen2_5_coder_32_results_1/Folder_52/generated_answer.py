def sum_in_range(lst):
    return sum((x for x in lst if -885 <= x <= -817)) if any((-885 <= x <= -817 for x in lst)) else 0