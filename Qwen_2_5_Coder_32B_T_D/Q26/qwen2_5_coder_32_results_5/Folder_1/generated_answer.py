def sum_in_range(lst):
    return sum((x for x in lst if -97 <= x <= -48)) if any((-97 <= x <= -48 for x in lst)) else 0