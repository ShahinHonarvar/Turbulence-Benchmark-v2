def sum_in_range(lst):
    return sum((x for x in lst if -74 <= x <= -17)) if any((-74 <= x <= -17 for x in lst)) else 0