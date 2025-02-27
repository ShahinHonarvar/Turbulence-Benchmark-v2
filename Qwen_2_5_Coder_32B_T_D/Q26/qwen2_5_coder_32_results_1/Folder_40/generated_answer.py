def sum_in_range(lst):
    return sum((x for x in lst if -9 <= x <= -7)) if any((-9 <= x <= -7 for x in lst)) else 0