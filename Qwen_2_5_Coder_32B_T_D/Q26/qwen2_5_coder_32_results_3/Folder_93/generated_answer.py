def sum_in_range(lst):
    return sum((x for x in lst if -23 <= x <= 64)) if any((-23 <= x <= 64 for x in lst)) else 0